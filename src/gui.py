from tkinter import *
from time import *
from PIL import Image, ImageTk
window = Tk()

board = Image.open("Board.png")
img = ImageTk.PhotoImage(board)
w = ImageTk.PhotoImage.width(img)
h = ImageTk.PhotoImage.height(img)
board = board.resize((round(w * 9/4), round(h * 9/4)), Image.ANTIALIAS)
img = ImageTk.PhotoImage(board)
canvas = Canvas(window, width=1366, height=768)
canvas.pack()
m = canvas.create_image(1366/2, 768/2, image=img)
canvas.scale(m, 1366/2, 768/2, 2, 2)
while(True):
   # canvas.move(m,10,0)
    window.update()
    sleep(.01)
