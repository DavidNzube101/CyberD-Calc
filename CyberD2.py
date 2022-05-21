# & "C:\Users\Juice David\AppData\Local\Programs\Python\Python39\python.exe" "c:\Users\Juice David\Documents\CyberD 2\CyberD 2.py"

'''
Dependencies for CyberD Calc 2 goes here!
'''
import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3 as snd
import math
from math import sqrt, pow
import PIL
from PIL import Image, ImageTk
import datetime
from datetime import date
import quadEqu
import linearExp
import superExp
import cubExp
import timeCon
import txtExtract
import os
import CYBcalculator as CYB
import CYBsearch as CYBs

engine = snd.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Date & Time Function
def timedate():
    Current_time = datetime.datetime.now().strftime('%I:%M %p')
    Current_date = date.today()

# BG function
def chngeBG(event):
    image = bgimage.resize((event.width, event.height), Image.ANTIALIAS)
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)

# Math Functions
def quadSolve():
    print(quadEqu.solve())

def linE():
    print(linearExp.solve())

def supE():
    print(superExp.solve())

def cubE():
    print(cubExp.solve())

def timeC():
    print(timeCon.solve())

def calcul():
    print(CYB.calculate())

def txtE():
    print(txtExtract.extract())

def ser():
    print(CYBs.search())

def allOnE():
    
    expRoot = tk.Tk()
    expRoot.title("Expansions")
    expRoot.iconbitmap("CYBIcon.ico")    

    intr = tk.Label(expRoot, text="Expansion Solver", font=("Helvetica 30 underline"), fg="red")
    intr.pack()

    introoL = tk.Label(expRoot, text="Choose what to solve", font=("Helvetica 15"), fg="red")
    introoL.pack()

    linEx = tk.Button(expRoot, text="Linear Expansion", font=("Calibri 20"), fg="blue", command=linE)
    linEx.pack()

    supEx = tk.Button(expRoot, text="Area Expansion", font=("Calibri 20"), fg="blue", command=supE)
    supEx.pack()

    cubEx = tk.Button(expRoot, text="Cubic Expansion", font=("Calibri 20"), fg="blue", command=cubE)
    cubEx.pack()

    expRoot.mainloop

def popup():

    messagebox.showinfo("Coming Soon...", "The Polynomial feature will be added in CyberD Calc 3. Thanks")
    
# Terminate Function
def close():
    global root
    root.destroy()

# Others
def App():
    password = passwordField.get()
    name = namebox.get()
    Sfile = open("LoginDetails.txt", "wb")
    Sfile.close()

    Sfile = open("LoginDetails.txt", "r+")
    name2 = Sfile.write("Name: " + name)
    space = Sfile.write("\n")
    pass1 = Sfile.write("PassCode: " + password)
    Sfile.close()

    guest = namebox.get()
    global root
    root.destroy()

    
    def mainApp():

        def chgBG(event):
            image = bgimage.resize((event.width, event.height), Image.ANTIALIAS)
            l.image = ImageTk.PhotoImage(image)
            l.config(image=l.image)

        root2 = tk.Tk()
        root2.geometry("1200x650")        
        root2.title("CyberD Calc 2")
        root2.iconbitmap("CYBIcon.ico")

        time = datetime.datetime.now().strftime('%I:%M %p')
        Currentdate = date.today()

        bgimage = Image.open("BG_PIC.jpg")
        l = tk.Label(root2)
        l.place(x=0, y=0, relwidth=1, relheight=1)
        l.bind('<Configure>', chgBG)
        
        engine.say("Welcome, " + guest + ", good day, What do you want to do today ?")
        engine.runAndWait()

        welcome = tk.Label(root2, text="Welcome, ", font=("Albertus 20 bold"), fg="blue")
        welcome.pack()

        namewel = tk.Label(root2, text=guest, font=("Albertus 20 bold"), fg="blue")
        namewel.pack()

        pickLabel = tk.Label(root2, text="What do you want to do today ?", font=("Albertus 25 bold"), fg="green")
        pickLabel.place(x=400, y=100)

        time = tk.Label(root2, text=time, font=("Calibri 20 bold"), fg="black")
        time.place(x=50, y=50)

        dateC = tk.Label(root2, text=Currentdate, font=("Calibri 20 bold"), fg="black")
        dateC.place(x=40, y=90)

        CALCLabel = tk.Button(root2, text="Calculator", font=("Bahnschrift 20"), fg="blue", command=calcul)
        CALCLabel.place(x=400, y=150)

        quadEquLabel = tk.Button(root2, text="Quadratic Equations", font=("Bahnschrift 20"), fg="blue", command=quadSolve)
        quadEquLabel.place(x=400, y=200)

        allOnEx = tk.Button(root2, text="🧮 All on Expansion", font=("Bahnschrift 20"), fg="blue", command=allOnE)
        allOnEx.place(x=400, y=250)

        TimeCo = tk.Button(root2, text="🕒 Time", font=("Bahnschrift 20"), fg="blue", command=timeC)
        TimeCo.place(x=400, y=300)

        textE = tk.Button(root2, text="📑 Extract Text", font=("Bahnschrift 20"), fg="blue", command=txtE)
        textE.place(x=400, y=350)

        serE = tk.Button(root2, text="CyberD LookUp", font=("Bahnschrift 20"), fg="blue", command=ser)
        serE.place(x=400, y=400)

        polyN = tk.Button(root2, text="Polynomials", font=("Bahnschrift 20"), fg="blue", command=popup)
        polyN.place(x=400, y=450)

        root2.mainloop()

    
    mainApp()




root = tk.Tk()
root.geometry("1000x500")
root.title("CyberD 2 Login Page")
root.iconbitmap("CYBIcon.ico")


# Menu
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="Skip Sign in", command=App)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

bgimage = Image.open('Login_Pic.jpg')
l = tk.Label(root)
l.place(x=0, y=0, relwidth=1, relheight=1)
l.bind('<Configure>', chngeBG)


lgScr = tk.PhotoImage(file="LoginScr2.gif")
lgScrLabel = tk.Label(root, image=lgScr)
lgScrLabel.image = lgScr
lgScrLabel.pack()

NameLael = tk.Label(root, text="Name", fg="Red", font=("Calibri 20 bold"))
NameLael.pack()
namebox = ttk.Entry(root, width=45)
namebox.pack()
nameboxG = namebox.get()


PassLael = tk.Label(root, text="CalcKey", fg="Red", font=("Calibri 20 bold"))
PassLael.pack()
passwordField = ttk.Entry(root, show="⚫", width=45)
passwordField.pack()
passFG = passwordField.get()


button = ttk.Button(root, text="Sign in", command=App)
button.pack()



root.mainloop()