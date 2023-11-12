import turtle
tr=turtle.Turtle()
tr.color("White")
wn=turtle.Screen()
wn.bgcolor("black")
tr.speed(2)
tr.begin_fill()
tr.fillcolor("green")
for i in range(4):
    tr.forward(100)
    tr.left(90)
tr.end_fill()
tr.hideturtle()
