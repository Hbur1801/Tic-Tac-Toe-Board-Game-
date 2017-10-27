# Tic tac toe Boi 
import Tkinter

screen = Tkinter.Tk()
screen.title("Tic Tac Toe Boi")

#Create a board
board = Tkinter.Canvas(screen,width=500,height=500)
board.pack()
board.create_line(0, 0, 200, 100)

screen.mainloop()