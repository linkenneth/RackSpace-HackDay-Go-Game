from tkinter import *


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
        self.liberties.remove(cell)
        
        for neighbour in getDirectNeighbors(cell):
            if neighbour.getChip() == None:
                self.liberties.add(neighbor)

    def removeChain(self):
        for cell in self.contained:
            cell.removeChip()
            
        
        
    
        

