from tkinter import *

class Chip(Label):
    BLACK = 0
    WHITE = 1
    
    def __init__(self, color, cell):
        Label.__init__(self, cell, relief=RIDGE)
        self.cell = cell
        self.setColor(color)
        
    def setColor(self, newcolor):
        self.color = newcolor
        if self.color == Chip.BLACK:
            self['image'] = PhotoImage(file='images/black.gif')
        else:
            self['image'] = PhotoImage(file='images/white/gif')

