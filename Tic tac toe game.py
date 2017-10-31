# Tic tac toe Boi 
import Tkinter

screen = Tkinter.Tk()
screen.title("Tic Tac Toe Boi")

#Create a board
board = Tkinter.Canvas(screen,width=300,height=300)
board.pack()


board.create_rectangle(0,0,300,300, outline="black")
board.create_rectangle(100,300,200,0, outline="black")
board.create_rectangle(0,100,300,200, outline="black")

screen.mainloop()