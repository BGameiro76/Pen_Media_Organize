#!/usr/bin/env python3
"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro)
More in 
  SoloLearn: https://www.sololearn.com/Profile/8198571
  GitHub: https://github.com/BGameiro76
  Repl.it: https://repl.it/@B_Gameiro

GUI in Python 3
Using Tkinter
"""

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
import os, re

Path = r"path to app form C://"

# Create instance
window = tk.Tk()

#======================
# title
#======================
# Title of the window    
window.title("Media Organization GUI")

#======================
# label
#======================
# Label to media
ttk.Label(window, text="Which media would you like to access?").grid(row=0)

#======================
# radio buttons
#======================
# Radiobutton global variables (list)
Apps = ["Name displayed", "Música", "Fotos"]
Paths = ["Path to the app", "C:\\Program Files (x86)\\MAGIX\\MP3 deluxe 19\\MP3deluxe.exe", "F:\\VLC\\vlc.exe"]
#rPaths = [re.compile(p) for p in Paths]
rPaths = ["Path to the app", r"C:\\Program Files (x86)\\MAGIX\\MP3 deluxe 19\\MP3deluxe.exe", r"F:\\VLC\\vlc.exe"]
AppsPath = dict(zip(Apps, rPaths))

#
thisApp = 0
def runApp(radioVariable):
    thisApp = AppsPath[Apps[radioVariable]]
    print(thisApp)
    return(thisApp)

# create three Radiobuttons using one variable
radioVariable = tk.IntVar()

# Selecting a non-existing index value for radioVariable
radioVariable.set(0)

# Creating all Radiobutton widgets within one loop
for ap in range(1, len(Apps)):
    curRad = tk.Radiobutton(window, text=Apps[ap], variable=radioVariable, value=ap, command=runApp)
    curRad.grid(column=ap, row=1, sticky=tk.E)

#======================
# go button
#======================
# Button Click Event Function
def click_me():
    os.startfile(thisApp, "open")

# Button
action = ttk.Button(window, text="Go!", command=click_me)
action.grid(column=4, row=1, sticky=tk.E)
while radioVariable == 0:
    action.configure(state="disabled")

#======================
# Start GUI
#======================
window.mainloop()
