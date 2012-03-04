from tkinter import *
from cell import Cell
from chip import Chip

class Board:
    BOARD_ROWS = 19
    BOARD_COLUMNS = 19
    
    def __init__(self, parent, game):
        self.board = []
        self.game = game
        for row in range(self.BOARD_ROWS):
            rowcell = []
            for column in range(self.BOARD_COLUMNS):
                image = PhotoImage(file='images/middleboard.gif')
                c = Cell(parent, self, self.game, image, row, column)
                c.grid(row=row, column=column)
                rowcell.append(c)
            self.board.append(rowcell)
            
    def getCell(self, row, column):
        return self.board[row][column]
    
    def clear(self):
        for row in self.board:
            for cell in row:
                cell.removeChip()

    def interactOn(self, color):
        for row in self.board:
            for cell in row:
                cell.interactOn(color)
