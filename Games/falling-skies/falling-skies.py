#Falling Skies in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import random
import os

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling Skies by @TokyoEdTech")
wn.bgcolor("green")
wn.bgpic("./img/background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("./img/deer_left.gif")
wn.register_shape("./img/deer_right.gif")
wn.register_shape("./img/hunter.gif")
wn.register_shape("./img/nut.gif")

#Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("./img/deer_right.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Create a list of good guys
good_guys = []

# Add the good_guys
for i in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("./img/nut.gif")
    good_guy.color("blue")
    good_guy.penup()
    x = random.randint(-380, 380)
    y = random.randint(300, 400)
    good_guy.goto(x, y)
    good_guy.speed = random.randint(1, 5)
    good_guys.append(good_guy)

# Create a list of bad guys
bad_guys = []

# Add the bad_guys
for i in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("./img/hunter.gif")
    bad_guy.color("red")
    bad_guy.penup()
    x = random.randint(-380, 380)
    y = random.randint(300, 400)
    bad_guy.goto(x, y)
    bad_guy.speed = random.randint(1, 5)
    bad_guys.append(bad_guy)

# Make the score pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

# Make the end of game message pen
scorePen = turtle.Turtle()
scorePen.hideturtle()
scorePen.speed(0)
scorePen.shape("square")
scorePen.color("white")
scorePen.penup()
scorePen.goto(0, 0)
font = ("Courier", 24, "normal")

# Functions
def go_left():
    player.direction = "left"
    player.shape("./img/deer_left.gif")

def go_right():
    player.direction = "right"
    player.shape("./img/deer_right.gif")

# Keybboard binding
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

# Main game loop
while lives > 0:
    #update screen
    wn.update()

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 5
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 5
        player.setx(x)
    
    if player.xcor() < -390:
        player.direction = "right"

    if player.xcor() > 390:
        player.direction = "left"

    #Move the good guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed      
        good_guy.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)

        # Check for a collision with the player
        if good_guy.distance(player) < 40:
            os.system("afplay ./sounds/power-up.wav&")
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
            

    #Move the bad guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed      
        bad_guy.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)

        # Check for a collision with the player
        if bad_guy.distance(player) < 40:
            os.system("afplay ./sounds/shotgun.wav&")
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

else:
    scorePen.clear()
    scorePen.write("GAME OVER!", align="center", font=font)
    print("The game is over!")


wn.mainloop()