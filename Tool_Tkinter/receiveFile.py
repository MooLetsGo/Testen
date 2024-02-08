import base64
import pyperclip
import os.path
import time

#Funktion nimmt sich geregelt b64 kodierte Segmente aus der Zwischenablage und speichert diese als Binärdateisegmente
def textToFileBitByBit():
    outputFolderpath = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\Testen\\OutputFiles'
    segmente = os.listdir(outputFolderpath)
    #"Preamble" um Vorgang abgestimmt mit Send Funktion zu starten
    while pyperclip.paste() != 'start':
                time.sleep(0.05)
    pyperclip.copy('loslegen')
    #Pufferzeit (wahrscheinlich nicht notwendig)
    time.sleep(1)
    while len(segmente)<8:#Bedingung noch hartkodiert!!!
        segmente = os.listdir(outputFolderpath)#Weil "segmente" sich verändert in jedem Durchlauf neu abfragen
        # Daten aus der Zwischenablage lesen
        data_url = pyperclip.paste()
        # Base64-Daten decodieren
        binary_data = base64.b64decode(data_url)

        
        output_file = outputFolderpath + '\\testFile.xlsx_segment_'+str(len(segmente)+1)#Name/ Pfad noch hartkodiert!!!
        print(output_file)
        with open(output_file, 'wb') as f:
                f.write(binary_data)
                
        #ack für Senden Funktion
        pyperclip.copy('nextPlease')
        time.sleep(2)#Pufferzeit (wahrscheinlich nicht notwendig)