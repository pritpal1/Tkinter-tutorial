import turtle
tt= turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("blue")
wn.title("Turtle")
tt.color("white")
def sqr(size):
    for i in range(4):
        tt.fd(size)
        tt.left(90)
        size=size-5
sqr(146)
sqr(126)
sqr(106)
sqr(86)
sqr(66)
sqr(46)
sqr(26)

turtle.done()
