import tkinter as tk
from tkinter import *

win=tk.Tk()
win.geometry('400x400')
win.title('Mwad Wibs')
win.config(bg='light green') # configuration module. Need to learn more about available functions

def story1(win):
    # define story1 function
    def final(tl: Toplevel, name, sports, city, playername, drinkname, snacks):
        # define functions to take in a set of values provided by user
        text=f'''
            One day me and my friend {name} decided to play a {sports} game in {city}.
            We wanted to watch {playername}.
            We drank {drinkname} and also ate some {snacks} we really enjoyed!
            We are looking forward to go again and enjoy!'''
        tl.geometry(newGeometry='500x550')
        Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)
        # end nested story function
    newScreen=Toplevel(win, bg='yellow')
    newScreen.title('A Memorable Day')
    newScreen.geometry('500x500')

    Label(newScreen, text='Memorable Day').place(x=100, y=0)
    Label(newScreen, text='Name:').place(x=0, y=35)
    Label(newScreen, text='Enter a game:').place(x=0, y=70)
    Label(newScreen, text='Enter a city:').place(x=0, y=110)
    Label(newScreen, text='Enter the name of a player:').place(x=0, y=150)
    Label(newScreen, text='Enter the name of a drink:').place(x=0, y=190)
    Label(newScreen, text='Enter the name of a snack:').place(x=0, y=230)

    name=Entry(newScreen, width=17)
    name.place(x=250, y=35)
    sports=Entry(newScreen, width=17)
    sports.place(x=250, y=70)
    city=Entry(newScreen, width=17)
    city.place(x=250, y=105)
    playername=Entry(newScreen, width=17)
    playername.place(x=250, y=150)
    drinkname=Entry(newScreen, width=17)
    drinkname.place(x=250, y=190)
    snacks=Entry(newScreen, width=17)
    snacks.place(x=250, y=220)

    submitButton=Button(newScreen, text='Submit', bg='blue', font=('Times', 12), command=lambda:final(newScreen, name.get(), sports.get(), city.get(), playername.get(), drinkname.get(), snacks.get()))
    # getting all the user values and passing them through the nested function for use.
    submitButton.place(x=150, y=270)

    newScreen.mainloop()
    # end parent function


Label(win, text='Kanzan\'s Amazing Mad Lib Generator').place(x=100, y=20)

# create buttons
storyButton1=Button(win, text='A memorable day', font=('Times New Roman', 13), command=lambda:story1(win), bg='blue')
# what is command lambda?
storyButton1.place(x=140, y=90)
# storyButton2=Button(win, text='Ambitions', font=('Times New Roman', 13), command=lambda:story2(win), bg='blue')
# storyButton2.place(x=150, y=150)

win.update()
# what does win.update do?
win.mainloop()