
#!/urs/bin/python3.8

import turtle as tt
from turtle import *
import sys
import random
from sys import stdin
import time
from random import randint as rand 
import math

# el orden de los factores si altera el producto 


colors =[

    '#FFFFFF' , '#F01bc4',
    '#000000' , '#11E511',
    '#1bc3F7' , '#1e1f11',
    '#0bc3F7' , '#4575fa',
    '#1bc3F7' , '#c63c55',
    '#1bF722' , '#00ce11',
    '#11c0F7' , '#F0000F'
    
]



def figures( vect_a, vect_b, vect_c, vect_d ):
    
    func = tt.Turtle()
    screen = tt.Screen()

    func.speed(1)
    # operators native 
    showturtle()
    screen.bgcolor("#000011") # obscure color down black 
    yambl = lambda x : x + 89 / math.pi
    func.color('#014Fc1')
    func.right(10)
    # func.forward(vect_a + 89)
    func.forward(vect_a + 89)
    func.down()
    func.left(yambl(vect_b))
    func.color('#FF0000')
    func.right(180)
    #func.up()
    func.forward(100)
    func.left(45)
    func.forward(yambl(vect_b))
    #func.left(lambda vect_b : vect_b + 109)
    
    func.goto(10,10)

# command is better use  command blocks  make build vector and create data    

    mainloop()



def shampes(vectv ,  vectx , vecty , vectz):
    
    pass


if __name__ == "__main__" :
    figures( int(10), 10, int(10), 10 )
    # print(lambda x ; x + 99 / math.pi)
    #print(yambl(10))
