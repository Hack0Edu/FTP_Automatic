import ftplib
import json

# Cargar las credenciales desde un archivo JSON
with open('credentials.json') as json_file:
    credentials = json.load(json_file)

# Información de las credenciales FTP
ftp_host = credentials['ftp_host']
ftp_user = credentials['ftp_user']
ftp_pass = credentials['ftp_pass']

# Conectar al servidor FTP
ftp = ftplib.FTP(ftp_host)
ftp.login(ftp_user, ftp_pass)

# Directorio remoto donde se encuentra el sitio web
remote_directory = 'public_html/'

# Ruta al archivo index.html local
local_index_file = 'index.html'

# Cargar el contenido del archivo index.html
with open(local_index_file, 'rb') as file:
    ftp.storbinary('STOR ' + remote_directory + 'index.html', file)

# Cerrar la conexión FTP
ftp.quit()

print("Sitio web actualizado exitosamente.")
