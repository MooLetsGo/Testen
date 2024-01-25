import base64
from io import BytesIO
from PIL import Image

# Dateipfad zur Textdatei
textfile_path = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\FileToText_B64\\encodedFile.txt'

# Daten aus der Textdatei lesen
with open(textfile_path, 'r') as file:
    data_url = file.read().strip()

# Daten-URL parsen, um MIME-Typ und Base64-kodierte Daten zu extrahieren
mime_type, base64_data = data_url.split(';')[0].split(':')[1], data_url.split(',')[1]

# Base64-Daten decodieren
binary_data = base64.b64decode(base64_data)

output_file_path = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\TextToFile_B64\\decodedFile.xlsx'

with open(output_file_path, 'wb') as f:
    f.write(binary_data)