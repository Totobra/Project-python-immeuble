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

carre(20,40,30,-20,(12,68,240))

done()