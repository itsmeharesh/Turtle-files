import turtle as t


t.bgcolor("red")
t.pencolor("blue")
t.speed(0)

for i in range(150):
    for j in range(6):
        t.forward(i)
        t.left(46)
        t.hideturtle()
t.done()
