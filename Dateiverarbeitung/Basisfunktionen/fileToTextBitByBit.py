import filetype
import base64
import sys
import os.path
import pyperclip
import time

#----------------------------------------------------------------------------------------

class bcolors:
    HEADER     = '\033[95m'
    OKBLUE     = '\033[94m'
    OKCYAN     = '\033[96m'
    OKGREEN    = '\033[92m'
    WARNING    = '\033[93m'
    FAIL       = '\033[91m'
    ENDC       = '\033[0m'
    BOLD       = '\033[1m'
    UNDERLINE  = '\033[4m'
    CEND       = '\33[0m'

    CBOLD      = '\33[1m'
    CITALIC    = '\33[3m'
    CURL       = '\33[4m'
    CBLINK     = '\33[5m'
    CBLINK2    = '\33[6m'
    CSELECTED  = '\33[7m'

    CBLACK     = '\33[30m'
    CRED       = '\33[31m'
    CGREEN     = '\33[32m'
    CYELLOW    = '\33[33m'
    CBLUE      = '\33[34m'
    CVIOLET    = '\33[35m'
    CBEIGE     = '\33[36m'
    CWHITE     = '\33[37m'

    CBLACKBG   = '\33[40m'
    CREDBG     = '\33[41m'
    CGREENBG   = '\33[42m'
    CYELLOWBG  = '\33[43m'
    CBLUEBG    = '\33[44m'
    CVIOLETBG  = '\33[45m'
    CBEIGEBG   = '\33[46m'
    CWHITEBG   = '\33[47m'

    CGREY      = '\33[90m'
    CRED2      = '\33[91m'
    CGREEN2    = '\33[92m'
    CYELLOW2   = '\33[93m'
    CBLUE2     = '\33[94m'
    CVIOLET2   = '\33[95m'
    CBEIGE2    = '\33[96m'
    CWHITE2    = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

#----------------------------------------------------------------------------------------
    
#Init Variablen
inputfile_name = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\Testen\\InputFiles\\testFile.xlsx'

data = ''
prefix = ''
postfix_1 = '"'
postfix_2 = '>'

ackStart = 'loslegen'
ack = 'nextPlease'

blockLength = 5120 #5KB
nextBlockPos = 0
#----------------------------------------------------------------------------------------

#Pfad von "inputfile" wird auf Existenz überprüft
if not(os.path.exists(inputfile_name)):
    print(f"{bcolors.WARNING}")
    print('Warning:  Input file ' + '\''+inputfile_name + '\''+' does not exist!')
    print(f"{bcolors.ENDC}")
    sys.exit(2)

#----------------------------------------------------------------------------------------

#Ermittlung und Prüfung des Dateityps --> HTML-Präfix generieren (DateiEndung/MIMEType)
kind = filetype.guess(inputfile_name)
if kind is None:
    print(f"{bcolors.WARNING}\r\n*** ERROR Invalid filetype ! ***\r\n{bcolors.ENDC}")
    sys.exit(2)     
else:
    prefix = '<src="data:' + kind.extension + ';charset=utf-8;base64,' #DateiEndung wird angehängt (nicht der MIMEType)

#----------------------------------------------------------------------------------------
#Prefixbehandlung noch machen
#Input Datei in Segment-Dateien aufsplitten
with open(inputfile_name, 'rb') as binary_file:
        segment_number = 1
        while True:
            block_data = binary_file.read(blockLength)
            if not block_data:
                break
            with open(f'{inputfile_name}_segment_{segment_number}', 'wb') as segment_file:
                segment_file.write(block_data)
            segment_number += 1

#Segmentdateien B64 kodieren, nacheinander in die Zwischenablage kopieren und wenn nicht mehr benötigt löschen
#Dateipfad wo die Segmente abgelegt werden für das finale Tool anpassen/ geeignet wählen
inputFolderpath = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\Testen\\InputFiles'
#Dateipfad evtl. auf Existenz und vorhandenen Inhalt überprüfen
segmente = os.listdir(inputFolderpath)

i = 1
for segmentfile_name in segmente[1:]:#[1:] Anweisung nur wegen aktuellem Dateipfad weil das testFile noch da drin liegt
    #Aktuelles Segment base64 kodieren
    with open(inputFolderpath + '\\' + segmentfile_name, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        data_url=base64_encoded_data.decode('utf-8')

    #"Preamble" um Vorgang abgestimmt mit Send Funktion zu starten
    if i == 1:
        pyperclip.copy('start')
        while pyperclip.paste() != ackStart:
            time.sleep(0.05)
    i += 1
                
    #Entstandene base64 dataURL in die Zwischenablage schreiben und auf ein acknowledgement warten
    pyperclip.copy(data_url)
    print(f"{bcolors.OKGREEN}\r\n*** B64 block successfully copied to clipboard !!! ***\r\n{bcolors.ENDC}")
    while pyperclip.paste() != ack:
            time.sleep(0.05)

    #Löschen des aktuellen Segmentes, wenn nicht mehr benötigt (durch das ack wird dies klar); Evtl. Farben für Error Messages noch machen
    try:
        os.remove(inputFolderpath + '\\' + segmentfile_name)
        print(f"Segment file '{inputFolderpath + '\\' + segmentfile_name}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting segment file '{inputFolderpath + '\\' + segmentfile_name}': {e}")

#postfixbehandlung noch machen  

