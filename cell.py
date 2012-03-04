from tkinter import *

class Cell(Label):

    def __init__(self, parent, board, game, imagepix, row, column):
        Label.__init__(self, parent, image=imagepix)
        self.parent = parent
        self.board = board
        self.row = row
        self.column = column
        self.chip = None
        self.chain = None
        self.liberty = set()
        self.bind("<Button-1>", self.addChip(game))

    def addChip(self, game):
        """Adds the chip to the cell. Also checks neighboring chains, and
        if the chain is the same color as the chip played, then connect the
        chain. Otherwise, if it is the opposite color, remove this cell's
        liberty from the opposing chain."""
        def eventActivate(event):
            if game.started:
                if self.playable():
                    self.chip = Chip(game.turn, self)
                    for neighbor in self.getDirectNeighbors():
                        if neighbor is not None:
                            if neighbor.chip.color == self.chip.color:
                                self.connectChain(neighbor)
                            else:
                                neighbor.chip.removeLiberty(self)
                        else:
                            self.liberty = getDirectNeighbors()
                    #graphics stuff
                    game.turn = 1-game.turn  # next turn
        return eventActivate

    def getChip(self):
        return self.chip

    def removeChip(self):
        if self.chip is not None:
            self.chip.destroy()
            self.chip = None
            self.chain = None

    @property
    def playable(self):
        """Playability relies on three conditions: whether the cell is completely
        blocked off (no immediate liberties), whether the cell is already
        occupied, and whether it returns the board to the same board a move
        ago."""
        for neighbor in self.getDirectNeighbors():
            if neighbor is None or neighbor.chip.color == self.chip.color:
                return True
        # add later - check if it makes the same board as before
        return False

    @property
    def position(self):
        return (self.row, self.column)

    def connectChain(self, neighbor):
        """Connects the chain of this cell with the chain of that cell, or
        forms a new chain if neither has one."""
        if (self.chain is None) and (neighbor.chain is None):
            Chain([self, neighbor])
        elif (self.chain is None) and (neighbor.chain is not None):
            neighbor.chain.appendToChain(self)
        elif (self.chain is not None) and (neighbor.chain is None):
            self.chain.appendToChain(neighbor)
        else:
            self.chain.mergeToChain(neighbor)

    def getNeighboringCells(self):
        """Returns a list of cells neighboring the cell in a 3x3 block."""
        neighbors = []
        for i in range(-1,2):
            neighborRow = self.row + i
            if neighborRow < 0 or neighborRow >= self.board.BOARD_ROWS:
                continue
            for j in range(-1,2):
                neighborColumn = self.column + j
                if (neighborRow < 0 or neighborRow >= self.board.BOARD_COLUMNS) or \
                   (i == 0 and j == 0):
                    continue
                neighbors.append(self.board.getCell(neighborRow, neighborColumn))
        return neighbors

    def getDirectNeighbors(self):
        """Returns a list of cells neighboring the cell in a cross."""
        neighbors = []
        invalidCells = ((-1,-1),(-1,1),(1,1),(1,-1),(0,0))
        for i in range(-1,2):
            neighborRow = self.row + i
            if neighborRow < 0 or neighborRow >= self.board.BOARD_ROWS:
                continue
            for j in range(-1,2):
                neighborColumn = self.column + j
                if (neighborRow < 0 or neighborRow >= self.board.BOARD_COLUMNS) or \
                   ((i,j) in invalidCells):
                    continue
                neighbors.append(self.board.getCell(neighborRow, neighborColumn))
        return neighbors

    def removeLiberty(self, other):
        if self.chain != None:
            self.chain.liberties.remove(other)
            if self.chain.liberties == set():
                self.chain.removeChain()
        elif other in self.liberties:
            self.liberties.remove(other)
            if self.liberties == set():
                self.removeChip()

