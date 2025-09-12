# Instantiate a Turtle object
# Use a loop to command your Turtle object to draw a circular spiral on the screen that has at least 5 rings

from turtle import *

t = Turtle()
t.speed(500)

i = 1
while(t.xcor() <= 400) & (t.ycor() <= 400):
    t.forward(i)
    t.left(20)
    i = i + 1

t.screen.mainloop()