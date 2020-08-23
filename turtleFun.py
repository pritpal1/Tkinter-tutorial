import turtle
color=["red","blue","green","purple","yellow","pink"]
pen=turtle.Pen()
turtle.bgcolor("black")
for x in range(100):
    pen.pencolor(color[x % 6])
    pen.width(x/100 + 1)
    pen.forward(x)
    pen.left(59)
turtle.done()