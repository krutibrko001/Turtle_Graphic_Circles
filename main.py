from turtle import Turtle, Screen
from random import choice, randint


screen = Screen()
turtle = Turtle()
turtle.speed(0)
turtle.pensize(1)
turtle.hideturtle()
screen.colormode(255)

def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_col = (r, g, b)
    return random_col

plus_count = 200


for i in range(plus_count):
    turtle.color(rand_color())
    turtle.tilt(i)
    turtle.forward(1)
    turtle.right(10)
    turtle.circle(i)
    plus_count -= 1
    if plus_count == 0:
        for element in range(200):
            turtle.color(rand_color())
            turtle.tilt(element-1)
            turtle.forward(10)
            turtle.right(10)
            turtle.circle(i)

print("test")




screen.exitonclick()
