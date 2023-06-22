import turtle

from itertools import cycle
colors = cycle(['yellow', 'black', 'green', 'blue', 'red', 'navy'])


def draw_circle(size,angle,shift):
    turtle.bgcolor("pink")
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+7, angle+0,shift+0)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(3)
draw_circle(10,0,0)
