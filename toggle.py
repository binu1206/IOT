from tkinter import *


def Simpletoggle():
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
    else:
        toggle_button.config(text='ON')


ws = Tk()
ws.title("Python Guides")
ws.geometry("200x100")

toggle_button = Button(text="OFF", width=10, command=Simpletoggle)
toggle_button.pack(pady=10)

ws.mainloop()