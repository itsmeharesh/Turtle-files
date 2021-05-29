import turtle
col = ['red', 'yellow','green','cyan','pink','white']
t = turtle.Turtle()
Screen = turtle.Screen()
Screen.bgcolor('black')
t.speed(5)

for i in range(150):
    t.color(col[i%6])
    t.forward(i*15)
    t.left(50)
    t.width(3)
