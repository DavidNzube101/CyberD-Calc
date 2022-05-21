import math
import tkinter as tk
from typing import final
import pyttsx3
from tkinter import ttk

engine = pyttsx3.init()


def solve():
    def solveCexP():
        temp = float(tempInput.get())
        initialVolume = float(c1Input.get())
        finalVolume = float(c2Input.get())
        numeratorPt = finalVolume - initialVolume
        demoninatorPt = initialVolume * temp
        CubicExp = numeratorPt / demoninatorPt
        CubicExpAppr = math.ceil(CubicExp)

        CexPlabel = tk.Label(root, text="The Cubic Expansion would be equal to: ", fg="green")
        CexPlabel.pack()

        CexP = tk.Label(root, text=CubicExp, fg="green")
        CexP.pack()

        engine.say("The Cubic Expansion would be equal to: ")
        engine.say(CubicExp)
        engine.runAndWait()

        # Approximate Value
        CexPlabelAppr = tk.Label(root, text="The Cubic Expansion would be approximately equal to: ", fg="green")
        CexPlabelAppr.pack()

        CexPAppr = tk.Label(root, text=CubicExpAppr, fg="green")
        CexPAppr.pack()

        engine.say("The Cubic Expansion would be approximately equal to: ")
        engine.say(CubicExpAppr)
        engine.runAndWait()

        # Dash Value
        CexPDash = tk.Label(root, text="-----------------Thank You-------------------")
        CexPDash.pack()


    root = tk.Tk()
    root.title("Cubic Expansion Solver")
    root.iconbitmap("CYBIcon.ico")


    canvas = tk.Canvas(root, height=50, width=100)
    canvas.pack()

    introtext = tk.Label(root, text="Cubic Expansion Solver", font=("Harrington 20 bold"))
    introtext.pack()

    labelGetTemp = tk.Label(root, text="Your Temperature: ", fg="blue")
    labelGetTemp.pack()

    tempInput = ttk.Entry(root)
    tempInput.pack()
    print(tempInput.get())

    labelGetL1 = tk.Label(root, text="Your Initial Volume: ", fg="blue")
    labelGetL1.pack()

    c1Input = ttk.Entry(root)
    c1Input.pack()
    print(c1Input.get())

    labelGetL2 = tk.Label(root, text="Your Final Volume: ", fg="blue")
    labelGetL2.pack()

    c2Input = ttk.Entry(root)
    c2Input.pack()
    print(c2Input.get())

    solveButton = ttk.Button(root, text="Solve", command=solveCexP)
    solveButton.pack()

    root.mainloop()