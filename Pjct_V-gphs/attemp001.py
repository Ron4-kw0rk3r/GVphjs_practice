import turtle as tt
from turtle import *








def myone():
    exa = tt.Turtle()
    a = tt.getscreen()
    showturtle()
    screen = tt.Screen()
    screen.bgcolor("black")    
    exa.speed(1)
    #a = exa.getscreen()
    # pen is module  pen control status control graphics  
    # tt = turtle.Turtle()
    for z in range(5):
        exa.color("green")
        exa.left(10)
        exa.forward(110)
        exa.goto(10,10)
        exa.right(15)
        #exa.up()
        for lap in range(10):
            exa.color("cyan")
            #exa.penup()
            exa.forward(100)
            exa.right(40)
            exa.forward(100)
            exa.goto(10,10)
            #return z 
            #exa.penup()
            # for jobs in range(20):
                # exa.color("yellow")
                # exa.forward(100)
                # exa.right(40)
                # exa.forward(100)
                # #exa.goto(10, 10)
    # tt.down()
    # tt.forward(200)
    # tt.left(90)
    # tt.forward(200)
    #exa.right(100)
    #exa.forward(100)
    #exa.pendown(15)
    #exa.left(40)
    mainloop()
if __name__ == "__main__":
    myone()
      
        


