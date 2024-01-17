import filetype
import base64
import getopt
import sys
import os.path

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


#Argumente aus der Kommandozeile
argvx = sys.argv[1:]

#Init Variablen
file_name = ''
file_name_def = False

data_url = ''
prefix = ''
postfix_1 = '"'
postfix_2 = '>'

#----------------------------------------------------------------------------------------

#prüft i.F., ob die Argumente und Parameter vorhanden sind
try:
    opts, args = getopt.getopt(argvx,"",["infile=","outfile="])

except getopt.GetoptError:
    #falsche undef. Argumente verwendet!  --> Abbruch
    # print('*** ERROR in arguments! ***')
    print(f"{bcolors.WARNING}\r\n*** ERROR in arguments! ***\r\n{bcolors.ENDC}")
    print('check arguments: ',argvx)
    sys.exit(2)

#----------------------------------------------------------------------------------------

#Argumente auslesen und überprüfen
for opt, arg in opts:
    if opt.lower() in ("--infile"):
        file_name = arg #file_name bekommt den angegebenen Pfad für das Argument --infile zugewiesen

        #Pfad wird auf Existenz überprüft
        if not(os.path.exists(file_name)):
            print(f"{bcolors.WARNING}")
            print('Warning:  Input file ' + '\''+file_name + '\''+' does not exist!')
            print(f"{bcolors.ENDC}")
            sys.exit(2)
        else:
            file_name_def = True #Aktuell nicht benötigte Variable    

#----------------------------------------------------------------------------------------

#Ermittlung und Prüfung des Dateityps --> HTML-Präfix generieren (MIMEType)
kind = filetype.guess(file_name)
if kind is None:
    print(f"{bcolors.WARNING}\r\n*** ERROR Invalid filetype ! ***\r\n{bcolors.ENDC}")
    sys.exit(2)     
else:
    prefix = '<' + kind.mime + ';charset=utf-8;base64,'

#----------------------------------------------------------------------------------------

#Datei mit B64-Verfahren in Text konvertieren --> data_url
with open(file_name, 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    
    data_url = prefix + base64_encoded_data.decode('utf-8')+postfix_1+postfix_2