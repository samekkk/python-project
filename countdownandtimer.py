#Importing the required libraries and Modules
#Creating the GUI window (Labels, Button and Entry Field)
#Displaying the current time
#Creating the Timer and Countdown Function
#Adding Desktop Notification
#Adding a Beep Sound

import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from win10toast import ToastNotifier
import winsound

#creating a window
window = Tk()
window.geometry("600x600")
window.title("SRS")
window.resizable(0, 0)
Label(window, text="Clock and timer", font=('Calibri 15')).pack(pady=20)

#to print current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window, text=current_time).pack()

check = tk.BooleanVar()
hour = tk.IntVar()
minute = tk.IntVar()
second = tk.IntVar()

def countdown():
    h = hour.get()
    m = minute.get()
    s = second.get()
    t = h * 3600 + m * 60 + s
    while t:
        mins, secs = divmod(t, 60)
        display = ("{:02d}:{:02d}".format(mins, secs))
        time.sleep(1) 
        t -= 1
        Label(window, text= display).pack()
    
    if (check.get() == True):
        winsound.Beep(1000, 3000)
    
    Label(window, text="Time-Up", font=("bold", 20)).place(x=250, y=440)

    #display notification on desktop
    toast = ToastNotifier()
    toast.show_toast("Notification", "Timer is Off", duration = 20, threaded=True)

Label(window, text="Enter time in HH:MM:SS", font="bold").pack()
Entry(window, textvariable=hour, width= 30).pack()
Entry(window, textvariable=minute, width= 30).pack()
Entry(window, textvariable=second, width= 30).pack()
Checkbutton(window, text="Music", onvalue=True, variable=check).pack()
Button(window, text="Set Countdown", command= countdown, bg="green").pack()


window.update()
window.mainloop()

