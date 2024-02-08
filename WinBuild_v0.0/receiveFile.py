import base64
import pyperclip

def textFromClipToFile(filepath:str):
    # Daten aus der Zwischenablage lesen
    data_url = pyperclip.paste()

    # Daten-URL parsen, um Dateiendung (MIME-Typ) und Base64-kodierte Daten zu extrahieren
    extension, base64_data = data_url.split(';')[0].split(':')[1], data_url.split(',')[1]

    # Base64-Daten decodieren
    binary_data = base64.b64decode(base64_data)

    output_file_path = filepath + '\\decodedFile.'+extension

    with open(output_file_path, 'wb') as f:
        f.write(binary_data)