import random
import time
import keyboard
import turtle
from turtle import Turtle


turtles = []
colors = ['khaki', 'aquamarine', 'springgreen', 'salmon']
press_start_turtle = turtle.Turtle()
winner_turtle = turtle.Turtle()


def set_turtles():
    global turtles
    for t in turtles:
        t.clear()
        t.reset()
        del t
    turtles.clear()
    for i in range(4):
        new_turtle = Turtle()
        new_turtle.speed(0)
        new_turtle.color(colors[i])
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.goto(-250, 100 - i * 50)
        new_turtle.pendown()
        turtles.append(new_turtle)


def screen_setup():
    title_turtle = turtle.Turtle()
    title_turtle.hideturtle()
    title_turtle.color('white')
    title_turtle.speed(0)
    title_turtle.penup()
    title_turtle.sety(200)
    title_turtle.write('turtle race', align='center', font=('Calibri', 30, 'normal'))
    title_turtle.penup()

    global press_start_turtle
    press_start_turtle.speed(0)
    press_start_turtle.hideturtle()
    press_start_turtle.penup()
    press_start_turtle.setpos(-125, 175)
    press_start_turtle.color('white')
    press_start_turtle.write('PRESS SPACE TO START', 'erasable', font=('Calibri', 20, 'normal'))

    stamp_size = 20
    square_size = 25
    finish_line_len = 200

    finish_turtle = turtle.Turtle()
    finish_turtle.color('white')
    finish_turtle.shape('square')
    finish_turtle.shapesize(square_size / stamp_size)
    finish_turtle.penup()

    for finish_line_index in range(10):
        finish_turtle.setpos(finish_line_len, (150 - (finish_line_index * square_size)))
        finish_turtle.stamp()

    finish_turtle.hideturtle()


def countdown():
    global winner_turtle
    winner_turtle.clear()
    winner_turtle.reset()
    time.sleep(1)
    global press_start_turtle
    press_start_turtle.clear()
    countdown_turtle = turtle.Turtle()
    countdown_turtle.speed(0)
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.setpos(-45, 175)
    countdown_turtle.color('white')

    count = 3
    while count != 0:
        countdown_turtle.write(count, 'erasable', font=('Calibri', 20, 'normal'))
        time.sleep(1)
        countdown_turtle.clear()
        count -= 1
    countdown_turtle.write('GO!', 'erasable', font=('Calibri', 20, 'normal'))
    time.sleep(1)
    countdown_turtle.clear()


def race():
    win = False
    global winner_turtle
    global turtles
    while not win:
        for index, one_turtle in enumerate(turtles):
            one_turtle.forward(random.uniform(1.0, 5.5))
            if one_turtle.xcor() >= 200:
                win = True
                winner_turtle.speed(0)
                winner_turtle.hideturtle()
                winner_turtle.penup()
                winner_turtle.sety(-150)
                winner_turtle.color('white')
                winner_turtle.write(f'The winner is {colors[index].upper()} turtle!',
                                    'erasable', align='center', font=('Calibri', 20, 'normal'))
                break


if __name__ == '__main__':
    window = turtle.Screen()
    window.title('TURTLE RACE')
    window.bgcolor('black')
    screen_setup()
    while True:
        if keyboard.is_pressed('space'):
            set_turtles()
            countdown()
            race()
        elif keyboard.is_pressed('escape'):
            break
