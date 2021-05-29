import turtle
sc = turtle.Screen()
sc.setup(600,600)
spiral = turtle.Turtle()
spiral.speed(10)
sc.bgcolor("black")
color = ('pink','blue','red','purple')
c=0
for i in range(80):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(color[c])
    if c==3:
        c=0
    else:
        c+=1
