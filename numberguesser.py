import tkinter as tk
from tkinter import *
import random

win = Tk()
win.geometry("750x750")
win.title("SRS")
win.resizable(0, 0)

hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = IntVar()
hint.set("Guess a number between 1 to 50 ")
score.set(4)
final_score.set(score.get()+1)
num = random.randint(1,50)

def fun():
    x = guess.get()
    final_score.set(score.get())
    if score.get() > 0:
        if x > 50 or x < 0:
            hint.set("Your number is out of bound: You lost 1 chance!")
            score.set(score.get()-1)
            final_score.set(score.get()+1)

        elif num == x:
            hint.set("Congratulations YOU WON!!!")
            win.after(3000, lambda: win.destroy())

        elif x < num:
            hint.set("Your guess was low: Guess a higher number.")
            score.set(score.get()-1)
            final_score.set(score.get()+1)
        
        elif x > num:
            hint.set("Your guess was high: Guess a lower number.")
            score.set(score.get()-1)
            final_score.set(score.get()+1)

    else:
        hint.set("Game Over You LOST.")
        win.after(3000, lambda: win.destroy())

Entry(win, textvariable=guess, width=3, font=("Ubuntu", 50)).place(relx=0.5, rely=0.3, anchor=CENTER)
Entry(win, textvariable=hint, width= 50, font=("Courier", 15), bg="orange").place(relx=0.5, rely=0.7, anchor=CENTER)
Entry(win, text=final_score, width=2, font=("Ubuntu", 25)).place(relx=0.6, rely=0.8, anchor=CENTER)
Label(win, text="Guess the  number!", font=("Courier", 25)).place(relx=0.5, rely=0.1, anchor=CENTER)
Label(win, text="Score out of 5", font=("Courier", 25)).place(relx=0.3, rely=0.8, anchor=CENTER)
Button(win, text="CHECK", width=8, font=("Courier", 25), command=fun, bg="light blue").place(relx=0.5, rely=0.5, anchor=CENTER)
win.mainloop()
