from graphics import *

class Test:
    point = Point(0,0)
    pos =[Point(0,0), Point(0,0)]

    def __init__(self, x, y):
        self.pos[0].x = x
        self.pos[0].y = y
        self.pos[1].x = 2*x
        self.pos[1].y = 2*y
    
    def save(self):
        self.point.x = self.pos[0].x

t = Test(20,20)
print(t.point.x)
t.save()
print(t.point.x)
t.pos[0].x = 10
print(t.point.x)

print('---------------\nTest1')
list = [1, 2, 3]
print('0:' + str(list[0]) + '\n1:' + str(list[1]) + '\n2:' + str(list[2]) )
for i in range(len(list)-1, 0, -1):
    # print(str(list[i]))
    list[i] = list[i-1]
    # print(str(list[i]))
list[0] = 0
print(str(list[0]))
print(str(list[1]))
print(str(list[2]))
    
