import base64
from io import BytesIO
from PIL import Image

# Dateipfad zur Textdatei
textfile_path = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\VSCode\\Testen\\ImageToB64\\IMG.txt'

# Daten aus der Textdatei lesen
with open(textfile_path, 'r') as file:
    data_url = file.read().strip()

# Daten-URL parsen, um MIME-Typ und Base64-kodierte Daten zu extrahieren --Ist hier falsch gemacht!!!--
mime_type, base64_data = data_url.split(',')[1].split(';')[0], data_url.split(',')[1]

# Base64-Daten decodieren
binary_data = base64.b64decode(base64_data)

# Bilddaten in ein BytesIO-Objekt laden
image_data = BytesIO(binary_data)

# PIL-Bildobjekt erstellen
image = Image.open(image_data)

# Bild in .jpg konvertieren und speichern
image.convert('RGB').save('ausgabe.jpg', format='JPEG')

# Optional: Bild anzeigen
image.show()
