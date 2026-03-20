import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.width(2)

n = 36
h = 0

for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.pencolor(c)

    t.forward(i * 2)
    t.right(59)
turtle.done()