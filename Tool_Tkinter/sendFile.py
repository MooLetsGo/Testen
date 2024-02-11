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

def fileToTextBitByBit():
           
    #Init Variablen
    inputfile = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\Testen\\InputFiles\\testFile.xlsx'
    blockLength = 5120 #5KB
    #----------------------------------------------------------------------------------------

    #Pfad von "inputfile" wird auf Existenz überprüft
    if not(os.path.exists(inputfile)):
        print(f"{bcolors.WARNING}")
        print('Warning:  Input file ' + '\''+inputfile + '\''+' does not exist!')
        print(f"{bcolors.ENDC}")
        sys.exit(2)

    #----------------------------------------------------------------------------------------

    #Ermittlung und Prüfung des Dateityps --> HTML-Präfix generieren (DateiEndung/MIMEType)
    kind = filetype.guess(inputfile)
    if kind is None:
        print(f"{bcolors.WARNING}\r\n*** ERROR Invalid filetype ! ***\r\n{bcolors.ENDC}")
        sys.exit(2)     
    else:
        prefix = '<src="data:' + kind.extension + ';charset=utf-8;base64,' #DateiEndung wird angehängt (nicht der MIMEType)

    #Dateiname ermitteln
    inputfile_name = ''
    #----------------------------------------------------------------------------------------
        
    #Protokoll - Vorgang abgestimmt mit der Receive Funktion starten
    pyperclip.copy('toRe_StartSending')#Verfügbarkeit anfragen
    while pyperclip.paste() != 'toSe_StartSending':#Warten bis Verfügbarkeit bestätigt
        time.sleep(0.05)
    
    #Prefixbehandlung noch machen
    
    
    segment_number = 1
    nextBlockPos = 0
    #Ordner, in dem das Segment kurzzeitig abgelegt wird; für das finale Tool anpassen/ geeignet wählen / evtl. Ordner, der durch das Tool (exe) generiert wird
    segment_stack = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\Testen\\InputFiles'
    #Input Datei segmentweise versenden
    while True:

        #Inputdatei öffnen und passendes Segment im Segment Stack Ordner erzeugen 
        with open(inputfile, 'rb') as binary_file:
            binary_file.seek(nextBlockPos,0)
            block_data = binary_file.read(blockLength)
            #Wenn kein Segment mehr gebildet werden kann -> Versenden beenden
            if not block_data:
                #Protokoll - Der Receive Funktion mitteilen, dass es keine Daten mehr zu versenden gibt
                pyperclip.copy('toRe_Weiter;Beenden')
                break
            with open(f'{segment_stack + '\\' + inputfile_name}_segment_{segment_number}', 'wb') as segment_file:
                segment_file.write(block_data)
        
        #Generiertes Segment versenden
        segmentfile_name = os.listdir(segment_stack)[1]#[1] Anweisung nur wegen aktuellem Dateipfad weil das testFile noch da drin liegt
        #Segment base64 kodieren
        with open(segment_stack + '\\' + segmentfile_name, 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_endcoded_segment= 'toRe_Weiter;'+base64_encoded_data.decode('utf-8')#Protokoll - Header um der Receive Funktion zu sagen, dass ein Segment zum verarbeiten in der Zwischenablage liegt
        #Base64 kodiertes Segment in die Zwischenablage schreiben
        pyperclip.copy(base64_endcoded_segment)
        print(f"{bcolors.OKGREEN}\r\n*** B64 block successfully copied to clipboard !!! ***\r\n{bcolors.ENDC}")

        #Protokoll - Warten, bis die Receive Funktion den Empfang bestätigt hat
        while pyperclip.paste() != 'toSe_ProceedSending':
            time.sleep(0.05)
        
        #Löschen des Segmentes
        try:
            os.remove(segment_stack + '\\' + segmentfile_name)
            print(f"Segment file '{segment_stack + '\\' + segmentfile_name}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting segment file '{segment_stack + '\\' + segmentfile_name}': {e}")
        
        #Laufvariablen neu berechnen
        nextBlockPos = nextBlockPos + blockLength  
        segment_number += 1