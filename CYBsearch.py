import tkinter as tk
import wikipedia as wiki
from tkinter import ttk
import pyttsx3 as voice
from PIL import Image, ImageTk

engine = voice.init()

def search():
    def chgBG(event):
        image = bgimage.resize((event.width, event.height), Image.ANTIALIAS)
        l.image = ImageTk.PhotoImage(image)
        l.config(image=l.image)


    def search():
        word = userentry.get()
        result = wiki.summary(word, 1)

        resultLabal = tk.Label(root, text=result, font=("Albertus 15 italic"))
        resultLabal.pack()
        def speak():
            engine.say(result)

        speak(result)    

    root = tk.Tk()
    root.geometry("500x250")
    root.title("CyberD Calc LookUp")
    root.iconbitmap("CYBIcon.ico")

    bgimage = Image.open("BG_PIC.jpg")
    l = tk.Label(root)
    l.place(x=0, y=0, relwidth=1, relheight=1)
    l.bind('<Configure>', chgBG)

    label = tk.Label(root, text="CyberD Calc LookUp", font=("Calibri 40"), fg="purple")
    label.pack()

    label2 = tk.Label(root, text="Make sure to have active Internet Connection, before Searching", font=("Calibri 10"), fg="red")
    label2.pack()

    userentry = ttk.Entry(root, width=50)
    userentry.pack()
    print(userentry.get)

    button = ttk.Button(root, text="Look up", width=25, command=search)
    button.pack()

    root.mainloop()
