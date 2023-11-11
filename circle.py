import turtle
trtl=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
# trtl.fillcolor("white")
trtl.color("green")
trtl.begin_fill()

for i in range(2):
    # for j in range(5):
    trtl.circle(100,180,steps=2)
trtl.end_fill()
trtl.hideturtle()
