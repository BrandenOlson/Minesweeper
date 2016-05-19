import OlsonMS
from Tkinter import *

xSize = 70
ySize = 50

class MinesweeperDeprecated(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def centerWindow(self):
        SCREENWIDTH = self.parent.winfo_screenwidth()
        SCREENHEIGHT = self.parent.winfo_screenheight()
        x = (SCREENWIDTH - WIDTH)/2
        y = (SCREENHEIGHT - HEIGHT)/2
        self.parent.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

    def initUI(self):
        self.parent.title("Minesweeper")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

class Minesweeper(Frame):
    board = OlsonMS.Board(xSize, ySize)

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Minesweeper')

        f = frame(self, TOP)
        self.btn = [[0 for x in range(0, xSize)] for y in range(0, ySize)]
        for x in range(0, xSize):
            for y in range(0, ySize):
                textval = ' '
                self.btn[x][y] = Button(f, text=textval, \
                        command = lambda x=x, y=y: self.updateState(x, y))
                self.btn[x][y].grid(column=x, row=y)

    def updateState(self, x, y):
        self.board.sweep(x, y)
        for x in range(0, xSize):
            for y in range(0, ySize):
                textval = ' '
                cell = self.board.board[x][y]
                cellState = cell.state
                if "Swept" == cellState:
                    if cell.neighborCount > 0:
                        textval = str(cell.neighborCount)
                    else:
                        textval = '*'
                self.btn[x][y].config(text=textval)

if __name__ == "__main__":
    xSize = 20
    ySize = 20

    Minesweeper().mainloop()

