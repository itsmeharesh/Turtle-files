import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)

while (True):
    for i in range(6):
        for colors in ['red', 'pink', 'yellow', 'pink', 'magenta', 'white']:
            turtle.color(colors)
            turtle.circle(150)
            turtle.right(5)


turtle.hideturtle()
turtle.mainloop()
