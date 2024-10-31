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
        data_dir = '/content/data' if in_colab else './data/raw'
    
    # Convertir a ruta absoluta para mejor depuración
    data_dir = os.path.abspath(data_dir)
    print(f"Directorio de destino: {data_dir}")
    
    # Crear directorio si no existe
    os.makedirs(data_dir, exist_ok=True)
    
    # Procesar el enlace o ID de archivo
    if 'drive.google.com' in url_or_id:
        # Si es un enlace de Google Drive
        file_id = extract_file_id(url_or_id)
        if file_id is None:
            print("Error: Enlace de Google Drive no válido.")
            return None
        download_url = f'https://drive.google.com/uc?id={file_id}'
    else:
        # Asumir que es una URL directa a un archivo ZIP
        download_url = url_or_id
    
    # Ruta para guardar el archivo ZIP
    output = os.path.join(data_dir, 'data.zip')
    print(f"URL de descarga: {download_url}")
    
    # Descargar el archivo
    try:
        if 'drive.google.com' in download_url:
            print("Descargando desde Google Drive...")
            gdown.download(download_url, output, quiet=False)
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
            print(f"Archivos extraídos en: {data_dir}")
    except zipfile.BadZipFile:
        print("Error: El archivo descargado no es un ZIP válido.")
        return None
        
    # Eliminar el archivo ZIP si no se desea conservar
    if not keep_zip:
        os.remove(output)
    
    # Listar los archivos extraídos
    archivos = os.listdir(data_dir)
    print("\nArchivos disponibles en el directorio:")
    for archivo in archivos:
        ruta_completa = os.path.join(data_dir, archivo)
        tamaño = os.path.getsize(ruta_completa)
        print(f"- {archivo} ({tamaño} bytes)")
    
    return data_dir



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