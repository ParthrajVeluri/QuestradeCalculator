from gtts import gTTS
import pandas as pd
import os
from tkinter import *
from tkinter import filedialog
import pyttsx3


def calculateFigure(data, action):
    i = 0
    value = 0
    for x in data["Action"]:
        if(x == action):
            value += float(data["Total value"][i])
        i = i+1
    return round(value, 2)


def openFiles():
    filepath = filedialog.askopenfilename(
        filetypes=(("CSV Files", "*.csv"),))

    if(len(filepath) > 0):
        data = pd.read_csv(filepath, thousands=',')

        comission = 0
        for x in data["Commission"]:
            comission += x

        covPrice = calculateFigure(data, "COV")
        buyPrice = calculateFigure(data, "Buy")
        sellValue = calculateFigure(data, "Sell")
        shortValue = calculateFigure(data, "SHRT")

        profit = round((sellValue + shortValue) -
                       (buyPrice + covPrice + comission), 2)

        updatedText = "Total profit is " + str(profit) + \
            "$\n Cover Price = " + str(covPrice) + "$" + "\n Buy Price = " + str(buyPrice) + "$" + "\n Sell Value = " + str(
                sellValue) + "$" + "\n Short Value = " + str(shortValue) + "$" + "\n Commission = " + str(round(comission, 2)) + "$"
        out.config(text=updatedText)

        readOutLoud = "Total profit is " + str(profit) + "$"
        
        engine = pyttsx3.init()
        engine.say(readOutLoud)
        engine.runAndWait()


root = Tk()
root.title("Executions Calculator")
root.geometry("600x200")

welcomeMessage = Label(
    root, text="Welcome to the program, press browse to select a file to calculate!", font=("Calibri", 15))
welcomeMessage.pack()

out = Label(root, text="", font=("Calibri", 12))
out.pack()

browse = Button(root, text="Browse", command=openFiles)
browse.pack()

root.mainloop()
