import turtle as t
t.bgcolor("red")
color =['VIOLET','#4b0082','green','yellow','blue','orange','pink']
t.speed(0)

for i in range(280):
    t.pencolor(color[i%7])
    t.pensize(2)
    t.forward(i)
    t.left(59)
t.done()
