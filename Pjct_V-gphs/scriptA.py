#!/usr/bin/python3.8



import turtle as tt
import time
ss = tt.Turtle()


ss.speed(1)
ss.color("red")
screen=tt.Screen()
screen.bgcolor("black")
def block_draw():
    for x in range(4):
        
        ss.forward(100)
        ss.right(90)

        for aa in range(4):
            ss.forward(50)
            ss.right(80)
            #ss.penup(40)
    ss.penup()  
    ss.back(200)    
    ss.pendown()


if __name__ == "__main__":
    
    for sequence in range(100):
        block_draw()
        ss.penup(5)
        ss.left(10)
        time.sleep(100)
        turtle.done()
    
    
#input('hello machine')
# turtle.show()
