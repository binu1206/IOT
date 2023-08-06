import time

print("Python UI")

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.attributes('-fullscreen', False)
window.title("IOT Project")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)


labelAMONIAValue = tk.Label(text="5.12",
                                    fg="#33CC33",
                                    justify=CENTER,
                                    font="TimesNewRoman 60 bold")

labelAMONIAValue.place(x=0, y=200, width=screen_width / 3, height=100)
labelAMONIA = tk.Label(text="LAMONIA",
                                    fg="#FF9999",
                                    justify=CENTER,
                                    font="Helvetica 60 bold")
labelAMONIA.place(x=0, y=100, width=screen_width / 3, height=100)


labelTDSValue = tk.Label(text="20",
                                 fg="#CC0000",
                                 justify=CENTER,
                                 # bg = "#333",
                                 font="Helvetica 60 bold")

labelTDSValue.place(x=screen_width / 3, y=200, width=screen_width / 3, height=100)

labelTDS = tk.Label(text="TDS",
                                 fg="#EE00EE",
                                 justify=CENTER,
                                 # bg = "#333",
                                 font="Helvetica 60 bold")
labelTDS.place(x=screen_width / 3, y=100, width=screen_width / 3, height=100)



labelPHValue = tk.Label(text="7.11",
                                fg="#0000ff",
                                justify=CENTER,
                                font="Helvetica 60 bold")

labelPHValue.place(x=2 * screen_width / 3, y=200, width=screen_width / 3, height=100)
labelPH = tk.Label(text="PH",
                                fg="#008080",
                                justify=CENTER,
                                font="Helvetica 60 bold")
labelPH.place(x=2 * screen_width / 3, y=100, width=screen_width / 3, height=100)

buttonOn = tk.Button(text="ON",
                                    fg="#33CC33",
                                    justify=CENTER,
                                    font="Helvetica 60 bold")

buttonOn.place(x=400, y=500, width=300, height=100)
buttonOff = tk.Button(text="OFF",
                                    fg="#33CC33",
                                    justify=CENTER,
                                    font="Helvetica 60 bold")

buttonOff.place(x=screen_width / 2, y=500, width=300, height=100)
# def Simpletoggle():
#     if toggle_button.config('text')[-1] == 'ON':
#         toggle_button.config(text='OFF')
#     else:
#         toggle_button.config(text='ON')

# def nut_nhan1():
#  print("Bat")
#
# def nut_nhan2():
#  print("Tat")
#
#
# buttonOn.config(command=nut_nhan1)
# buttonOff.config(command=nut_nhan2)

# while True:
#     window.update()
#     time.sleep(0.1)
