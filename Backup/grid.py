from graphics import *

class Grid:
    win_width = 0
    win_height = 0
    felder = 30
    box_width = 0
    box_height = 0

    def __init__(self):
        pass

    def SetDimensions(self, win_height, win_width):
        #Bestimmt die Boxgröße anhand der Fenstergröße und der Felderanzahl
        self.win_height = win_height
        self.win_width = win_width
        self.box_width = self.win_width / self.felder
        self.box_height = self.win_width / self.felder

    def GetGridPositionAbs(self, x, y):
        # x - Zeile, y - Spalte; Beginnend bei "0"; Absoluter Wert in Pixeln
        x1 = x*self.box_width
        y1 = y*self.box_height
        x2 = x*self.box_width + self.box_width
        y2 = y*self.box_height + self.box_height
        return [Point(x1,y1), Point(x2,y2)]

    def GetGridPositionRel(self, x, y):
        # x - Zeile, y - Spalte; Beginnend bei "0"; Relativer Wert zw. [0 grid.felder]
        x = x / self.box_width
        y = y / self.box_height
        return [x, y]

    def GetPositionDelta(self, x, y, dx, dy):
        dx = dx*self.box_width
        dy = dy*self.box_height
        return [dx, dy]