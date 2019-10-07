from turtle import *
from random import randrange
from UtilitiesUsedForGames import square, vector

Food = vector(0, 0)
Snake = [vector(10, 0)]
Aim = vector(0, -10)

#The snake's direction will be changed in respect to the x and y axis
def change(x, y):
    "Change the snakes direction."
    Aim.x = x
    Aim.y = y

def inside(Head):
    "Return True only if head is inside the boundaries."
    return -200 < Head.x < 190 and -200 < Head.y < 190

#The snake's movement
def move():
    "move the snake forward one segment at a time."
    Head = Snake[-1].copy()
    Head.move(Aim)

    if not inside(Head) or Head in Snake:
        square(Head.x, Head.y, 9, 'yellow')
        update()
        return

    Snake.append(Head)
#The simulation of the snake eating
    if Head == Food:
        print('Snake:', len(Snake))
        Food.x = randrange(-15, 15) * 10
        Food.y = randrange(-15, 15) * 10
    else:
        Snake.pop(0)

    clear()

    for Body in Snake:
        square(Body.x, Body.y, 9, 'blue')

    square(Food.x, Food.y, 9, 'purple')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

#Keyboard Controls
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
