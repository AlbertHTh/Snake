from random import *
from graphics import *

class Target:
    x = 0 
    y = 0
    limit = 0
    box_width = 0
    box_height = 0 
    tar = Rectangle(Point(x,y), Point(x,y))
    farbe = 'red'
    outline = 'white'
    win = GraphWin()
    win.close()
        
    def Setup(self, win, limit, box_width, box_height):
        self.win = win
        self.limit = limit
        self.box_height = box_height
        self.box_width = box_width
        x = self.GetRandZahl()*box_width
        y = self.GetRandZahl()*box_height
        self.SetCurPos(x,y)
        self.tar = Rectangle(Point(x, y), Point(x + box_width, y + box_height))
        self.tar.setFill(self.farbe)
        self.tar.setOutline(self.outline)
        self.tar.draw(win)  

    def GetRandZahl(self):
        return randrange(0, self.limit) #Zahl zw. 0 und limit - 1, da limit außerhalb wäre

    def SetCurPos(self, x, y):
        self.x = x
        self.y = y

    def DrawTarget(self, box_width, box_height):
        x = self.GetRandZahl()*box_width
        y = self.GetRandZahl()*box_height
        self.SetCurPos(x,y)
        
        self.tar.undraw()
        self.tar = Rectangle(Point(x, y), Point(x + box_width, y + box_height))
        self.tar.setFill(self.farbe)
        self.tar.setOutline(self.outline)
        self.tar.draw(self.win)
    