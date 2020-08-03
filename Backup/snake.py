from graphics import *
from grid import *
from target import *

class Snake:
    grid = Grid()
    target = Target()
    pos = []
    pos_old = Point(0,0)
    old_positions = [Point(0,0)]
    snake = Rectangle(Point(0,0), Point(0,0))
    tail = []
    lastInput = ''
    speed = 5
    speed_increase = 0.3
    farbe = color_rgb(150,0,255)#rötlich: 120,50,60; #lila-ähnlich: 
    outline = 'white'
    win = GraphWin()
    win.close()
    delay_flag = False

    def __init__(self, win):
        self.win = win
        self.grid.SetDimensions(self.win.getWidth(), self.win.getHeight())    
        self.target.Setup(self.win, self.grid.felder, self.grid.box_width, self.grid.box_height)
        self.pos = self.grid.GetGridPositionAbs(0,0)
        self.DrawSnake()

    def DrawSnake(self):
        self.snake = Rectangle(self.pos[0], self.pos[1])
        self.snake.setFill(self.farbe)
        self.snake.setOutline(self.outline)
        self.snake.draw(self.win)

    def MoveSnake(self):
        self.UserInputMoveSnake()
        self.HitWall()
        
    def UserInputMoveSnake(self):
        input = self.win.checkKey()
        input = self.GetRightInput(input, self.lastInput)
            
        x = self.pos[0].x
        y = self.pos[0].y
        dx = self.grid.box_width
        dy = self.grid.box_height
        if(input == 'Right'):
            self.RepositionSnake(1,0)
            self.RepositionTail()
            self.UpdateTailPos()
            self.SetSnakePosition(x+dx,y)
        elif(input == 'Left'):
            self.RepositionSnake(-1,0)
            self.RepositionTail()
            self.UpdateTailPos()
            self.SetSnakePosition(x-dx,y)
        elif(input == 'Up'):
            self.RepositionSnake(0,-1)
            self.RepositionTail()
            self.UpdateTailPos()
            self.SetSnakePosition(x,y-dy)
        elif(input == 'Down'):
            self.RepositionSnake(0,1)
            self.RepositionTail()
            self.UpdateTailPos()
            self.SetSnakePosition(x,y+dy)
            #self.DrawTail()
        self.lastInput = input

    def GetRightInput(self, curInput, lastInput):
        if (curInput == 'Right' or curInput == 'Left' or curInput == 'Up' or curInput == 'Down'):
            return curInput
        else:
            return lastInput

    def RepositionSnake(self, dx, dy):
        [dx, dy] = self.grid.GetPositionDelta(self.pos[0].x, self.pos[0].y, dx, dy)
        self.snake.move(dx, dy)

    def SetSnakePosition(self, x, y):
        self.pos[0].x = x
        self.pos[0].y = y
        self.pos[1].x = x + self.grid.box_width
        self.pos[1].y = y + self.grid.box_height
        self.SaveOldPos()

    def UpdateTailPos(self):
        if (len(self.old_positions) > 1):
            for i in range(len(self.old_positions), 1, -1):
                self.old_positions[i-1] = self.old_positions[i-2]
        self.old_positions[0] = self.pos_old     
        
    def RepositionTail(self):
        if (len(self.tail) > 0):
            self.delay_flag = True
            if (self.delay_flag):
                self.tail[0].undraw()               
                point2 = self.Get2ndPoint(self.old_positions[0])
                self.tail[0] = Rectangle(self.old_positions[0], point2)
                self.tail[0].setFill('blue')
                self.tail[0].setOutline(self.outline)
                self.tail[0].draw(self.win)

    def SaveOldPos(self):
        self.pos_old = self.pos[0]
        
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

#------------Target-----------

    def Target(self):
        if (self.HitTarget()):
            self.CreateTarget()
            self.UpdateSpeed()
            self.AddBoxToTail()       

    def HitTarget(self):
        if (self.target.x == self.pos[0].x and self.target.y == self.pos[0].y):
            return True
        else:
            return False

    def CreateTarget(self):
        self.target.DrawTarget(self.grid.box_width, self.grid.box_height)

    def UpdateSpeed(self):
        self.speed += self.speed_increase

    def AddBoxToTail(self):
        self.AddOldPos()
        self.DrawNewBox()

    def AddOldPos(self):
        self.old_positions.insert(0, self.pos[0])

    def DrawNewBox(self):
    #     n = len(self.old_positions) - 1
    #     point2 = self.Get2ndPoint(self.old_positions[n])
    #     self.tail.append(Rectangle(self.old_positions[n], point2))
    
        point2 = self.Get2ndPoint(self.pos_old)
        self.tail.append(Rectangle(self.pos_old, point2)) 
        self.tail[0].setFill(self.farbe)
        self.tail[0].setOutline(self.outline)
        self.tail[0].draw(self.win)

    def Get2ndPoint(self, point):
        point2 = Point(0,0)
        point2.x = point.x + self.grid.box_width
        point2.y = point.y + self.grid.box_height
        return point2



        