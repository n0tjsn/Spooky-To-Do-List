import random
from tkinter import *
import tkinter.messagebox
from playsound import playsound
import time
todo = Tk()

#basic initialization
WIDTH, HEIGHT = 400, 600
BUTTON_WIDTH = WIDTH/5
todo.geometry(f"{WIDTH}x{HEIGHT}")
todo.title("HackUNT | Spooky To-Do List")
label = Label(todo,text="EVIL TODO LIST", font=('Arial', 35, 'bold'), fg='brown', bg='black')
label.pack(fill=BOTH)

canvas = Canvas(todo, width=WIDTH, height=HEIGHT, background="brown")
canvas.pack()

if random.randint(1,4) == 1:
    label = Label(todo,text="EVIL TODO LIST", font=('Arial', 35, 'bold'), fg='white', bg='black')
    label.pack(fill=BOTH)
else:
    label = Label(todo,text="TODO LIST", font=('Arial', 35, 'bold'))
    label.pack(fill=BOTH)
label.pack(fill=BOTH)

# FIXME
# icon = PhotoImage(file='hackUntlogo.png')
# todo.iconphoto(True,icon)
# todo.configure(bg="brown")

#BUTTON FUNCTIONS
def addTask():
    usertask = task.get()
    task.delete(0,END)
    if usertask != "":
            if random.randint(1,4) == 1:
                tasklist.insert(END, "I'm evil...")
            else:
                tasklist.insert(END, usertask)

def deleteTask():
    selected_tasks = tasklist.curselection()
    for task_index in selected_tasks[::-1]:
        tasklist.delete(task_index)
    tasklist.delete(ANCHOR)
    
def saveTasks():
    tasks = tasklist.get(0,END)
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task + "\n") 
    tkinter.messagebox.showinfo("Saved", "Your tasks have been saved")

def loadTasks():
    tasklist.delete(0,END)
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    for task in tasks:
        tasklist.insert(END, task)
    tkinter.messagebox.showinfo("Loaded", "Your tasks have been loaded")

def clearTasks():
    tasklist.delete(0,END)
    tkinter.messagebox.showinfo("Cleared", "Your tasks have been cleared")

#MISC FUNCTIONS
def entryFocusIn():
    if task.get() == "Enter a task...":
        task.delete(0,END)
        task.configure(fg='black')

def entryFocusOut():
    if task.get() == "":
        task.insert(0,"Enter a task...")
        task.configure(fg='gray')

def focus(event):
    if task.get() == "Enter a task...":
        task.delete(0,END)
        task.configure(fg='black')
    
def defocus(event):
    if task.get() == "":
        task.insert(0,"Enter a task...")
        task.configure(fg='gray')

def exit():    
    if tkinter.messagebox.askyesno("I wouldn't do that...", "Are you sure you want to do that?"):
            if tkinter.messagebox.askokcancel("...", "..."): 
                    todo.destroy()

#TEXT BOXES
task = Entry(todo, font=('Arial',15))
task.insert(0,"Enter a task...")
task.bind("<FocusIn>", focus)
task.bind("<FocusOut>", defocus)
task.place(x=20,y=100, width=WIDTH-40)

#BUTTONS
addButton = Button(text="ADD", command=addTask)
addButton.place(x=0, y=150, width=BUTTON_WIDTH, height=40)

deleteButton = Button(text="DELETE", command=deleteTask)
deleteButton.place(x=BUTTON_WIDTH, y=150, width=BUTTON_WIDTH, height=40)

saveButton = Button(text="SAVE", command=saveTasks)
saveButton.place(x=BUTTON_WIDTH*2, y=150, width=BUTTON_WIDTH, height=40)

loadbutton = Button(text="LOAD", command=loadTasks)
loadbutton.place(x=BUTTON_WIDTH*3, y=150, width=BUTTON_WIDTH, height=40)

clearButton = Button(text="CLEAR", command=clearTasks)
clearButton.place(x=BUTTON_WIDTH*4, y=150, width=BUTTON_WIDTH, height=40)

#TASKS LIST
tasklist = Listbox(todo, font=('Arial', 15))
tasklist.place(x=20, y=220, width=WIDTH-40, height=350)

todo.protocol("WM_DELETE_WINDOW", exit)
todo.mainloop()
