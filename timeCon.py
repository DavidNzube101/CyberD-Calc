import tkinter as tk
from tkinter import ttk

def solve():
    
    def solveTime():
        if 'sec' in valueEntry.get():
            valE = valueEntry.get()
            realVal = valE.replace('sec', '')
            valSec = int(realVal)
            minConst = 60
            hrConst = 360
            convToMin = valSec / minConst
            convToHr = valSec / hrConst

            minLabel1 = tk.Label(root, text="Value in Minutes: ", fg="green")
            minLabel1.pack()

            minValLabel = tk.Label(root, text=convToMin, fg="green")
            minValLabel.pack()

            hrLabel = tk.Label(root, text="Value in Hours: ", fg="green")
            hrLabel.pack()

            hrValLabel = tk.Label(root, text=convToHr, fg="green")
            hrValLabel.pack()
            dashX = tk.Label(root, text="-----------------------------Done!-----------------------------", fg="green")
            dashX.pack()
        elif 'hr' in valueEntry.get():
            valE3 = valueEntry.get()
            realVal3 = valE3.replace('hr', '')
            valHr = int(realVal3)
            minConst3 = 60
            secConst = 3600
            convToMin3 = valHr * minConst3
            convTosec = valHr * secConst

            minLabel3 = tk.Label(root, text="Value in Minutes: ", fg="green")
            minLabel3.pack()

            minValLabe3 = tk.Label(root, text=convToMin3, fg="green")
            minValLabe3.pack()

            secLabel = tk.Label(root, text="Value in Seconds: ", fg="green")
            secLabel.pack()

            secValLabel3 = tk.Label(root, text=convTosec, fg="green")
            secValLabel3.pack()
            dashX = tk.Label(root, text="-----------------------------Done!-----------------------------", fg="green")
            dashX.pack()
        elif 'min' in valueEntry.get():
            valE5 = valueEntry.get()
            realVal5 = valE5.replace('min', '')
            valMin = int(realVal5)
            secConst = 60
            hrConst = 0.016667
            convToHr4 = valMin * hrConst
            convTosec2 = valMin * secConst

            hrLabel5 = tk.Label(root, text="Value in Hours: ", fg="green")
            hrLabel5.pack()

            hrValLabe5 = tk.Label(root, text=convToHr4, fg="green")
            hrValLabe5.pack()

            secLabel2 = tk.Label(root, text="Value in Seconds: ", fg="green")
            secLabel2.pack()

            secValLabel4 = tk.Label(root, text=convTosec2, fg="green")
            secValLabel4.pack()
            dashX = tk.Label(root, text="-----------------------------Done!-----------------------------", fg="green")
            dashX.pack()
        elif 'days' in valueEntry.get():
            DvalE5 = valueEntry.get()
            DrealVal5 = DvalE5.replace('days', '')
            DvalMin = int(DrealVal5)
            secConst = 86400
            hrConstD = 24
            minConstD = 1440
            convToHr4 = DvalMin * hrConstD
            convTosec2 = DvalMin * secConst
            convToMinD = DvalMin * minConstD

            hrLabel5 = tk.Label(root, text="Value in Hours: ", fg="green")
            hrLabel5.pack()

            hrValLabe5 = tk.Label(root, text=convToHr4, fg="green")
            hrValLabe5.pack()

            secLabel2 = tk.Label(root, text="Value in Seconds: ", fg="green")
            secLabel2.pack()

            secValLabel4 = tk.Label(root, text=convTosec2, fg="green")
            secValLabel4.pack()

            MinValLabel2 = tk.Label(root, text="Value in Minutes", fg="green")
            MinValLabel2.pack()

            MinValLabel4 = tk.Label(root, text=convToMinD, fg="green")
            MinValLabel4.pack()
            
            dashX = tk.Label(root, text="-----------------------------Done!-----------------------------", fg="green")
            dashX.pack()
        elif 'wks' in valueEntry.get():
            WDvalE5 = valueEntry.get()
            WDrealVal5 = WDvalE5.replace('wks', '')
            WDvalMin = int(WDrealVal5)
            secConst = 604800
            hrConst = 168
            minConstD = 10080
            dayConst = 7
            convToHr4 = WDvalMin * hrConst
            convTosec2 = WDvalMin * secConst
            convToMinD = WDvalMin * minConstD
            convToDay = WDvalMin * dayConst

            hrLabel5 = tk.Label(root, text="Value in Hours: ", fg="green")
            hrLabel5.pack()

            hrValLabe5 = tk.Label(root, text=convToHr4, fg="green")
            hrValLabe5.pack()

            secLabel2 = tk.Label(root, text="Value in Seconds: ", fg="green")
            secLabel2.pack()

            secValLabel4 = tk.Label(root, text=convTosec2, fg="green")
            secValLabel4.pack()

            MinValLabel2 = tk.Label(root, text="Value in Minutes", fg="green")
            MinValLabel2.pack()

            MinValLabel4 = tk.Label(root, text=convToMinD, fg="green")
            MinValLabel4.pack()

            DayValLabel2 = tk.Label(root, text="Value in Days", fg="green")
            DayValLabel2.pack()

            Day2ValLabel4 = tk.Label(root, text=convToDay, fg="green")
            Day2ValLabel4.pack()
            
            dashX = tk.Label(root, text="-----------------------------Done!-----------------------------", fg="green")
            dashX.pack()
        else:
            dashX = tk.Label(root, text="----------------------------------------------------------------", fg="red")
            dashX.pack()
            errorLabel = tk.Label(root, text="Not a time measurement!", fg="red")
            errorLabel.pack()
            dashX = tk.Label(root, text="----------------------------------------------------------------", fg="red")
            dashX.pack()

    root = tk.Tk()
    root.title("Time Converter")
    root.iconbitmap("CYBIcon.ico")

    canvas = tk.Canvas(root, height=50, width=100)   
    canvas.pack()

    introText = ttk.Label(root, text="Time Converter", font="gabriola 32 bold", foreground="indigo")
    introText.pack()

    # Note
    noteOne = tk.Label(root, text="To convert seconds to minutes or hour, use the s-e-c keyword. After writing your number, write s-e-c after your number then tap the go button.", fg="purple")
    noteOne.pack()

    noteTwo = tk.Label(root, text="To convert minutes to seconds or hour, use the m-i-n keyword. After writing your number, write m-i-n after your number then tap the go button.", fg="purple")
    noteTwo.pack()

    noteThree = tk.Label(root, text="To convert hour to minutes or seconds, use the h-r keyword. After writing your number, write h-r after your number then tap the go button.", fg="purple")
    noteThree.pack()

    noteFour = tk.Label(root, text="To convert day to hour, minutes or seconds, use the d-a-y-s keyword. After writing your number, write d-a-y-s after your number then tap the go button.", fg="purple")
    noteFour.pack()

    noteFive = tk.Label(root, text="To convert Week to hour, day, minutes or seconds, use the w-k-s keyword. After writing your number, write w-k-s after your number then tap the go button.", fg="purple")
    noteFive.pack()


    # Seconds Label
    secLabel = ttk.Label(root, text="Value: ", font="helevitica", foreground="blue")
    secLabel.pack()

    valueEntry = ttk.Entry(root)
    valueEntry.pack()
    print(valueEntry.get())

    button = ttk.Button(root, text="Go!", command=solveTime)
    button.pack()

    root.mainloop()