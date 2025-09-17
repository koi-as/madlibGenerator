import tkinter as tk
from tkinter import *

win=tk.Tk()
win.geometry('x')
win.title('Mwad Wibs')
win.config(bg='light green')

Label(win, text='Kanzan\'s Amazing Mad Lib Generator').place(x=100, y=20)

# create buttons
storyButton1=Button(win, text='A memorable day', font=('Times New Roman', 13), command=lambda:story1(win), bg='blue')
storyButton1.place(x=140, y=90)
storyButton2=Button(win, text='Ambitions', font=('Times New Roman', 13), command=lambda:story2(win), bg='blue')
storyButton2.place(x=150, y=150)

win.update()
win.mainloop()