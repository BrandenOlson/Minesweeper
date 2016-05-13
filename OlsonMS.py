import numpy as np
from random import *

class Cell:
    state = "Unswept"
    neighborCount = 0

    def __init__(self, state):
        self.state = state

class Board:
    xSize = 40
    ySize = 40
    printingValue = {"Unswept": 0, "Mine": 'X'}
    neighborCount = 0

    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        self.board = [[Cell("Unswept") for y in range(self.ySize)] \
                       for x in range(self.xSize)] 
    
    def printBoard(self):
        for i in range(self.xSize):
            for j in range(self.ySize):
                cell = self.board[i][j]
                if cell.state == "Swept":
                    if cell.neighborCount > 0:
                        print cell.neighborCount,
                    else:
                        print '*',
                else:
                    print self.printingValue[self.board[i][j].state],
            print 
        print

    def setState(self, i, j, state):
        self.board[i][j].state = state

    def isOnBoard(self, i, j):
        return i >= 0 and i < self.xSize and j >= 0 and j < self.ySize

    def randomize(self):
        mineCount = self.xSize*self.ySize/8
        currentCount = 0
        while currentCount < mineCount:
            x = randint(0, self.xSize - 1)
            y = randint(0, self.ySize - 1)
            cell = self.board[x][y]
            if cell.state != "Mine":
                cell.state = "Mine"
                currentCount = currentCount + 1

    def sweep(self, i, j):
        cell = self.board[i][j] 
        if "Mine" == cell.state:
            print("YOU LOSE")
            return

        if "Swept" == cell.state:
            return

        mineCount = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if self.isOnBoard(x, y) and not(x == i and y == j):
                    if self.board[x][y].state == "Mine":
                        mineCount = mineCount + 1

        cell.state = "Swept"
        cell.neighborCount = mineCount

        if 0 == cell.neighborCount:
            toCheck = [[i, j - 1], [i + 1, j], [i, j + 1], [i - 1, j]]
            for x, y in toCheck:
                if self.isOnBoard(x, y) and self.board[x][y].state is not "Mine":
                    self.sweep(x, y) 

