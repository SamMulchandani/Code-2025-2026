# Instantiate a Turtle object
# Use a loop to command your Turtle object to draw a zigzag across the screen

from turtle import *

t = Turtle()
print(t.screen.screensize())
t.teleport(-400,-400)
t.speed(799)
t.left(90)

while(t.xcor() <= 400) & (t.ycor() <= 300):
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)

t.screen.mainloop()