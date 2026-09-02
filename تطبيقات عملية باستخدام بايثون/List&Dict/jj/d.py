import turtle

t=turtle.Turtle()

for i in range(2):
    t.forward(100)
    t.lt(90)
    t.fd(30)
    t.left(90)
t.penup()
t.goto(0,60)
t.pendown()
for i in range(2):
    t.forward(100)
    t.lt(90)
    t.fd(30)
    t.left(90)
t.penup()
t.goto(0,30)
t.pendown()
for i in range(2):
    t.pencolor("white")

    t.forward(100)
    t.lt(90)
    t.fd(30)
    t.left(90)