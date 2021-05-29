import turtle
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
t.speed(0)
screen.setup(700,700)
col=('yellow','red','cyan','purple')
for a in range(450):
    t.pencolor(col[a%4])
    t.width(2)
    t.forward (a)
    t.right(89)
    t.forward(a*2)
    t.right(89)
    
