import random
from tkinter import *
import tkinter.messagebox
import datetime
todo = Tk()


#basic initialization
WIDTH, HEIGHT = 400, 600
todo.geometry(f"{WIDTH}x{HEIGHT}")
todo.title("HackUNT | Spooky To-Do List")
label = Label(todo,text="EVIL TODO LIST", font=('Arial', 35, 'bold'), fg='brown', bg='black')
label.pack(fill=BOTH)

# if random.randint(1,4) == 1:
#     label = Label(todo,text="EVIL TODO LIST", font=('Arial', 35, 'bold'), fg='white', bg='black')
#     label.pack(fill=BOTH)
# else:
#     label = Label(todo,text="TODO LIST", font=('Arial', 35, 'bold'))
#     label.pack(fill=BOTH)
# label = Label(todo,text=datetime.datetime.now())
# label.pack(fill=BOTH)

icon = PhotoImage(file='hackUntlogo.png')
todo.iconphoto(True,icon)
todo.configure(bg="brown")

def addTask():
    usertask = task.get()
    task.delete(0,END)
    if usertask != "":
        print(usertask)
        tasklist.insert(END, usertask)
        
def deleteTask():
    selected_tasks = tasklist.curselection()
    for task_index in selected_tasks[::-1]:
        tasklist.delete(task_index)
    tasklist.delete(ANCHOR)

def complete():
    pass

def clear():
    tasklist.delete(0,END)


task = Entry(todo, font=('Arial',15))
task.place(x=20,y=100, width=WIDTH-40)
task.insert(0,"Enter a task...")

dl = Entry(todo, font=('Arial',15))
dl.place(x=20,y=150, width=WIDTH-40)
dl.insert(0,"Enter a date (dd/mm/yyyy)...")

addButton = Button(text="ADD", command=addTask)
addButton.place(x=20, y=200, width=100, height=40)

addButton = Button(text="ADD", command=addTask)
addButton.place(x=20, y=200, width=100, height=40)

deleteButton = Button(text="DELETE", command=deleteTask)
deleteButton.place(x=220, y=200, width=100, height=40)

tasklist = Listbox(todo)
tasklist.place(x=20, y=250, width=WIDTH-40, height=300)




todo.mainloop()


