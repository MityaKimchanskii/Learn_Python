from tkinter import *

window = Tk()
window.title("Convert Miles to Kilometers")
window.minsize(width=200, height=100)

def button_tapped():
    res = float(miles_input.get()) * 1.609
    calculated_label.config(text=res)

miles_input = Entry()
miles_input.grid(column=0, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=1, row=0)

kilometer_label = Label(text='Km')
kilometer_label.grid(column=1, row=2)

calculated_label = Label(text='0')
calculated_label.grid(column=0, row=2)

button = Button(text='Convert', command=button_tapped)
button.grid(column=0, row=3)

window.mainloop()
