import math
import tkinter as tk
from typing import final
import pyttsx3
from tkinter import ttk

engine = pyttsx3.init()

def solve():
    def solveAexP():
        temp = float(tempInput.get())
        initialArea = float(a1Input.get())
        finalArea = float(a2Input.get())
        numeratorPt = finalArea - initialArea
        demoninatorPt = initialArea * temp
        AreaExp = numeratorPt / demoninatorPt
        AreaExpAppr = math.ceil(AreaExp)

        AexPlabel = tk.Label(root, text="The Area Expansion would be equal to: ", fg="green")
        AexPlabel.pack()

        AexP = tk.Label(root, text=AreaExp, fg="green")
        AexP.pack()

        engine.say("The Area Expansion would be equal to: ")
        engine.say(AreaExp)
        engine.runAndWait()

        # Approximate Value
        AexPlabelAppr = tk.Label(root, text="The Area Expansion would be approximately equal to: ", fg="green")
        AexPlabelAppr.pack()

        AexPAppr = tk.Label(root, text=AreaExpAppr, fg="green")
        AexPAppr.pack()

        engine.say("The Area Expansion would be approximately equal to: ")
        engine.say(AreaExpAppr)
        engine.runAndWait()

        # Dash Value
        AexPDash = tk.Label(root, text="-----------------Thank You-------------------")
        AexPDash.pack()


    root = tk.Tk()
    root.title("Area Expansion Solver")
    root.iconbitmap("CYBIcon.ico")

    canvas = tk.Canvas(root, height=50, width=100)
    canvas.pack()

    introtext = tk.Label(root, text="Area Expansion Solver", font=("Harrington 20 bold"))
    introtext.pack()

    labelGetTemp = tk.Label(root, text="Your Temperature: ", fg="blue")
    labelGetTemp.pack()

    tempInput = ttk.Entry(root)
    tempInput.pack()
    print(tempInput.get())

    labelGetL1 = tk.Label(root, text="Your Initial Area: ", fg="blue")
    labelGetL1.pack()

    a1Input = ttk.Entry(root)
    a1Input.pack()
    print(a1Input.get())

    labelGetL2 = tk.Label(root, text="Your Final Area: ", fg="blue")
    labelGetL2.pack()

    a2Input = ttk.Entry(root)
    a2Input.pack()
    print(a2Input.get())

    solveButton = ttk.Button(root, text="Solve", command=solveAexP)
    solveButton.pack()

    root.mainloop()