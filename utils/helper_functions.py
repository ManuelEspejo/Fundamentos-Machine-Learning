import os
import zipfile

import gdown
from IPython import get_ipython


def download_data(file_id: str, data_dir=None):
    """
    Descarga y descomprime un archivo ZIP de datos desde Google Drive.
    
    Args:
        file_id (str): ID del archivo en Google Drive
        data_dir (str, optional): Directorio donde se guardarán los datos. 
            Si no se especifica, se detectará automáticamente según el entorno.
    """
    # Detectar si estamos en Colab
    in_colab = 'google.colab' in str(get_ipython())
    
    # Configurar el directorio de datos según el entorno
    if data_dir is None:
        data_dir = '/content/data' if in_colab else './data/raw'
    
    # Convertir a ruta absoluta para mejor depuración
    data_dir = os.path.abspath(data_dir)
    print(f"Directorio de destino: {data_dir}")
    
    # Variables y rutas
    zip_url = f'https://drive.google.com/uc?id={file_id}'
    print(f"URL de descarga: {zip_url}")
    
    # Crear directorio si no existe
    os.makedirs(data_dir, exist_ok=True)
    
    # Descargar el archivo ZIP
    output = f'{data_dir}/data.zip'
    print(f"Descargando archivo ZIP a: {output}")
    success = gdown.download(zip_url, output, quiet=False)
    
    if not success:
        print("Error: La descarga falló. Verifica el ID del archivo y asegúrate de que sea público.")
        return None
        
    if not os.path.exists(output):
        print("Error: El archivo ZIP no se descargó correctamente.")
        return None
    
    print(f"Tamaño del archivo ZIP: {os.path.getsize(output)} bytes")
    
    # Descomprimir el archivo ZIP
    try:
        with zipfile.ZipFile(output, 'r') as zip_ref:
            print("Contenido del ZIP:", zip_ref.namelist())
            zip_ref.extractall(data_dir)
            print(f"Archivos extraídos en: {data_dir}")
    except zipfile.BadZipFile:
        print("Error: El archivo descargado no es un ZIP válido")
        return None
        
    # Eliminar el archivo ZIP después de extraer
    os.remove(output)
    
    # Listar los archivos extraídos
    archivos = os.listdir(data_dir)
    print("\nArchivos disponibles en el directorio:")
    for archivo in archivos:
        ruta_completa = os.path.join(data_dir, archivo)
        tamaño = os.path.getsize(ruta_completa)
        print(f"- {archivo} ({tamaño} bytes)")
    
    return data_dir

download_data('1FqMwy0E4O7evqMYIm23y2UjI8QwgbQ9h')