import turtle
import colorsys as cs
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(0)
t.pensize(2)
for i in range(25):
    for j in range(15):
        turtle.color(cs.hsv_to_rgb(j/15,i/25,1))
        turtle.right(90)
        turtle.circle(200-i*4,90)
        turtle.left(90)
        turtle.circle(200-i*4,90)
        turtle.right(180)
        turtle.circle(50,24)
turtle.hideturtle()
turtle.done()