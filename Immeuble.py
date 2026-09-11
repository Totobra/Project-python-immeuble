from turtle import *
from random import *

colormode(255)
hideturtle()

def carre(x,y,w,h,c):
    teleport(x,y)
    fillcolor(c)
    begin_fill()
    for _ in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)
    end_fill()    
    return None

def fenetre(x,y):
    carre(x,y,30,30,(255,255,255))

def etage(x,y,c,p):
    carre(x,y,140,60,c)
    for i in range(3):
        if p != i : fenetre(x+15+40*i,y+20)
        else:None

def immeuble(x,y):
    for i in range(4):
        



c = (randint(1,255),randint(1,255),randint(1,255))
etage(-20,-80,c,1)

done()