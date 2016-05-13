import OlsonMS
from Tkinter import *

xSize = 7
ySize = 5

WIDTH = 100*xSize
HEIGHT = 100*ySize

class Minesweeper(Frame):
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

if __name__ == "__main__":
    xSize = 40
    ySize = 40
    b = OlsonMS.Board(xSize, ySize)
    b.printBoard()

    b.printBoard()

    b.randomize()

    b.printBoard()

    for x in range(0, xSize):
        for y in range(0, ySize):
            b.sweep(x, y)

    b.printBoard()

    sys.exit()
    root = Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    app = Minesweeper(root)
    root.mainloop()

