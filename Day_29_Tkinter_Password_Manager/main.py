from tkinter import *
from tkinter import messagebox

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website.strip() == '' or password.strip() == '':
        messagebox.showerror(title='Error', message='Website and Password cannot be empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'The details entered: \nEmail: {email} '
                                                        f'\nPassword: {password} \nSave?')
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=300, width=300)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string='hello@email.com')
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Button
password_button = Button(text='Generate Password')
password_button.grid(row=3, column=2)
add_button = Button(text='Add', width=48, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()