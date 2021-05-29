import turtle
hand=turtle.Turtle()
hand.speed(10)
window=turtle.Screen()
window.bgcolor("white")
colors=('red','green','orange','yellow','blue','indigo','violet')
size=300
hand.penup()
hand.goto(250,-300)
hand.pendown()
for i in range(7):
    hand.color(colors[i])
    hand.fillcolor(colors[i])
    hand.begin_fill()
    hand.circle(size)
    hand.end_fill()
    size -=20
hand.hideturtle()
turtle.done()
