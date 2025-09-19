#red triangle in the upper left
#green square in the upper right
#blue pentagon in the bottom right
from turtle import *


t_red = Turtle()
t_green = Turtle()
t_blue = Turtle()

t_red.pencolor("red")
t_green.pencolor("green")
t_blue.pencolor("blue")

t_red.teleport(-350, 225)
t_red.left(60)
t_red.forward(100)
t_red.right(120)
t_red.forward(100)
t_red.right(120)
t_red.forward(100)

t_blue.teleport(300,-250)
t_blue.right(180)
t_blue.forward(100)
t_blue.right(72)
t_blue.forward(100)
t_blue.right(72)
t_blue.forward(100)
t_blue.right(72)
t_blue.forward(100)
t_blue.right(72)
t_blue.forward(100)

t_green.teleport(350, 225)
t_green.right(180)
t_green.forward(100)
t_green.right(90)
t_green.forward(100)
t_green.right(90)
t_green.forward(100)
t_green.right(90)
t_green.forward(100)

t_red.screen.mainloop()