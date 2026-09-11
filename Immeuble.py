from turtle import *
from random import random



for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    right(angle)
    fd(steps)


done()