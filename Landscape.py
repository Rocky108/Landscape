import turtle

g = turtle.Turtle()

g.pu()
g.speed(100000000000000000)
g.right(90)
g.forward(150)
g.right(90)
g.pd()
g.begin_fill()
g.fillcolor("forestgreen")
g.forward(500)
g.left(90)
g.forward(200)
g.left(90)
g.forward(1000)
g.left(90)
g.forward(200)
g.left(90)
g.forward(500)
g.end_fill()

s = turtle.Turtle()
s.speed(1000000000000000)
s.right(90)
s.pu()
s.forward(150)
s.right(90)
s.pd()
s.begin_fill()
s.fillcolor("skyblue")
s.forward(500)
s.right(90)
s.forward(1000)
s.right(90)
s.forward(1000)
s.right(90)
s.forward(1000)
s.right(90)
s.forward(500)
s.end_fill()

t = turtle.Turtle()

t.speed(1000000000000)
t.right(90)
t.pu()
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.pd()
t.right(90)
t.begin_fill()
t.fillcolor("darkolivegreen")
t.left(90)
t.forward(70)
t.right(110)
t.forward(50)
t.left(150)
t.forward(75)
t.right(150)
t.forward(50)
t.left(150)
t.forward(75)
t.right(150)
t.forward(50)
t.left(150)
t.forward(100)
t.left(94)
t.forward(100)
t.left(150)
t.forward(50)
t.right(150)
t.forward(75)
t.left(150)
t.forward(50)
t.right(150)
t.forward(75)
t.left(150)
t.forward(50)
t.right(104)
t.forward(73)
t.end_fill()
t.begin_fill()
t.fillcolor("brown")
t.back(70)
t.forward(70)
t.left(90)
t.forward(54)
t.left(90)
t.forward(70)
t.left(90)
t.forward(54)
t.end_fill()

h = turtle.Turtle()

h.pu()
h.right(90)
h.forward(175)
h.left(90)
h.pd()
h.begin_fill()
h.fillcolor("firebrick")

def square():
    for i in range(4):
        h.forward(300)
        h.left(90)
square()
h.end_fill()

t.pu()
t.goto(-10000,-10000)
g.pu()
g.goto(-10000,-10000)
s.pu()
s.goto(-10000,-10000)

h.forward(140)
h.left(90)
h.forward(75)
h.right(90)
h.forward(50)
h.right(90)
h.forward(75)


turtle.exitonclick()