from turtle import *
from random import *

colormode(255)
hideturtle()

def mega_giga_super_ultre_special_tera_kilo_peta_putain_ins():
    ins = []
    for i in range(4):
        tac = []
        for j in range(randint(1,5)):
            tic = []
            if j == 0:
                tic.append(randint(0,2))
            else:
                tic = []
                for i in range(3):
                    tic.append(randint(0,2))
            tac.append(tic)    
        ins.append(tac)  
    return ins

ins = mega_giga_super_ultre_special_tera_kilo_peta_putain_ins()

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

def etage(x,y,c,ins,i,j):
    carre(x,y,140,60,c)
    for k in range(3):
        if k not in ins[i][j] : fenetre(x+15+40*k,y+20)
        else:None
    return None

def immeuble(x,y,c,ins,i):
    for j in range(len(ins[i])):
        etage(x,y+60*j,c,ins,i,j)
    return None

def cartier(x,y,c,ins):
    for i in range(4):
        immeuble(x+i*170,y,c[i],ins,i)
    return None

def immeuble_color():
    c = []
    for i in range(4):
        c.append((randint(1,255),randint(1,255),randint(1,255)))
    return c

def initialisation():
    c = immeuble_color()
    cartier(-200,-80,c,ins)
    return None

done()