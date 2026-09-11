from turtle import *
from random import *

colormode(255)


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

carre(20,40,30,-20,(12,68,240))

done()