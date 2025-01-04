import turtle
import time
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Snake body
segments = []

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Speed
speed = 0.1

# Functions to control the snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Check for collision with food
def check_food_collision():
    if head.distance(food) < 20:
        # Move food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Speed up the game
        global speed
        speed *= 0.9

# Check for collision with wall or self
def check_collision():
    # Check for collision with wall
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        return True

    # Check for collision with self
    for segment in segments:
        if segment.distance(head) < 20:
            return True
    return False

# Update the segments' position
def move_segments():
    # Move the segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment to the head's position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

# Main game loop
def game_loop():
    # Update the screen
    screen.update()

    # Check for food collision
    check_food_collision()

    # Move the snake
    move_segments()
    move()

    # Check for collisions
    if check_collision():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset speed
        global speed
        speed = 0.1

    # Call the game loop again after a delay
    screen.ontimer(game_loop, int(speed * 1000))

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Start the game loop
game_loop()

# Main loop
screen.mainloop()
