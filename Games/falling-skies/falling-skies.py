#Falling Skies in Python 3 for Beginners
# By @TokyoEdTech

import turtle

wn = turtle.Screen()
wn.title("Falling Skies by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=800, height=600)

#Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

# Main game loop
while True:

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)




wn.mainloop()