import tkinter as tk
from tkinter import filedialog
import fileToTextWithGuiTest


def choose_file():
    file_path = filedialog.askopenfilename(title="Datei auswählen")
    if file_path:
        print(f"Ausgewählte Datei: {file_path}")
    return file_path

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("500x500 GUI")

# Festlegen der Größe auf 500x500 Pixel
root.geometry("500x500")

# Erstellen von Widgets
send_button = tk.Button(root, text="Senden", command=lambda: fileToTextWithGuiTest.fileToTextWithGuiTest(choose_file()), width=30, height=5)
send_button.place(relx=0.7, rely=0.22, anchor=tk.E)

black_bar = tk.Label(root, bg="black", width=500, height=1)
black_bar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Starten der Tkinter-Schleife
root.mainloop()
