import turtle
import random

class Disk(object):

    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40,color=None):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.color = color
        if self.color is None:
            self.color = '#'+str(hex(random.randint(0,256*256*256))[2:])

    def showdisk(self, color = None):
        if color is None:
            color = self.color
        turtle.pencolor(color)
        turtle.lt(90)
        turtle.penup()
        turtle.goto(self.dxpos,self.dypos)
        turtle.pendown()
        turtle.rt(90)
        for x in range(2):
            turtle.fd(self.dwidth/2)
            turtle.lt(90)
            turtle.fd(self.dheight)
            turtle.lt(90)
            turtle.fd(self.dwidth/2)

    def newpos(self,xpos,ypos):
        self.dxpos = xpos
        self.dypos = ypos
        
    def cleardisk(self):
        self.showdisk("WHITE")
        turtle.pencolor(self.color)

class Pole(object):

    def __init__(self,name="",xpos=0,ypos=0,thick=10,length=100,color=None):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
        self.color = color
        if self.color is None:
            self.color = '#'+str(hex(random.randint(0,256*256*256))[2:])

    def showpole(self):
        turtle.pencolor(self.color)
        turtle.lt(90)
        turtle.penup()
        turtle.goto(self.pxpos,self.pypos)
        turtle.pendown()
        turtle.rt(90)
        for x in range(2):
            turtle.fd(self.pthick/2)
            turtle.lt(90)
            turtle.fd(self.plength)
            turtle.lt(90)
            turtle.fd(self.pthick/2)
        turtle.pencolor("BLACK")

    def pushdisk(self,disk):
        disk.newpos(self.pxpos,self.toppos)
        disk.showdisk()
        self.stack.append(disk)
        self.toppos += disk.dheight
        self.toppos += 1


    def popdisk(self):
        d = self.stack.pop()
        d.cleardisk()
        self.toppos -= 1
        self.toppos -= d.dheight
        return d
       
class Hanoi(object):

    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i),0,i*150,20,(n-i)*30))

    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)
        
#h = Hanoi()
#h.solve()

from turtle import *
N = 3

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*(9./N), 1)
        self.fillcolor(n/float(N), 0, 1-n/float(N))
        self.st()

class Tower(list,Turtle):
    def __init__(self, x, n):
        self.x = x
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(10*(9./N), 1.5, 1)
        self.fillcolor(1-n/float(N), n/float(N),0)
        self.st()
        self.setx(self.x)

    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    clear()
    hanoi(N, t1, t2, t3)

def main():
    global t1, t2, t3, N
    ht(); penup(); goto(0, -225) 
    t1 = Tower(-250, 1)
    t2 = Tower(0, 2)
    t3 = Tower(250, 3)
    for i in range(N,0,-1):
        t1.push(Disc(i))
    play()
    return "EVENTLOOP"

if __name__=="__main__":
    msg = main()
    print(msg)
    mainloop()


