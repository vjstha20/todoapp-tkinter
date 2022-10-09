from tkinter import *
import pickle
import tkinter.messagebox

root = tkinter.Tk()
root.title("To Do List App by Vijay")
root.iconbitmap('D:/projects_repo/todoapp-tkinter/favicon.ico')

def add_task():
	task = entry_task.get()
	if task != "":
		listbox_task.insert(tkinter.END,task)
		entry_task.delete(0,tkinter.END)
	else:
		tkinter.messagebox.showwarning(title="Warning!", message = "You Must Enter a Task!")

def delete_task():
	try:
		task_index = listbox_task.curselection()[0]
		listbox_task.delete(task_index)
	except:
		tkinter.messagebox.showwarning(title="Warning!", message = "You Must Select a Task!")

def save_task():
	tasks = listbox_task.get(0,listbox_task.size())
	#print(tasks)
	pickle.dump(tasks,open("tasks.dat","wb"))

def load_task():
	try:
		tasks = pickle.load(open("tasks.dat","rb"))
		listbox_task.delete(0,tkinter.END)
		for task in tasks:
			listbox_task.insert(tkinter.END,task)
	except:
		tkinter.messagebox.showwarning(title="Warning!", message = "Cannot Find Data File!")
		

#Creating GUI

#Creating frame
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_task = tkinter.Listbox(frame_tasks, height=10,width=50)
listbox_task.pack(side=tkinter.LEFT)

#Creating scrollbar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_task.yview)

entry_task = tkinter.Entry(root, width = 50)
entry_task.pack()

#Creating buttons
button_add_task = tkinter.Button(root,text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root,text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(root,text="Load Task", width=48, command=load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root,text="Save Task", width=48, command=save_task)
button_save_task.pack()

root.mainloop()
