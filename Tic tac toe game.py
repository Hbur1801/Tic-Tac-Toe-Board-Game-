# Tic tac toe Boi 
from Tkinter import *   # don't pollute namespace like this except for Tkinter
import PIL    
from PIL import ImageTk # a subpackage that must be imported explicitly

import os.path              
__dir__ = os.path.dirname(os.path.abspath(__file__))  
filename = os.path.join(__dir__, 'tictacx.png')
img = PIL.Image.open(filename)




screen = Tk()
screen.title("Tic Tac Toe Boi")

#Create a board
board = Canvas(screen,width=300,height=300)
board.pack()


board.create_rectangle(0,0,300,300, outline="black")
board.create_rectangle(100,300,200,0, outline="black")
board.create_rectangle(0,100,300,200, outline="black")
tkimg=PIL.ImageTk.PhotoImage(img)
def stamp(event):
    board.create_image(event.x,event.y,image=tkimg)
    board.create_rectangle(40,50,300,200, outline="red")
# Bind event to handler

board.bind('<ButtonPress-1>', stamp)


screen.mainloop()