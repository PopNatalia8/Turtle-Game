from turtle import *
from random import *
import time

# SCREEN SETUP
setup(800, 500)
title('Turtle Race')
bgcolor('#64AD62')
speed(0)

# HEADING
penup()
goto(-100, 205)
color('white')
write('TURTLE RACE', font=('Arial', 20, 'bold'))

# DIRT
goto(-350, 200)
pendown()
color('#92664A')
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

# FINISH LINE
gap_size = 20
shape('square')
penup()

# WHITE SQUARES ROW 1
color('white')
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

# WHITE SQUARES ROW 2
color('white')
for i in range(10):
    goto(250 + gap_size, (210 - gap_size) - (i * gap_size * 2))
    stamp()

# BLACK ROW SQUARES 1
color('black')
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

# BLACK ROW SQUARES 2
color('black')
for i in range(10):
    goto(250 + gap_size, (190 - gap_size) - (i * gap_size * 2))
    stamp()

# TURTLE 1 - BLUE
blue_turtle = Turtle()
blue_turtle.color('#4169E1')
blue_turtle.shape('turtle')
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()


# TURTLE 1 - PINK
pink_turtle = Turtle()
pink_turtle.color('#FF69B1')
pink_turtle.shape('turtle')
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300, 50)
pink_turtle.pendown()

# TURTLE 1 - YELLOW
yellow_turtle = Turtle()
yellow_turtle.color('#FFF44F')
yellow_turtle.shape('turtle')
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300, -50)
yellow_turtle.pendown()


# TURTLE 1 - ORANGE
orange_turtle = Turtle()
orange_turtle.color('#FFAA1D')
orange_turtle.shape('turtle')
orange_turtle.shapesize(1.5)
orange_turtle.penup()
orange_turtle.goto(-300, -150)
orange_turtle.pendown()

# PAUSE FOR 1 SECONDS BEFORE RACING
time.sleep(1)

# MOVE THE TURTLES

while blue_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and yellow_turtle.xcor() <= 230 and orange_turtle.xcor() <= 230:
    blue_turtle.forward(randint(1, 10))
    pink_turtle.forward(randint(1, 10))
    yellow_turtle.forward(randint(1, 10))
    orange_turtle.forward(randint(1, 10))


# CELEBRATE THE WINNER

# BLUE TURTLE WINS
if blue_turtle.xcor() > pink_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor() and blue_turtle.xcor() > orange_turtle.xcor():
    print('Blue turtle wins !')
    for x in range(72):
        blue_turtle.right(5)
        blue_turtle.shapesize(4)
    for i in range(4, 120):
        blue_turtle.shapesize(i)

    penup()
    color('black')
    goto(-270, 0)
    pendown()
    write('BLUE TURTLE WINS !', font=('Arial', 40, 'bold'))

# PINK TURTLE WINS
elif pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > yellow_turtle.xcor() and pink_turtle.xcor() > orange_turtle.xcor():
    print('Pink turtle wins !')
    for x in range(72):
        pink_turtle.right(5)
        pink_turtle.shapesize(4)
    for i in range(4, 120):
        pink_turtle.shapesize(i)

    penup()
    color('black')
    goto(-280, 0)
    pendown()
    write('PINK TURTLE WINS !', font=('Arial', 40, 'bold'))


# YELLOW TURTLE WINS
elif yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > orange_turtle.xcor():
    print('Yellow turtle wins !')
    for x in range(72):
        yellow_turtle.right(5)
        yellow_turtle.shapesize(4)
    for i in range(4, 120):
        yellow_turtle.shapesize(i)

    penup()
    color('black')
    goto(-300, 0)
    pendown()
    write('YELLOW TURTLE WINS !', font=('Arial', 40, 'bold'))


# ORANGE TURTLE WINS
else:
    print('Orange turtle wins !')
    for x in range(72):
        orange_turtle.right(5)
        orange_turtle.shapesize(2.5)
    for i in range(4, 120):
        orange_turtle.shapesize(i)

    penup()
    color('black')
    goto(-300, 0)
    pendown()
    write('ORANGE TURTLE WINS !', font=('Arial', 40, 'bold'))

exitonclick()
