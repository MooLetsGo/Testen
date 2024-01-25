#!/usr/bin/env python3
#=====================================================================================
# Image to B64-DATA converter
#
# Converts image files of type jpg, png, gif, svg into B64-Date-URL text-format
#
Version = "10"
#
#=====================================================================================
#


#   https://www.tutorialspoint.com/python/python_command_line_arguments.htm
#
#
#   https://pypi.org/project/pyclip/
#   pip install pyperclip
#


import os.path
import sys
import getopt
import pyperclip   #fuer Clipboardzugriff 
import base64


#----------------------------------------------------------------------------------------
# How do I print colored text to the terminal?
#
#  https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal

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

def print_help():
    print ('==========================================================')
    print ('Image to B64-DATA converter v'+Version+' :\r\n')
    print ('Converts JPG, PNG, GIF, SVG Images into B64-DATA text-format.\r\n')
    print ('---------------------------------------------------------')
    print ('Argument-format:\r\n')
    print ('b64_data_url.py --infile=<inputfile> --outfile=<outputfile> --clip \r\n')
    print ('Parameters:\r\n')
    print ('   --help shows help\r\n')
    print ('   --infile=<path_inputfile>\r\n')
    print ('   --outfile=<path_outputfile>\r\n\n')
    print ('   --height=<Image height pixels>')
    print ('   --heightp=<Image height (percent of page)>\r\n')
    print ('   --width=<Image width pixels>')
    print ('   --widthp=<Image width (percent of page)>\r\n')
    print ('   --clip copy text result into clipboard')
    print ('==========================================================')
    print ('Missing parameters width/height will be set to "auto" ')
    print ('==========================================================')


#----------------------------------------------------------------------------------------


#Argumente aus der Kommandozeile
argvx = sys.argv[1:]

#Init Variablen
imagefile_name = ''
imagefile_name_def = False
outputfile_name = ''
outputfile_name_def = False
copy_clipboard = False

auto_height = True
auto_width = True

image_height =''
image_heightp =''
image_width  =''
image_widthp =''

image_height_def = False
image_heightp_def = False
image_width_def = False
image_widthp_def = False

data_url = ''
prefix = ''
pre_postfix = ''
postfix_1 = '"'
postfix_2 = '>'

#----------------------------------------------------------------------------------------

#prüft i.F., ob die Argumente und Parameter vorhanden sind
try:
   # opts : Liste von Parameterpaaren (Option, Wert)
   # args:  hier nicht weiter benötigt, Liste der verbliebenen, nicht weiter ausgewerteten Parameter
   # siehe https://www.geeksforgeeks.org/getopt-module-in-python/
   
   # options: String of option letters that the script wants to recognize. Options that require an argument should be followed by a colon (:).
   
   # long_options: List of the string with the name of long options. Options that require arguments should be followed by an equal sign (=).

   # old: opts, args = getopt.getopt(argvx,"hci:o:",["help","clip","ifile=","ofile="])

   opts, args = getopt.getopt(argvx,"", ["help","clip","height=","heightp=","width=","widthp=","infile=","outfile="])
   # Achtung: verkürzte Schreibweisen clip --> "cl ... cli"  werden als Parameter auch akzeptiert und zugeordnet!

except getopt.GetoptError:
   #falsche undef. Argumente verwendet!  --> Abbruch

   # print('*** ERROR in arguments! ***')
   print(f"{bcolors.WARNING}\r\n*** ERROR in arguments! ***\r\n{bcolors.ENDC}")
   print('check arguments: ',argvx)
   sys.exit(2)

#----------------------------------------------------------------------------------------

#Argumente extrahiert, jetzt Bestimmung der Co-Parameter der Optionen
for opt, arg in opts:
   if opt.lower() in ("-h", "--help"):
      print_help()
      sys.exit()

   elif opt.lower() in ("-i", "--infile"):
      imagefile_name = arg

      if not(os.path.exists(imagefile_name)) :
        print(f"{bcolors.WARNING}")
        print('Warning:  Input file ' + '\''+imagefile_name + '\''+' does not exist!')
        print(f"{bcolors.ENDC}")
        sys.exit(2)
      else:
          imagefile_name_def = True  


   
   elif opt.lower() in ("-o", "--outfile"):
      outputfile_name = arg
      #outputfile_name_def = False
      
      outputfile_name = os.path.expanduser(outputfile_name)
      
      if not str(outputfile_name):    #string ist leer?
           print(f"{bcolors.WARNING}\r\n*** WARNING output filename path is empty !!! ***\r\n{bcolors.ENDC}")
           
            #pass  # mache NICHTS!
      else:
          #Überprüfung, ob der Ausgabeordner der Ausgabedatei existiert
          #Möglichkeit - Dateiname ohne Pfad --> d.h. lokale Datei!  --> prüfen auf /Pfade
          
          #print ( str(os.path.dirname (outputfile_name)))
          #print (os.path.exists (os.path.dirname (outputfile_name)))
          
          if (not str(os.path.dirname (outputfile_name))) or os.path.exists (os.path.dirname (outputfile_name)):
              outputfile_name_def = True
          

   elif opt.lower() in ("--height"):
      image_height = arg
      image_height_def = True
      auto_height = False

   elif opt.lower() in ("--width"):
      image_width = arg
      image_width_def = True
      auto_width = False

   elif opt.lower() in ("--heightp"):
      image_heightp = arg
      image_heightp_def = True
      auto_height = False

   elif opt.lower() in ("--widthp"):
      image_widthp = arg
      image_widthp_def = True
      auto_width = False

   elif opt.lower() in ("-c", "--clip"):
      copy_clipboard = True

# Keine Argumente --> Ausgabe der Hilfe & Ende
if (len(argvx) ==0):
    print_help()
    sys.exit(2)

# Festlegung der pre_postfix Einstellungen für die Abmessungsangaben der Grafik
# bspw. width=50% height=auto       width=30 height=90

if (image_height_def or image_width_def):
    
    if (image_height_def and image_width_def):
        pre_postfix = ' height="' + image_height + '"' + ' width="' + image_width + '"'
    
    if (image_height_def and not(image_width_def)):
        pre_postfix = ' height="' + image_height + '"' + ' width="auto"'

    if (not(image_height_def) and image_width_def):
        pre_postfix = ' height="auto"' + ' width="' + image_width + '"'


elif (image_heightp_def or image_widthp_def):

    if (image_heightp_def and image_widthp_def):
        pre_postfix = ' height="' + image_heightp + '%"' + ' width="' + image_widthp + '%"'
    
    if (image_heightp_def and not(image_widthp_def)):
        pre_postfix = ' height="' + image_heightp + '%"' + ' width="auto"'

    if (not(image_heightp_def) and image_widthp_def):
        pre_postfix = ' height="auto"' + ' width="' + image_widthp + '%"'

else:
    pass


#Prüfung des Typs der Grafik --> Anpassung der HTML-Prefixes
if (imagefile_name.lower()).endswith('.jpg'):
   prefix = '<img src="data:image/jpeg;charset=utf-8;base64,'

elif (imagefile_name.lower()).endswith('.jpeg'):
   prefix = '<img src="data:image/png;charset=utf-8;base64,'

elif (imagefile_name.lower()).endswith('.png'):
   prefix = '<img src="data:image/png;charset=utf-8;base64,'

elif (imagefile_name.lower()).endswith('.gif'):
   prefix = '<img src="data:image/gif;charset=utf-8;base64,'

elif (imagefile_name.lower()).endswith('.svg'):
   prefix = '<img src="data:image/svg+xml;charset=utf-8;base64,'

else:
   #Keine JPG, PNG, GIF oder SVG Datei als Argument!
   # print('\r\n*** ERROR input image must be .jpg/.png/.gif/.svg-type ! ***\r\n')

   print(f"{bcolors.WARNING}\r\n*** ERROR input image must be .jpg/.png/.gif/.svg-type ! ***\r\n{bcolors.ENDC}")
   sys.exit(2)



with open(imagefile_name, 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    
    data_url = prefix + base64_encoded_data.decode('utf-8')+postfix_1+pre_postfix+postfix_2


if outputfile_name_def:
    with open(outputfile_name, "w") as text_file:
        text_file.write(data_url)
        print(f"{bcolors.OKGREEN}\r\n*** Output filename successfully written !!! ***\r\n{bcolors.ENDC}")
else:
    print(f"{bcolors.WARNING}\r\n*** WARNING output filename path not defined !!! ***\r\n{bcolors.ENDC}")


# Kopiert data_url in Zwischenablage
if copy_clipboard:
      pyperclip.copy(data_url)
      print(f"{bcolors.OKGREEN}\r\n*** B64 block successfully copied to clipboard !!! ***\r\n{bcolors.ENDC}")

