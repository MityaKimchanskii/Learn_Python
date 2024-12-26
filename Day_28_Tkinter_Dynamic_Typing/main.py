from tkinter import *
import time
import math

WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
REPS = 0
TIMER: None = None


def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global  REPS
    REPS += 1

    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg="green")
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg="lightgreen")
    else:
        count_down(work_sec)
        title_label.config(text="Time to Work")

def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(REPS/2)):
            mark += '✔'
        check_marks.config(text=mark)

def reset_timer():
    global TIMER
    title_label.config(text='Timer')
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')
    global REPS
    REPS = 0


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
reset_button.config(width=5, height=2, font=('Ariel', 15, 'bold'), command=reset_timer)
reset_button.grid(column=3, row=2)

check_marks = Label(fg='red', background='black', font=('Ariel', 30, 'bold'))
check_marks.grid(column=1, row=2)


window.mainloop()

