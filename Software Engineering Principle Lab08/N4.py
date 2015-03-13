from PySide.QtCore import *
from PySide.QtGui import *
from turtle import *

N = 5

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*(9./N), 2)
        self.fillcolor(n/float(N), 0, 1-n/float(N))
        self.st()

class Tower(list):
    def __init__(self, x):
        self.x = x
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
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    for i in range(N,0,-1):
        t1.push(Disc(i))
    play()
    return "EVENTLOOP"

if __name__=="__main__":
    msg = main()
    print(msg)
    mainloop()