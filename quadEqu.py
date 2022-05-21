import math
import tkinter as tk
from tkinter import font
import pyttsx3

engine = pyttsx3.init()


def solve():
    def solveQuad():
        aD = int(quadInputOne.get())
        bD = int(quadInputTwo.get())
        cD = int(quadInputThree.get())
        bDSquare = int(math.pow(bD, 2))
        realBDSquare = bDSquare
        fourADCD = int(4 * aD * cD)
        realFourADCD = fourADCD
        discriminant = realBDSquare - realFourADCD

        if discriminant > 0 & discriminant == 0:
    
            a = float(quadInputOne.get())
            b = float(quadInputTwo.get())
            c = float(quadInputThree.get())
            minusB = -b
            bSquare = math.pow(b, 2)
            fourAC = 4 * a * c
            twoA = 2 * a
            bSquareSubtFAC = bSquare - fourAC
            sqrtOfbSquareSubtFAC = math.sqrt(bSquareSubtFAC)
            x1Plus = minusB + sqrtOfbSquareSubtFAC
            x1 = x1Plus / twoA
            x1Subt = minusB - sqrtOfbSquareSubtFAC
            x2 = x1Subt / twoA
            x1F = math.ceil(x1)
            x2F = math.ceil(x2)
            print("Your roots are: ")
            print(x1)
            print(x2)
            print(x1F)
            print(x2F)
            # x1 ans
            xoneLabel = tk.Label(root, text="Your x1 is: ")
            xoneLabel.pack()

            xoneLabel2 = tk.Label(root, text=x1, fg="green")
            xoneLabel2.pack()

            xoneLabelRound = tk.Label(root, text="Your x1 approximatedly is: ")
            xoneLabelRound.pack()

            xoneLabel2Round = tk.Label(root, text=x1F, fg="green")
            xoneLabel2Round.pack()

            # x2 ans 
            xtwoLabel = tk.Label(root, text="Your x2 is:- ")
            xtwoLabel.pack()

            xtwoLabel2 = tk.Label(root, text=x2, fg="green")
            xtwoLabel2.pack()

            xtwoLabelRound = tk.Label(root, text="Your x2 approximatedly is:- ")
            xtwoLabelRound.pack()

            xtwoLabel2Round = tk.Label(root, text=x2F, fg="green")
            xtwoLabel2Round.pack()

            xdash = tk.Label(root, text="----------------------Thank You!-------------------------", fg="green")
            xdash.pack()
            
        else:
            xdash2 = tk.Label(root, text="---------------------------------------------------------", fg="red")
            xdash2.pack()
            error2Label = tk.Label(root, text="Your Quadratic Equation roots will be that of a\n'IMAGINARY ROOTS'", fg="red")
            error2Label.pack()
            xdash3 = tk.Label(root, text="---------------------------------------------------------", fg="red")
            xdash3.pack()

    root = tk.Tk()
    root.title("Quadratic Equation Solver")
    root.iconbitmap("CYBIcon.ico")

    canvas = tk.Canvas(root, height=50, width=100)
    canvas.pack()

    floatrotext = tk.Label(root, text="Quadratic Equation Solver", font=("Gabriola 30"),  fg="purple")
    floatrotext.pack()


    labelQuadOne = tk.Label(root, text="Your a:", fg="red")
    labelQuadOne.pack()
    # ax2 + bx + c = 0 (A)
    quadInputOne = tk.Entry(root)
    quadInputOne.pack()
    print(quadInputOne.get())

    labelQuadTwo = tk.Label(root, text="Your b:", fg="blue")
    labelQuadTwo.pack()
    # ax2 + bx + c = 0 (B)
    quadInputTwo = tk.Entry(root)
    quadInputTwo.pack()
    print(quadInputTwo.get())

    labelQuadThree = tk.Label(root, text="Your c:", fg="green")
    labelQuadThree.pack()
    # ax2 + bx + c = 0 (C)
    quadInputThree = tk.Entry(root)
    quadInputThree.pack()
    print(quadInputThree.get())


    button = tk.Button(root, text="Go!", command=solveQuad)
    button.pack()

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack( side = tk.RIGHT, fill=tk.Y )
    scrollbar.config()


    root.mainloop()