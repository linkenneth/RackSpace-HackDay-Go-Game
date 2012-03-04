from tkinter import *
from board import Board
from chip import Chip

class Game:

    def __init__(self):
        self.turn = Chip.BLACK
        self.started = False
        
        root = Tk()
        boardFrame = Frame(root, width=500, height=500, relief=RIDGE, borderwidth=2)
        boardFrame.pack(side=LEFT)
        board = Board(boardFrame, self)
        rightFrame = Frame(root, width=200, height=500, relief=RIDGE, borderwidth=2)
        rightFrame.pack(side=RIGHT)
        clearButton = Button(rightFrame, text='Clear', command=board.clear)
        startButton = Button(rightFrame, text='Start', command=self.start)
        clearButton.pack()
        startButton.pack()

        root.mainloop()

    def start(self):
        self.started = True

if __name__ == "__main__":
    GO = Game()
