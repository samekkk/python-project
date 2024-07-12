import random
from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("350x300")
win.title("SRS")
win.resizable(0, 0)

character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,-./:;<=>?@[\]^_`{|}~"

def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except:
        messagebox.showerror(message="Please key in the required inputs")
        return 
    
    #Check if user has allowed repitition
    if repeat == 1:
        password = random.sample(character_string, k=length)

    else:
        password = random.choices(character_string, k=length)

    #Since the returned value is a list, we convert to a sting using join
    
    password = ''.join(password)
    password_v.set(password)
    

def clipper():
    win.clipboard_clear()
    win.clipboard_append(password_v.get())
    messagebox.showinfo("Clipboard", "Password copied to clipboard!")

password_v = StringVar()
title_label = Label(win, text="Password Generator", font=("Ubuntu Mono", 12))
title_label.pack(pady = 10)

length_label = Label(win, text="Enter length of the password: ")
length_label.place(x=20, y=40)
length_entry = Entry(win, width=3)
length_entry.place(x= 200, y = 40)

repeat_label = Label(win, text="Repetition? 1: no repetition, 2: otherwise: ")
repeat_label.place(x=20,y=80)
repeat_entry = Entry(win, width=3)
repeat_entry.place(x = 260, y = 80)

password_button = Button(win, text="Generate Password", command=generate_password)
password_button.place(x=30, y=120)

clipboard_button = Button(win, text="Copy to Clipboard", command=clipper)
clipboard_button.place(x=200, y=120)

password_display = Entry(win, textvariable=password_v, font=("Hevetica", 20), bd=0, bg="gray", state="readonly" )
password_display.place(x=30, y=180)

win.mainloop()
