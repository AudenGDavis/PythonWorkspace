'''
Created on Dec 14, 2021

@author: adavis25
'''
from tkinter import *
from tkinter import ttk

root = Tk()

exitButton = Button(root, text="Exit", command=root.destroy())
exitButton.place(x=0, y=0) 
ttk = Label(root, text="Hello World!")
ttk2 = Button()
root.mainloop() 
