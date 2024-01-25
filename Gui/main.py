import tkinter as tk
from tkinter import filedialog
import sendFile
import receiveFile


def choose_file():
    file = filedialog.askopenfilename(title="Datei auswählen")
    if file:
        print(f"Ausgewählte Datei: {file}")
    return file

def choose_filepath():
    file_path = filedialog.askdirectory(title="Dateipfad auswählen")
    if file_path:
        print(f"Ausgewählter Dateipfad: {file_path}")
    return file_path

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("500x500 GUI")

# Festlegen der Größe auf 500x500 Pixel
root.geometry("500x500")

# Erstellen von Widgets
send_button = tk.Button(root, text="Senden", command=lambda: sendFile.fileToTextToClip(choose_file()) , width=30, height=5)
send_button.place(relx=0.7, rely=0.22, anchor=tk.E)

black_bar = tk.Label(root, bg="black", width=500, height=1)
black_bar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

receive_button = tk.Button(root, text="Empfangen", command=lambda: receiveFile.textFromClipToFile(choose_filepath()), width=30, height=5)
receive_button.place(relx=0.7, rely=0.74, anchor=tk.E)

# Starten der Tkinter-Schleife
root.mainloop()
