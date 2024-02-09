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
outputFolderpath = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\Testen\\OutputFiles'
segmente = os.listdir(outputFolderpath)
#"Preamble" um Vorgang abgestimmt mit Send Funktion zu starten
while pyperclip.paste() != 'start':
    time.sleep(0.05)
pyperclip.copy('loslegen')
#Pufferzeit (wahrscheinlich nicht notwendig)
time.sleep(1)
while len(segmente)<9:
    segmente = os.listdir(outputFolderpath)#Weil "segmente" sich verändert in jedem Durchlauf neu abfragen
    # Daten aus der Zwischenablage lesen
    data_url = pyperclip.paste()

    # Base64-Daten decodieren
    binary_data = base64.b64decode(data_url)

    
    output_file = outputFolderpath + '\\testFile.xlsx_segment_'+str((len(segmente)+1))
    with open(output_file, 'wb') as f:
            f.write(binary_data)

    pyperclip.copy('nextPlease')
    time.sleep(1)