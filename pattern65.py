import tkinter as tk
import turtle

def star(t,x,y):
    t.goto(x,y)
    for angle in range (0,360,15):
        t.color("#ff0000")
        t.width(5)
        t.forward(50)
        t.color("#ffff00")
        t.width(1)
        t.back(50)
        t.right(angle)


def gman():
    tw = turtle.Screen()
    tw.clear()
    t = turtle.Turtle()
    t.width(3)
    # *******************
    xlist = [-10,20,50,90,-100,300,-300]
    ylist = [5,  0,-40,4,  40, -30, 5]
    tcolor = ["#ff0000","#00ff00","#0000ff","#ffff00","#00ffff","#ff00ff",]
    t.speed(5)
    t.pendown()
    t.goto(xlist[0],ylist[0])
    t.goto(xlist[1],ylist[1])
    done = 0
    x= 0
    addvalue = 1
    while  (done == 0):
        print(x,addvalue)
        t.color(tcolor[x - 1 - 1])
        t.goto(xlist[x - 1],ylist[x - 1])
        x = x + addvalue
        if (x > 6):
                addvalue = addvalue * -1
        if (x < 0):
                addvalue = addvalue * -1
    tw.exitonclick()

gman()


"""
apt-cache search tkinter | more
apt install python3-tk python-tk
"""
