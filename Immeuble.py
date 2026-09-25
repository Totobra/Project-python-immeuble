from turtle import *
from random import *

colormode(255)
hideturtle()
speed(1000)
screensize(900,480)

def mega_giga_super_ultre_special_tera_kilo_peta_fantastique_legendaire_cosmique_galactique_infini_absolu_supreme_mythique_divin_titanesque_colossal_cataclysmique_universel_sideral_apocalyptique_ins():
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
                    tic.append(randint(0,3))
            tac.append(tic)    
        ins.append(tac)  
    return ins

ins = mega_giga_super_ultre_special_tera_kilo_peta_fantastique_legendaire_cosmique_galactique_infini_absolu_supreme_mythique_divin_titanesque_colossal_cataclysmique_universel_sideral_apocalyptique_ins()

def rectangle(x,y,w,h,c):
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

def fenetre(x,y,c=(255,255,255)):
    if 0 == randint(0,1):
        rectangle(x,y,30,30,c)
    elif 0 == randint(0,1):
        fillcolor(c)
        begin_fill()
        teleport(x+15,y)
        circle(15)
        end_fill()
        teleport(x,y)
        begin_fill()
        goto(x,y+15)
        penup()
        goto(x+30,y+15)
        pendown()
        goto(x+30,y)
        goto(x,y)
        end_fill()
    else:
        teleport(x+15,y)
        fillcolor(c)
        begin_fill()
        circle(15)
        end_fill()
    return None

def porte_fenetre(x,y):
    porte(x,y,(255,255,255))
    rectangle(x-5,y-5,40,25,"brown")
    for i in range(4):
        rectangle(x+7.5*i,y-2,5,19,(255,255,255))
    return None

def porte(x,y,c=(10,10,10)):
    if 0 == randint(0,1):
        rectangle(x,y,30,50,c)
    else:
        fillcolor(c)
        begin_fill()
        teleport(x+15,y+25)
        circle(15)
        end_fill()
        teleport(x,y)
        begin_fill()
        goto(x,y+40)
        penup()
        goto(x+30,y+40)
        pendown()
        goto(x+30,y)
        goto(x,y)
        end_fill()

    return None

def cheminée(x,y):
    rectangle(x+10,y,5,12,(255,0,0))
    rectangle(x+8,y+12,9,5,(255,0,0))
    return None

def etage(x,y,c,ins,i,j):
    rectangle(x,y,140,60,c)
    for k in range(3):
        if k not in ins[i][j] : fenetre(x+15+40*k,y+20)
        elif j == 0: porte(x+15+40*k,y)
        else : porte_fenetre(x+15+40*k,y)
    return None

def toit(x,y):
    cheminée(x,y)
    pensize(5)
    fillcolor("black")
    begin_fill()
    if 0 == randint(0,1):
        rectangle(x,y,140,0,(0,0,0))
    else : 
        teleport(x,y)
        goto(x+140,y)
        goto(x+70,y+30)
        goto(x,y)
    end_fill()
    pensize(0)
    return None

def immeuble(x,y,c,ins,i):
    for j in range(len(ins[i])):
        etage(x,y+60*j,c,ins,i,j)
    toit(x,y+len(ins[i])*60)
    return None

def quartier(x,y,c,ins):
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
    quartier(-320,-180,c,ins)
    return None


initialisation()
done()