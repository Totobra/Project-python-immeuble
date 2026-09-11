from turtle import *
from random import *

colormode(255)
hideturtle()

def mega_giga_super_ultre_special_tera_kilo_peta_putain_ins()

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
    return None

def etage(x,y,c,p):
    carre(x,y,140,60,c)
    for i in range(3):
        if p != i : fenetre(x+15+40*i,y+20)
        else:None
    return None

def immeuble(x,y,c,ins):
    for i in range(4):
        etage(x,y+60*i,c,ins)
    return None

def cartier(x,y,c,ins):
    for i in range(4):
        immeuble(x+i*170,y,c[i],ins)
    return None

c = []
for i in range(4):
    c.append((randint(1,255),randint(1,255),randint(1,255)))
cartier(-200,-80,c,4)

done()