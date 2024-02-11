import base64
import pyperclip
import os.path
import time

#Funktion nimmt sich geregelt b64 kodierte Segmente aus der Zwischenablage und speichert diese als Binärdateisegmente
def textToFileBitByBit():

    #Init Variablen
    outputfile = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\Testen\\OutputFiles'
    blockLength = 5120 #5KB

    #Protokoll - Vorgang abgestimmt mit der Send Funktion starten
    while pyperclip.paste() != 'toRe_StartSending':#Warten auf Startsignal
                time.sleep(0.05)
    pyperclip.copy('toSe_StartSending')#Empfangsbereitschaft bestätigen
    
    #Protokoll - Warten bis ein Segment zum verarbeiten in der Zwischenablage liegt
    while pyperclip.paste().split('_')[1].split(';')[0] != 'Weiter':
        time.sleep(0.05)

    segment_stack = 'C:\\Users\\morit\\OneDrive\\Studium\\6. Semester\\Studienarbeit 2\\Umsetzung\\VSCode\\Testen\\Testen\\OutputFiles'
    #Segmente der Inputdatei empfangen
    #Protokoll - Empfangen Algorithmus solange ausführen, bis die Send Funktion den Vorgang beendet
    while pyperclip.paste().split('_')[1].split(';')[1] != 'Beenden':
        
        #Segment aus der Zwischenablage lesen
        base64_endcoded_segment = pyperclip.paste().split(';')[1]
        #Segment dekodieren
        binary_file_data = base64.b64decode(base64_endcoded_segment)
        #Passendes Segment im Segment Stack Ordner erzeugen
        segmente = os.listdir(segment_stack)
        segment_file = segment_stack + '\\testFile.xlsx_segment_'+str(len(segmente)+1)#Name/ Pfad noch hartkodiert!!!
        print(segment_file)
        with open(segment_file, 'wb') as binary_file:
                binary_file.write(binary_file_data)

        #Protokoll - Der Send Funktion mitteilen, dass das nächste Segment empfangen werden kann
        pyperclip.copy('toSe_ProceedSending')
        #Protokoll - Warten, bis das nächste Segment von der Send Funktion gesendet wurde
        while pyperclip.paste().split('_')[1].split(';')[0] != 'Weiter':
            time.sleep(0.05)
        #time.sleep(2)
    
    #Ursprüngliche Datei aus Segmenten generieren
    nextBlockPos = 0
    output_file = segment_stack + '\\decodedFile.xlsx'
    with open(output_file, 'wb') as original_file:
           segmente = os.listdir(segment_stack)
           for segment in segmente[1:]:
                  with open(segment_stack+'\\'+segment, 'rb') as segment_data:
                         original_file.seek(nextBlockPos,0)
                         original_file.write(segment_data.read())
                         nextBlockPos = nextBlockPos + blockLength