from graphics import *
from snake import *

#Snake Spiel
win_width = 600
win_height = 600

win = GraphWin('Snake', win_width, win_height, autoflush=False)
win.setBackground('black')

s = Snake(win)

while True:
    s.Run()
    update(s.speed)
    