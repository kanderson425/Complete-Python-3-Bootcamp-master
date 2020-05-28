#Falling Skies in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import random

wn = turtle.Screen()
wn.title("Falling Skies by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=800, height=600)
# wn.tracer(0)

#Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

#Add the good_guy
good_guy = turtle.Turtle()
good_guy.speed(0)
good_guy.shape("circle")
good_guy.color("blue")
good_guy.penup()
good_guy.goto(0, 250)

# Functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

# Keybboard binding
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

# Main game loop
while True:
    #update screen
    wn.update()

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    #Move the good guy
    y = good_guy.ycor()
    y -= 10
    good_guy.sety(y)
    # good_guy.sety(good_guy.ycor() - 3)

    # Check if off the screen
    if y < -300:
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        good_guy.goto(x, y)

    # Check for a collision with the player
    if good_guy.distance(player) < 20:
        x = random.randint(-380, 380)
        y = random.randint(300, 400)
        good_guy.goto(x, y)


wn.mainloop()