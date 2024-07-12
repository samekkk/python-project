from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("720x550")
root.title("SRS")
root.config(bg="#aee4e8")
root.resizable(0, 0)

contactlist = [
    ['Ram','369854712'],
    ['Shyam', '521155222'],
    ['Hari', '78945614'],
    ['SRS', '58745246'],
    ['Sam', '5846975'],
]

name = StringVar()
number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman',16), bg="#f0fffc", width=20, height=20, borderwidth=2)

scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=RIGHT, fill=BOTH, expand=1)

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)
Select_set()

def Selected():
    print("Hello", len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please select the name.")

    else:
        return int(select.curselection()[0])

def AddContact():
    if name.get() != "" and number.get() != "":
        contactlist.append([name.get(), number.get()])
        print(contactlist)
        Select_set()
        Clear()
    
    else:
        messagebox.showerror("Error", "Please fill in the complete information")

def Edit():
    if name.get() and number.get():
        contactlist[Selected()] = [name.get(), number.get()]

        messagebox.showinfo("Message", "Successfully updated contact")
        Select_set()
        Clear()

    elif not (name.get()) and not (number.get()) and (len(select.curselection())) != 0:
        messagebox.showerror("Error", "Please fill in the information")

    else:
        if len(select.curselection())==0:
            messagebox.showerror("Error", "Please Select the Name")

def Delete():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno("Confirmation", "Do you want to delete this contact?")

        if result == True:
            del contactlist[Selected()]
            Select_set()
    
    else:
        messagebox.showerror("Error", "Please Select a contact")

def View():
    NAME, NUMBER = contactlist[Selected()]
    name.set(NAME)
    number.set(NUMBER)

def Clear():
    name.set("")
    number.set("")

def Exit():
    root.destroy()

Label(root, text="Name", font=("Times new roman",25,"bold"), bg="SlateGray3").place(x = 30, y = 20)
Entry(root, textvariable= name, font=("Times new roman",15), width=15).place(x = 200, y = 30)

Label(root, text="Contact no.", font=("Times new roman", 22, "bold"), bg="SlateGray3").place(x = 30, y = 75)
Entry(root, textvariable= number, font=("Times new roman", 15), width=15).place(x = 200, y = 85)

Button(root, text="ADD", font="Helvetica 18 bold", bg="#e8c1c7", command=AddContact, width=8).place(x=50, y=170)
Button(root, text="EDIT", font="Helvetica 18 bold", bg="#e8c1c7", command=Edit, width=8).place(x=50, y=270)
Button(root,text="DELETE", font='Helvetica 18 bold',bg='#e8c1c7',command = Delete, width=8).place(x= 270, y=170)
Button(root,text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command = View, width=8).place(x= 50, y=370)
Button(root,text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command = Clear,width=8).place(x= 270, y=270)
Button(root,text="EXIT", font='Helvetica 18 bold', bg='tomato', command = Exit, width=8).place(x= 270, y=370)
root.mainloop()