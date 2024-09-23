import requests
import os

# URL del archivo
url = 'https://campusvirtual.ucc.edu.co/d2l/le/658193/discussions/posts/2562183/ViewAttachment?fileId=28009426 '

# Ruta donde deseas descargar el archivo
directorio_descarga = 'C:\Users\Equipo\Downloads'

# Asegúrate de que el directorio de descarga exista
if not os.path.exists(directorio_descarga):
    os.makedirs(directorio_descarga)

# Nombre del archivo
nombre_archivo = 'file.pdf'

# Ruta completa donde se guardará el archivo
ruta_completa = os.path.join(directorio_descarga, nombre_archivo)

# Descargar el archivo
response = requests.get(url)

# Guardar el archivo en la ruta especificada
with open(ruta_completa, 'wb') as file:
    file.write(response.content)

print(f'Archivo descargado exitosamente en: {ruta_completa}')