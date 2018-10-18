#Turtlegraphics.py Jerry

import tkinter as tk
import turtle


def outloop(t,angle):
    for i in range (1,11):
        t.color("#7700dd")
        t.forward(30)
        t.right(angle)

def backloop(t,angle):
    t.width(12)
    t.color("#7700dd")
    for i in range (20,4,-1):
        t.forward(-15)
        t.left(angle)

def poly(t,size,x,y,color):
    t.width(10)
    t.penup(100)
    t.goto(10,15)
    t.pendown()
    t.color(color)
    for i in range (1,31):
        t.forward(size)
        t.right(1)

def myperro():
    tw = turtle.Screen()
    tw.clear()
    t = turtle.Turtle()
    t.width(10)
    # *******************
    t.speed(5)
    t.goto(-150,-100)
    t.color("#0f0e00")
    outloop(t,0)
    # *******************
    t.width(10)
    t.goto(-120,-100)
    t.color("#7700dd")
    backloop(t,12)
    t.goto(10,10)
    t.goto(2,1)
    t.forward(10)

    tw.exitonclick()

myperro()
