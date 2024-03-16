import turtle
# Produced by ~ Jayakumar K

pen = turtle.Turtle()
turtle.speed(3)
turtle.shapesize=-500
turtle.shapesize=500


def curve():
    
    for i in range(201):
        pen.right(1)
        pen.forward(1)
def clear():
    for i in range(5):
        pen.circle("draw")

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def text1():
    pen.up()
    pen.setpos(-85, 95)
    pen.down()
    pen.color('yellow')
    pen.write("       i love you", font=("italic", 16, "normal"))

heart()
text1()

pen.hideturtle()

turtle.done()
