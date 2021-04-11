import turtle

screen = turtle.Screen()

dh = turtle.Turtle()

dh.shape("square")

dh.penup()


def moveUp():
    dh.setheading(90)
    dh.forward(2)

def moveRight():
    dh.setheading(0)
    dh.forward(2)

def moveLeft():
    dh.setheading(180)
    dh.forward(2)

def moveDown():
    dh.setheading(270)
    dh.forward(2)

screen.onkeypress(moveRight, "Right")


screen.onkeypress(moveUp, "Up")


screen.onkeypress(moveLeft, "Left")


screen.onkeypress(moveDown, "Down")

screen.listen()

while True:
    dh.forward(2)





screen.exitonclick()