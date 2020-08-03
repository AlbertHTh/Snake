from graphics import *
from snake import *

# screen_width = 1200
# screen_height = 800

win_width = 600
win_height = 600

win = GraphWin('Snake', win_width, win_height, autoflush=False)
win.setBackground('black')

s = Snake(win)

while True:
    s.MoveSnake()
    s.Target()
    s.SaveOldPos()
    update(s.speed)
    #Testneu
    