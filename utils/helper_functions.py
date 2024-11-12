import os
import zipfile
from urllib.parse import parse_qs, urlparse

import gdown
import requests
from IPython import get_ipython


def download_data(url_or_id: str, data_dir=None, keep_zip=False):
    """
    Descarga y descomprime un archivo ZIP de datos desde Google Drive u otra URL.
    
    Args:
        url_or_id (str): URL completa o ID del archivo en Google Drive. 
            También puede ser una URL directa a un archivo ZIP desde otra fuente.
        data_dir (str, optional): Directorio donde se guardarán los datos. 
            Si no se especifica, se detectará automáticamente según el entorno.
        keep_zip (bool, optional): Si True, no elimina el archivo ZIP después de descomprimirlo.
            Por defecto es False.
    """
    # Detectar si estamos en Colab
    in_colab = 'google.colab' in str(get_ipython())
    
    # Configurar el directorio de datos según el entorno
    if data_dir is None:
        if in_colab:
            data_dir = '/content/data'
        else:
            # Obtener la ruta del directorio raíz del proyecto
            current_file = os.path.abspath(__file__)  # Ruta del archivo actual (helper_functions.py)
            project_root = os.path.dirname(os.path.dirname(current_file))  # Subir dos niveles
            data_dir = os.path.join(project_root, 'data', 'raw')
    
    # Convertir a ruta absoluta para mejor depuración
    data_dir = os.path.abspath(data_dir)
    
    # Crear directorio si no existe
    os.makedirs(data_dir, exist_ok=True)
    
    # Procesar el enlace o ID de archivo
    if 'drive.google.com' in url_or_id:
        # Si es un enlace de Google Drive, extraer el file_id
        file_id = extract_file_id(url_or_id)
        if file_id is None:
            print("Error: Enlace de Google Drive no válido.")
            return None
        download_url = f'https://drive.google.com/uc?id={file_id}'
    else:
        # Asumir que es un ID de Google Drive directo o una URL genérica
        download_url = f'https://drive.google.com/uc?id={url_or_id}' if len(url_or_id) == 33 else url_or_id
    
    # Ruta para guardar el archivo ZIP
    output = os.path.join(data_dir, 'data.zip')
    
    # Descargar el archivo
    try:
        if 'drive.google.com' in download_url:
            print("Descargando desde Google Drive...")
            gdown.download(download_url, output, quiet=True)
        else:
            print("Descargando desde una URL genérica...")
            response = requests.get(download_url, stream=True)
            if response.status_code == 200:
                with open(output, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print("Descarga completada.")
            else:
                print(f"Error en la descarga: código de estado {response.status_code}")
                return None
    except Exception as e:
        print(f"Error en la descarga: {e}")
        return None
    
    # Verificar tamaño del archivo descargado
    if not os.path.exists(output):
        print("Error: El archivo ZIP no se descargó correctamente.")
        return None
    
    print(f"Tamaño del archivo ZIP: {os.path.getsize(output)} bytes")
    
    # Descomprimir el archivo ZIP
    try:
        with zipfile.ZipFile(output, 'r') as zip_ref:
            print("Contenido del ZIP:", zip_ref.namelist())
            zip_ref.extractall(data_dir)
    except zipfile.BadZipFile:
        print("Error: El archivo descargado no es un ZIP válido.")
        return None
        
    # Eliminar el archivo ZIP si no se desea conservar
    if not keep_zip:
        os.remove(output)
    
    # Listar los archivos extraídos
    archivos = os.listdir(data_dir)
    print("\nArchivos disponibles:")
    for archivo in archivos:
        tamaño = os.path.getsize(os.path.join(data_dir, archivo))
        print(f"- {archivo} ({tamaño} bytes)")

    return None


def extract_file_id(url):
    """
    Extrae el ID del archivo desde una URL de Google Drive.
    
    Args:
        url (str): URL de Google Drive.
    
    Returns:
        str: ID del archivo, o None si no se encuentra un ID válido.
    """
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    # Buscar el ID en los parámetros de la URL
    if 'id' in query_params:
        return query_params['id'][0]
    # Buscar el ID en la ruta de la URL, en el formato "/d/<file_id>/"
    elif 'drive.google.com' in parsed_url.netloc and '/file/d/' in parsed_url.path:
        return parsed_url.path.split('/')[3]
    return None

def plot_example_relationships():
    import matplotlib.pyplot as plt
    import numpy as np

    # Configuración general de las gráficas
    plt.figure(figsize=(12, 10))

    # 1. Variable que aumenta y la satisfacción del cliente también aumenta
    # Ejemplo: Calidad del Producto (de 0 a 100)
    np.random.seed(0)  # Para reproducibilidad
    calidad_producto = np.linspace(0, 100, 100)
    satisfaccion_cliente_1 = calidad_producto + np.random.normal(0, 10, 100)  # Añadimos ruido

    plt.subplot(2, 2, 1)
    plt.scatter(calidad_producto, satisfaccion_cliente_1, color='blue')
    plt.title('Calidad del Producto vs. Satisfacción del Cliente')
    plt.xlabel('Calidad del Producto')
    plt.ylabel('Satisfacción del Cliente (0-100)')
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    # 2. Variable que disminuye y la satisfacción del cliente aumenta
    # Ejemplo: Tiempo de Espera en Soporte (Segundos)
    tiempo_espera = np.linspace(300, 0, 100)  # De 300 a 0 segundos
    satisfaccion_cliente_2 = 100 - tiempo_espera / 3 + np.random.normal(0, 5, 100)

    plt.subplot(2, 2, 2)
    plt.scatter(tiempo_espera, satisfaccion_cliente_2, color='green')
    plt.title('Tiempo de Espera vs. Satisfacción del Cliente')
    plt.xlabel('Tiempo de Espera (Segundos)')
    plt.ylabel('Satisfacción del Cliente (0-100)')
    plt.xlim(0, 300)
    plt.ylim(0, 100)

    # 3. Variable que aumenta y la satisfacción del cliente disminuye
    # Ejemplo: Precio del Producto (en USD)
    precio_producto = np.linspace(0, 200, 100)
    satisfaccion_cliente_3 = 100 - precio_producto / 2 + np.random.normal(0, 10, 100)

    plt.subplot(2, 2, 3)
    plt.scatter(precio_producto, satisfaccion_cliente_3, color='red')
    plt.title('Precio del Producto vs. Satisfacción del Cliente')
    plt.xlabel('Precio del Producto (USD)')
    plt.ylabel('Satisfacción del Cliente (0-100)')
    plt.xlim(0, 200)
    plt.ylim(0, 100)

    # 4. Variable que disminuye y la satisfacción del cliente disminuye
    # Ejemplo: Nivel de Personalización (Porcentaje)
    nivel_personalizacion = np.linspace(100, 0, 100)
    satisfaccion_cliente_4 = nivel_personalizacion + np.random.normal(0, 10, 100)

    plt.subplot(2, 2, 4)
    plt.scatter(nivel_personalizacion, satisfaccion_cliente_4, color='purple')
    plt.title('Nivel de Personalización vs. Satisfacción del Cliente')
    plt.xlabel('Nivel de Personalización (%)')
    plt.ylabel('Satisfacción del Cliente (0-100)')
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    plt.tight_layout()
    plt.show()

plot_example_relationships()
