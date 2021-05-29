import turtle
b = turtle.Turtle()
b.getscreen().bgcolor("black")
b.penup()
b.goto(-200,100)
b.pendown()
b.color("yellow")
b.speed(25)
def star(turtle, size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
            turtle.end_fill()
star(b,360)
turtle.done()
