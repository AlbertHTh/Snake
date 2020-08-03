from graphics import *
from grid import *
from target import *

class Snake:
#------------Eigenschaften-----------
    grid = Grid()
    target = Target()
    win = GraphWin()
    win.close()
    pos = []
    pos_old = Point(0,0)
    old_positions = []
    snake = Rectangle(Point(0,0), Point(0,0))
    tail = []
    lastInput = ''
    speed = 5
    speed_increase = 0.3
    farbe = color_rgb(150,0,255)#rötlich: 120,50,60; #lila-ähnlich: 
    outline = 'white'
    hit_target_flag = False

#------------Initialisierung-----------
    def __init__(self, win):
        self.win = win
        self.grid.SetDimensions(self.win.getWidth(), self.win.getHeight())    
        self.target.Setup(self.win, self.grid.felder, self.grid.box_width, self.grid.box_height)
        self.pos = self.grid.GetGridPositionAbs(0,0)
        self.InitializeSnake()

    def InitializeSnake(self):
        self.snake = Rectangle(self.pos[0], self.pos[1])
        self.snake.setFill(self.farbe)
        self.snake.setOutline(self.outline)
        self.snake.draw(self.win)
        
#------------Run-----------       
    def Run(self):
        self.MoveSnake()
        self.Target()

#------------MoveSnake-----------
    def MoveSnake(self):
        self.UserInputMovesSnake()
        self.HitWall()
        self.HitTail()
        self.SaveCurPos()

    def UserInputMovesSnake(self):
        input = self.win.checkKey()
        input = self.GetRightInput(input, self.lastInput)
            
        x = self.pos[0].x
        y = self.pos[0].y
        dx = self.grid.box_width
        dy = self.grid.box_height

        if(self.HitTarget() == False and self.hit_target_flag == False): # Nur ausführen wenn letzte und diese Runde kein Target getroffen wurde
            self.UpdateTailPos()
        self.hit_target_flag = False #Reset flag

        if(input == 'Right'):
            self.RepositionHead(1,0)
            self.RepositionTail()
            self.SetCurHeadPosition(x+dx,y)
        elif(input == 'Left'):
            self.RepositionHead(-1,0)
            self.RepositionTail()
            self.SetCurHeadPosition(x-dx,y)
        elif(input == 'Up'):
            self.RepositionHead(0,-1)
            self.RepositionTail()
            self.SetCurHeadPosition(x,y-dy)
        elif(input == 'Down'):
            self.RepositionHead(0,1)
            self.RepositionTail()
            self.SetCurHeadPosition(x,y+dy)
        self.lastInput = input

    def GetRightInput(self, curInput, lastInput):
        if (curInput == 'Right' or curInput == 'Left' or curInput == 'Up' or curInput == 'Down'):
            return curInput
        else:
            return lastInput
            
    def UpdateTailPos(self):
        if self.TailExists():
            for i in range(len(self.old_positions)-1, 0, -1):
                self.old_positions[i].x = self.old_positions[i-1].x
                self.old_positions[i].y = self.old_positions[i-1].y
            self.old_positions[0].x = self.pos_old.x 
            self.old_positions[0].y = self.pos_old.y  

    def RepositionHead(self, dx, dy):
        [dx, dy] = self.grid.GetPositionDelta(self.pos[0].x, self.pos[0].y, dx, dy)
        self.snake.move(dx, dy)

    def RepositionTail(self):
        if self.TailExists(): 
            for i in range(0, len(self.tail)):
                self.tail[i].undraw()                   
                point2 = self.Get2ndPoint(self.old_positions[i])
                self.tail[i] = Rectangle(self.old_positions[i], point2)
                self.tail[i].setFill('blue')
                self.tail[i].setOutline(self.outline)
                self.tail[i].draw(self.win)

    def SetCurHeadPosition(self, x, y):
        self.pos[0].x = x
        self.pos[0].y = y
        self.pos[1].x = x + self.grid.box_width
        self.pos[1].y = y + self.grid.box_height  
    
    def TailExists(self):
        return len(self.tail) > 0

    def HitWall(self):
        if (self.pos[0].x < 0 or self.pos[0].y < 0 \
            or self.pos[1].x > self.win.getWidth() or self.pos[1].y > self.win.getHeight()):
            message = Text(Point(self.win.getWidth()/2, self.win.getHeight()/2), 'GAME OVER\n Click anywhere to exit...')
            message.setSize(25)
            message.setFace('helvetica')
            message.setFill('white')
            message.draw(self.win)
            self.win.getMouse()
            self.win.close()

    def HitTail(self):
        if(self.CheckHitTail()):
            message = Text(Point(self.win.getWidth()/2, self.win.getHeight()/2), 'GAME OVER\n Click anywhere to exit...')
            message.setSize(25)
            message.setFace('helvetica')
            message.setFill('white')
            message.draw(self.win)
            self.win.getMouse()
            self.win.close()

    def CheckHitTail(self):
        for i in range(0, len(self.old_positions)):
            if (self.old_positions[i].x == self.pos[0].x and self.old_positions[i].y == self.pos[0].y):
                return True
        else: 
            return False
                
    def SaveCurPos(self):
        self.pos_old.x = self.pos[0].x
        self.pos_old.y = self.pos[0].y

#------------Target-----------
    def Target(self):
        if (self.HitTarget()):
            self.CreateTarget()
            self.UpdateSpeed()
            self.ExtendTail() 

    def HitTarget(self):
        if (self.target.x == self.pos[0].x and self.target.y == self.pos[0].y):
            self.hit_target_flag = True
            return True
        else:
            return False

    def CreateTarget(self):
        self.target.DrawTarget(self.grid.box_width, self.grid.box_height)

    def UpdateSpeed(self):
        self.speed += self.speed_increase

    def ExtendTail(self):
        self.AddCurPosToOldPos()
        self.AddBoxToTail()

    def AddCurPosToOldPos(self):
        self.old_positions.insert(0, Point(0,0)) 
        self.old_positions[0].x = self.pos[0].x 
        self.old_positions[0].y = self.pos[0].y

    def AddBoxToTail(self):
        point2 = self.Get2ndPoint(self.old_positions[0])
        self.tail.insert(0, Rectangle(self.old_positions[0], point2)) 

    def Get2ndPoint(self, point):
        point2 = Point(0,0)
        point2.x = point.x + self.grid.box_width
        point2.y = point.y + self.grid.box_height
        return point2



        