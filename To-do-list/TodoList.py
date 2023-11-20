import tkinter as tk
from tkinter import PhotoImage

def resize_image(image, width, height):
    return image.subsample(image.width() // width, image.height() // height)

task_list = []

def addTask():
     task = task_entry.get()
     task_entry.delete(0, tk.END)
     if task:
          with open('tasklist.txt', 'a') as taskfile:
               taskfile.write(f'\n{task}')
          task_list.append(task)
          listbox.insert(tk.END, task)

def deleteTask():
     global task_list
     task = str(listbox.get(tk.ANCHOR))
     if task in task_list:
          task_list.remove(task)
          with open('tasklist.txt', 'w') as taskfile:
               for task in task_list:
                    taskfile.write(task+'\n')
          listbox.delete(tk.ANCHOR)

def openTaskList():
     
     try:
          global task_list
          with open('tasklist.txt','r') as taskfile:
               tasks = taskfile.readlines()

          for task in tasks:
               if task != '\n':
                    task_list.append(task)
                    listbox.insert(tk.END,task)
     except:
          file = open('tasklist.txt', 'w')
          file.close()
           



window = tk.Tk()
window.geometry('500x650')
window.title('To-Do-List')
window.resizable(False,False)
icon = PhotoImage(file='toDo.png')
window.iconphoto(True, icon)
window.config(bg='#EEEDED')
title_image = PhotoImage(file='sketch.png')
width = 50  # Set the desired width
height = 40  # Set the desired height
resized_image = resize_image(title_image, width, height)
to_do_top = tk.Label(window, text='ALL TASK', font=('arial 20 bold'), image=resized_image, compound='right',bg='#32405b', fg='white',width=500)
to_do_top.pack()

#main
frame = tk.Frame(window, width=500,height=50,bg='white')
frame.place(x=0,y=150)

task = tk.StringVar()
task_entry = tk.Entry(frame, width=25,font='arial 20', bd=0, relief='solid',  borderwidth=2)
task_entry.place(x=10,y=7)
task_entry.focus()
button =tk.Button(frame, text='ADD', font='arial 20 bold', width=6, bg='#5a95ff', fg='#fff', bd=0 , command=addTask)
button.place(x=400, y=0)


#listbox
frame1= tk.Frame(window, bd=3, width=700,height=350,bg='#32405b')
frame1.pack(pady=(160,0))

listbox=tk.Listbox(frame1, font=('arial', 12), width=50,height=16,bg='#32405b',fg='white',cursor='hand2',selectbackground='#5a95ff')
listbox.pack(side='left', fill='both',padx=2)
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side='right', fill='both')
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskList()

bottom_image = PhotoImage(file='delete.png')
width_1 = 50  # Set the desired width
height_1 = 50  # Set the desired height
delete_image = resize_image(bottom_image, width_1, height_1)
to_do_bottom = tk.Button(window,  image=delete_image, command=deleteTask)
to_do_bottom.place(x=220, y=570)
window.mainloop()


