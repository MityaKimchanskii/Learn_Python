import tkinter

window = tkinter.Tk()
window.title('GUI Program')
window.minsize(width=500, height=500)

label1 = tkinter.Label(text='Label', font=('Times New Roman', 25, 'bold'))
label1.pack()
label1.config(text='hello')

def button_tapped():
    print('Button tapped')
    label1.config(text=input.get())

button = tkinter.Button(text='Button', command=button_tapped)
button.place(x=200, y=250)

input = tkinter.Entry(width=20)
input.pack()


window.mainloop()