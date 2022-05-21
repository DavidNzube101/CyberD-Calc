import tkinter as tk
from tkinter import ttk, filedialog
import pyttsx3 as voice
from PIL import Image
import pytesseract

engine = voice.init()

def extract():
    def scanImage():
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img = filedialog.askopenfilename()
        extractedText = pytesseract.image_to_string(img)
        print(extractedText)
        extractedTextEdit = extractedText.replace('', '© CyberD Calc 2021')
        file = open("EXTRACTED TEXT.txt", "wb")
        file.close()

        file = open("EXTRACTED TEXT.txt", "r+")
        line = file.write(extractedTextEdit)
        file.close()

        done = tk.Label(root, text="✔")
        done.pack()
        doneL = tk.Label(root, text="Done, Extracted text.\nGo to CyberD Calc directory and look for 'EXTRACTED TEXT.txt', that's your extracted text.", font=("Albertus 15 bold"), fg="green")
        doneL.pack()
        engine.say("Done, Extracted text. Go to CyberD Calc directory and look for 'EXTRACTED TEXT.txt', that's your extracted text")
        engine.runAndWait()

    root = tk.Tk()
    root.title("Text Extractor")
    root.iconbitmap("CYBIcon.ico")

    introL = tk.Label(root, text="Text Extractor", font=("Tahoma 30 bold"), fg="purple")
    introL.pack()

    button = ttk.Button(root, text="📙-Open Image!-📖", command=scanImage)
    button.pack()

    root.mainloop()
