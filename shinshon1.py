from turtle import *
s=Screen()
s.screensize(700,1000)
speed(5)
def myposition(x,y):
    penup()
    goto(x,y)
    pendown()
pensize(2)
def ankur():
    fillcolor('green')
    begin_fill()
    right(25)
    forward(20)
    right(45)
    forward(20)
    left(70)
    forward(90)
    left(95)
    forward(75)
    left(85)
    forward(175)
    left(85)
    forward(75)
    left(85)
    forward(90)
    left(85)
    forward(18)
    end_fill()
    
def leftLeg():
    myposition(-39,-25)
    fillcolor('red')
    begin_fill()
    right(89)
    forward(25)
    right(90)
    forward(50)
    right(90)
    forward(20)
    right(85)
    forward(50)
    end_fill()
    
def leftSock():
    myposition(-36,-78)
    fillcolor('#ffffff')
    begin_fill()
    right(90)
    circle(80,13)
    right(110)
    forward(22)
    right(85)
    forward(19)
    right(90)
    forward(21)
    end_fill()
    
def leftShoe():
    myposition(-69,-112)
    fillcolor("pink")
    begin_fill()
    right(90)
    left(5)
    forward(56)
    left(105)
    forward(13)
    left(75)
    forward(20)
    right(90)
    forward(15)
    circle(10,15)
    left(80)
    forward(4)
    circle(10,15)
    left(40)
    circle(20,15)
    forward(10)
    right(45)
    forward(15)
    end_fill()
    
def rightLeg():
    myposition(60,-28)
    fillcolor("red")
    begin_fill()
    left(128)
    forward(25)
    right(95)
    forward(55)
    right(90)
    forward(20)
    right(85)
    forward(55)
    end_fill()

def rightSock():
    myposition(64,-79)
    fillcolor("#ffffff")
    begin_fill()
    right(90)
    circle(90,14)
    right(110)
    forward(23)
    right(90)
    forward(15)
    right(80)
    forward(21)
    end_fill()
    
def rightShoe():
    myposition(64,-108)
    fillcolor("cyan")
    begin_fill()
    right(100)
    forward(56)
    left(160)
    forward(25)
    right(68)
    forward(17)
    left(90)
    circle(18,15)
    forward(5)
    left(75)
    forward(11)
    right(85)
    forward(20)
    left(45)
    circle(10,30)
    left(25)
    forward(5)
    end_fill()

def myShirt():
    myposition(-75,48)
    fillcolor("red")
    begin_fill()
    left(72)
    forward(185)
    left(87)
    forward(75)
    right(68)
    circle(20,8)
    circle(300,23)
    left(90)
    circle(35,17)
    right(38)
    circle(35,17)
    left(58)
    forward(75)
    right(12)
    forward(140)
    right(40)
    forward(93)
    left(120)
    circle(-20,65)
    left(23)
    forward(88)
    right(31)
    forward(87)
    right(180)
    forward(108)
    right(180)
    forward(104)
    circle(10,70)
    end_fill()

def myHead():
    myposition(-20,295)
    left(20)
    pensize(2)
    fillcolor("yellow")
    begin_fill()
    right(90)
    forward(40)
    right(90)
    circle(50,80)
    left(10)
    circle(50,80)
    left(2)
    circle(200,50)

    
    left(48)
    forward(60)
    circle(45,60)
    right(5)
    circle(100,85)
    end_fill()
    fillcolor('black')
    begin_fill()
    
    pensize(2)
    right(170)
    circle(-100,165)
    right(78)
    forward(26)
    right(87)
    forward(55)
    circle(45,60)
    right(5)
    circle(100,85)
    end_fill()

    
    fillcolor("yellow")
    begin_fill()
    right(180)
    circle(-100,105)
    right(37)
    forward(49)
    pensize(2)
    left(130)
    forward(30)
    circle(-10,70)
    right(50)
    forward(36)
    right(80)
    forward(50)
    pencolor("yellow")
    right(90)
    forward(30)
    end_fill()

def rightHand():
    myposition(197,209)
    pencolor("black")
    fillcolor('red')
    begin_fill()
    right(45)
    forward(6)
    left(55)
    forward(20)
    circle(-5,70)
    right(100)
    forward(18)
    left(105)
    forward(18)
    circle(-5,70)
    right(100)
    forward(18)
    left(145)
    forward(15)
    circle(-5,70)
    right(100)
    forward(18)
    
    left(150)
    forward(13)
    circle(-5,70)
    right(100)
    forward(15)
    
    left(150)
    forward(10)
    circle(-5,70)
    right(100)
    forward(12)
    circle(60,10)
    left(45)
    forward(6)
    right(90)
    forward(10)
    end_fill()

def leftHand():
    myposition(-94,242)
    fillcolor("green")
    begin_fill()
    right(10)
    forward(6)
    left(90)
    penup()
    forward(12)
    pendown()
    left(90)
    forward(8)
    left(90)
    forward(12)
    end_fill()


def myBis():
    myposition(-103,291)
    right(90)
    fillcolor("green")
    begin_fill()
    right(90)
    forward(55)
    left(80)
    forward(12)
    left(10)
    forward(17)
    left(10)
    forward(12)
    left(80)
    forward(55)
    left(80)
    forward(12)
    left(10)
    forward(17)
    left(10)
    forward(12)
    left(80)
    left(80)
    forward(12)
    left(10)
    forward(17)
    left(10)
    forward(12)
    end_fill()
    penup()
    right(100)
    forward(20)
    right(90)
    forward(14)
    pendown()
    pencolor("blue")
    fillcolor("blue")
    begin_fill()
    for i in range(5):
        forward(15)
        right(144)
    end_fill()
    penup()
    forward(27)
    left(90)
    forward(16)
    left(90)
    forward(7)
    pendown()
    fillcolor('pink')
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()
    penup()
    forward(20)
    right(90)
    forward(5)
    pendown()
    fillcolor("cyan")
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()
    penup()
    right(180)
    forward(6)
    pendown()
    fillcolor("red")
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()

def leftHand2():
    myposition(-112,284)
    pencolor('black')
    fillcolor("pink")
    begin_fill()
    right(180)
    forward(31)
    left(90)
    for i in range(2):
        circle(4,90)
    for i in range(3):
        right(180)
        for i in range(2):
            circle(4,90)
    end_fill()


def myMouth():
    myposition(-25,200)
    left(65)
    fillcolor("orange")
    begin_fill()
    for i in range(2): 
        circle(25,90)
        circle(25//2,90)
    end_fill()

def myEyebrow(x,y):
    myposition(x,y)
    pensize(18)
    right(150)
    forward(25)
    right(90)
    for i in range(1):
        right(45)
        dot(15)
    left(55)
    forward(25)
    for i in range(1):
        right(45)
        dot(15)

def myEyelid(x,y):
    myposition(x,y)
    pensize(2)
    left(170)
    circle(-23,180)

def myallEyes1(x,y):
    myposition(x,y)
    right(90)
    fillcolor("green")
    begin_fill()
    circle(18)
    end_fill()
    left(90)
    penup()
    forward(19)
    right(90)
    forward(7)
    pendown()
    fillcolor("red")
    begin_fill()
    left(90)
    circle(9)
    end_fill()

def myallEyes2(x,y):
    myposition(x,y)
    right(90)
    fillcolor("purple")
    begin_fill()
    circle(18)
    end_fill()
    left(90)
    penup()
    forward(19)
    right(90)
    forward(8)
    pendown()
    fillcolor("red")
    begin_fill()
    left(90)
    circle(9)
    end_fill()

def myRobot():
    myposition(155,-105)
    left(93)
    color("red")
    pensize(7)
    
    begin_fill()
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    end_fill()
    
    color("green")
    penup()
    left(90)
    forward(30)
    right(90)
    forward(12)
    pendown()
    pensize(3)
    circle(5)
    penup()
    forward(25)
    pendown()
    circle(5)
    
    penup()
    right(90)
    forward(20)
    right(90)
    pendown()
    
    begin_fill()
    forward(23)
    right(90)
    forward(7)
    right(90)
    forward(23)
    right(90)
    forward(7)
    right(90)
    end_fill()

    
    penup()
    forward(25)
    right(90)
    forward(35)
    pendown()
    
    color('red')
    forward(30)
    penup()
    right(90)
    pendown()
    begin_fill()
    circle(5)
    end_fill()

def allLegs():
    leftLeg()
    leftSock()
    leftShoe()
    rightLeg()
    rightSock()
    rightShoe()

def allHands():
    rightHand()
    leftHand()
    myBis()
    leftHand2()
def allEyebrows():
    myEyebrow(-8,300)
    right(90)
    myEyebrow(72,300)
    myEyelid(-9,270)
    left(15)
    myEyelid(68,265)
def allEyes():
    myallEyes1(17,275)
    myallEyes2(95,270)
    
def my_goto(x,y):
    penup()
    goto(x,y)
    pendown()

ankur()
allLegs()
myShirt()
myHead()
allHands()
myMouth()
allEyebrows()
allEyes()
myRobot()
ht()

my_goto(-200,-250)
done()
