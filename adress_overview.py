#imports

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

#screen build

screen = Tk()
screen.geometry("600x600")
screen.title("my adress book")
screen.config(background = "gray")

#defs

myAddressBook = {}

def add_data ():

    key = entry1.get()

    if key not in myAddressBook.keys():
        
        entry_main.insert(END, key)

    myAddressBook[key] = (key, entry2.get(), entry3.get(), entry4.get(), entry5.get())
    clear()
    
def clear ():

    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)

def edit_data ():

    clear() 
    data = entry_main.curselection()
    if data: 

        entry1.insert(0,entry_main.get(data))
        details = myAddressBook[entry1.get()]
        entry2.insert(0,details[1])
        entry3.insert(0,details[2])
        entry4.insert(0,details[3])
        entry5.insert(0,details[4])

def delete_data ():
    data = entry_main.curselection()
    if data:

        del myAddressBook[entry_main.get(data)]
        entry_main.delete(data)
        clear()

def save_data ():
    file = asksaveasfile(defaultextension = ".txt")
    if file:
        print(myAddressBook,file = file)
        clear()
        myAddressBook.clear()
        entry_main.delete(0,END)

def open_file ():
    global myAddressBook

    clear()
    myAddressBook.clear()
    entry_main.delete(0,END)
    file = askopenfile()
    if file:
        myAddressBook  = eval(file.read())
        for key in myAddressBook:
            entry_main.insert(END, key)


#widgets

mab = Label(screen,text = "my adress book:", background = "white", foreground = "black", font = ("times", "25" ))
mab.place(x = 150, y = 50)

name = Label(screen,text = "Name:", background =  "white", foreground = "black", font = ("times", "15" ))
name.place(x = 300, y = 100)

entry1 = Entry(screen)
entry1.place(x = 400, y = 100)


adress = Label(screen,text = "Adress:", background = "white", foreground = "black", font = ("times", "15" ))
adress.place(x = 300, y = 150)

entry2 = Entry(screen)
entry2.place(x = 400, y = 150)


mobile = Label(screen,text = "Mobile:", background = "white", foreground = "black", font = ("times", "15" ))
mobile.place(x = 300, y = 200)

entry3 = Entry(screen)
entry3.place(x = 400, y = 200)


email = Label(screen,text = "Email:", background = "white", foreground = "black", font = ("times", "15" ))
email.place(x = 300, y = 250)

entry4 = Entry(screen)
entry4.place(x = 400, y = 250)


birthday = Label(screen,text = "Birthday:", background = "white", foreground = "black", font = ("times", "15" ))
birthday.place(x = 300, y = 300)

entry5 = Entry(screen)
entry5.place(x = 400, y = 300)




entry_main = Listbox(screen, width = 20, height = 15)
entry_main.place(x = 100, y = 100)

open = Button(screen, text = "open", command = open_file)
open.place(x = 350, y = 50)

edit = Button(screen, text = "edit", command = edit_data)
edit.place(x = 100, y = 400)


delete = Button(screen, text = "delete", command = delete_data)
delete.place(x = 200, y = 400)

update = Button(screen, text = "add/update", command = add_data)
update.place(x = 500, y = 400)

save = Button(screen, text = "save", command = save_data)
save.place(x = 300, y = 500)




#finish ups
screen.mainloop()