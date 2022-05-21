import math
import tkinter as tk
from typing import final
import pyttsx3
from tkinter import ttk 

engine = pyttsx3.init()
def solve():
    def solveLexP():
        temp = float(tempInput.get())
        initialLength = float(l1Input.get())
        finalLength = float(l2Input.get())
        numeratorPt = finalLength - initialLength
        demoninatorPt = initialLength * temp
        LinearExp = numeratorPt / demoninatorPt
        LinearExpAppr = math.ceil(LinearExp)

        lexPlabel = tk.Label(root, text="The Linear Expansion would be equal to: ", fg="green")
        lexPlabel.pack()

        lexP = tk.Label(root, text=LinearExp, fg="green")
        lexP.pack()

        engine.say("The Linear Expansion would be equal to: ")
        engine.say(LinearExp)
        engine.runAndWait()

        # Approximate Value
        lexPlabelAppr = tk.Label(root, text="The Linear Expansion would be approximately equal to: ", fg="green")
        lexPlabelAppr.pack()

        lexPAppr = tk.Label(root, text=LinearExpAppr, fg="green")
        lexPAppr.pack()

        engine.say("The Linear Expansion would be approximately equal to: ")
        engine.say(LinearExpAppr)
        engine.runAndWait()

        # Dash Value
        lexpDash = tk.Label(root, text="-----------------Thank You-------------------")
        lexpDash.pack()


    root = tk.Tk()
    root.title("Linear Expansion Solver")
    root.iconbitmap("c:/users/juice david/documents/terry/emotions/terry.ico")

    canvas = tk.Canvas(root, height=50, width=100)
    canvas.pack()

    introtext = tk.Label(root, text="Linear Expansion Solver", font=("Harrington 20 bold"))
    introtext.pack()

    labelGetTemp = tk.Label(root, text="Your Temperature: ", fg="blue")
    labelGetTemp.pack()

    tempInput = ttk.Entry(root)
    tempInput.pack()
    print(tempInput.get())

    labelGetL1 = tk.Label(root, text="Your Initial Length: ", fg="blue")
    labelGetL1.pack()

    l1Input = ttk.Entry(root)
    l1Input.pack()
    print(l1Input.get())

    labelGetL2 = tk.Label(root, text="Your Final Length: ", fg="blue")
    labelGetL2.pack()

    l2Input = ttk.Entry(root)
    l2Input.pack()
    print(l2Input.get())

    solveButton = ttk.Button(root, text="Solve", command=solveLexP)
    solveButton.pack()

    root.mainloop()