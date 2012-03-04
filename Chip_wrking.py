from tkinter import *

class Cell(Label):

    def __init__(self, board, row, column):
        Label.__init__(board)
        self.board = board
        self.row = row
        self.column = column
        self.chip = None
        self.bind("<Button-1>", self.addChip)

    def addChip(self, chip):
        if self.board.playable:
            self.chip = chip

    def removed(self):
        if self
        

    def getChip(self):
        return self.chip

    def removeChip(self):
        self.chip.destroy()
        self.chip = None

class Chain:
    def __init__(self, cells):
        self.contained = cells
        self.liberties = self.createLiberties()
        for cell in cells:
            cell.chain = self

    def appendToChain(self, cell):
        """Appends one item to the chain"""
        self.contained.append(cell)
        cell.chain = self
        self.updateLiberties(cell)

    def mergeToChain(self, chain):
        """Extend one chain to another"""
        self.contained.extend(cell.chain.contained)
        for cell in chain.contained:
            cell.chain = self
        self.liberties = self.createLiberties()

    def createLiberties(self):
        """Takes in a chain and creates the attribute _liberties to keep track
        of the liberties of the chain"""   
        liberties = set()
        for cell in self.contained:
            liberties.add(cell.liberty)
        liberties = set(filter(lambda liberty: liberty.chip != None, liberties))
        
    def updateLiberties(self, cell):
        """"Is called when a new chip is added to update the number of liberties
        of the chain. cell is the object cell where the new chip is added"""
        if cell in self.liberties:
            self.liberties.remove(cell)
        for neighbour in getDirectNeighbors(cell):
            if neighbour.getChip() == None:
                self.liberties.add(neighbor)
            
        
        
    
        

