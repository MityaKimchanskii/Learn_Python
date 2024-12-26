from tkinter import *
import time
import math

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


def start_timer():
    count_down(300)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, count_down, count - 1)

window = Tk()
window.title("Timer")
window.config(padx=20, pady=20, background='black')



title_label = Label(text="Timer", fg='white', background='black', font=('Ariel', 75))
title_label.grid(column=1, row=0)

canvas = Canvas(width=640, height=640, background='white', highlightthickness=0)
image_png = PhotoImage(file='batman.png')
canvas.create_image(320, 320, image=image_png)
timer_text = canvas.create_text(320, 210, text='00:00', fill='red', font=('Ariel', 75, 'bold'))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, fg='blue')
start_button.config(width=5, height=2, font=('Ariel', 15, 'bold'), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, fg='blue')
reset_button.config(width=5, height=2, font=('Ariel', 15, 'bold'))
reset_button.grid(column=3, row=2)

check_marks = Label(text='✔', fg='red', background='black', font=('Ariel', 30, 'bold'))
check_marks.grid(column=1, row=2)


window.mainloop()

