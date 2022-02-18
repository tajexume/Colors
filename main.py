import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color = (r, g, b)
  return color

def drawSpiro(spaceBetween):
  for _ in range(int(360/spaceBetween)):
    tim.color(random_color())
    #tim.fillcolor(random_color())
    tim.speed(0)
    #tim.begin_fill()
    tim.circle(80)
    #tim.end_fill()
    tim.setheading(tim.heading() + int (spaceBetween))
drawSpiro(5)

