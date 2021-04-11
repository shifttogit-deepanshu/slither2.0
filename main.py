import turtle
import random


screen = turtle.Screen()

dh = turtle.Turtle()

food = turtle.Turtle()

food.shape("square")
food.color("red")
food.speed(1000)
dh.shape("square")

dh.penup()
food.penup()

def setFood():
    food.hideturtle()
    food.setpos(random.randint(-screen.window_width()/2,screen.window_width()/2),random.randint(-screen.window_height()/2,screen.window_height()/2))
    food.showturtle()

setFood()


def moveUp():
    dh.forward(2)
    dh.setheading(90)
    setFood()


def moveRight():
    dh.forward(2)
    dh.setheading(0)
    setFood()


def moveLeft():
    dh.forward(2)
    dh.setheading(180)
    setFood()


def moveDown():
    dh.forward(2)
    dh.setheading(270)
    setFood()


screen.onkeypress(moveRight, "Right")


screen.onkeypress(moveUp, "Up")


screen.onkeypress(moveLeft, "Left")


screen.onkeypress(moveDown, "Down")

screen.listen()

while True:
    dh.forward(5)



screen.exitonclick()