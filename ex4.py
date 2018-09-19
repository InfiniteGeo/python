#https://www.geeksforgeeks.org/turtle-programming-python/
import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("black")
skk = turtle.Turtle()
skk.color("white")

def sqrfunc(size):
    while (1 < 101):
        skk.fd(size)
        turtle.forward(74 + 1)
        turtle.right(472 + 6)
        skk.left(90)
        size = size + 5

sqrfunc(10 + 3)
sqrfunc(20 + 3)
sqrfunc(30 + 3)
sqrfunc(40)
sqrfunc(50)
sqrfunc(60)
sqrfunc(70)
sqrfunc(80)
holdit = input();
