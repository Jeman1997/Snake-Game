from turtle import *
import random
class Snake():
    def __init__(self):
        self.start_pos=[(0,0),(-20,0),(-40,0)]
        self.col=['blue','red','green','pink','brown']
        self.seg=[]
        for x in self.start_pos:
            self.addseg(x)
            
    def addseg(self,pos):
        ns=Turtle('square')
        ns.color(random.choice(self.col))
        ns.penup()
        ns.setpos(pos)
        self.seg.append(ns)
    def extend(self):
        self.addseg(self.seg[-1].position())
    def move(self):
        for sn in range(len(self.seg)-1,0,-1):
            self.seg[sn].goto(self.seg[sn-1].xcor(),self.seg[sn-1].ycor())
        self.seg[0].fd(20) 

    def upward(self):
        if self.seg[0].heading()!=270:
            self.seg[0].setheading(90)
        else:
            pass
    def downward(self):
        if self.seg[0].heading()!=90:
            self.seg[0].setheading(270)
        else:
            pass
    def rightward(self):
        if self.seg[0].heading()!=180:
            self.seg[0].setheading(0)
        else:
            pass
    def leftward(self):
        if self.seg[0].heading()!=0:
            self.seg[0].setheading(180)
        else:
            pass
    def reset(self):
        for s in self.seg:
            s.goto(1000,1000)
        self.seg.clear()
        for x in self.start_pos:
            self.addseg(x)
