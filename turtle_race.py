import time
import turtle
from turtle import Turtle
from random import randint


turtles = []
colors = ['khaki', 'aquamarine', 'springgreen', 'salmon']
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
    turtle.color('white')
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-100, 200)
    turtle.write('turtle race', font=('Calibri', 30))
    turtle.penup()

    stamp_size = 20
    square_size = 25
    finish_line = 200

    turtle.color('white')
    turtle.shape('square')
    turtle.shapesize(square_size / stamp_size)
    turtle.penup()

    for finish_line_index in range(10):
        turtle.setpos(finish_line, (150 - (finish_line_index * square_size)))
        turtle.stamp()

    turtle.hideturtle()


def countdown():
    countdown_turtle = turtle.Turtle()
    countdown_turtle.speed(0)
    countdown_turtle.hideturtle()
    countdown_turtle.up()
    countdown_turtle.setpos(-50, 170)
    countdown_turtle.color('white')

    count = 3
    while count != 0:
        countdown_turtle.write(count, 'erasable', font=('Calibri', 20))
        time.sleep(1)
        countdown_turtle.clear()
        count -= 1
    countdown_turtle.write('GO!', 'erasable', font=('Calibri', 20))
    time.sleep(1)
    countdown_turtle.clear()


def race():
    win = False
    while not win:
        for index, one_turtle in enumerate(turtles):
            one_turtle.forward(randint(1, 5))
            if one_turtle.xcor() >= 200:
                winner_turtle = turtle.Turtle()
                winner_turtle.speed(0)
                winner_turtle.hideturtle()
                winner_turtle.up()
                winner_turtle.setpos(-180, -150)
                winner_turtle.color('white')
                winner_turtle.write(f'The winner is {colors[index].upper()} turtle!', font=('Calibri', 20))
                win = True
                break


def main():
    window = turtle.Screen()
    window.title('TURTLE RACE')
    window.bgcolor('black')

    screen_setup()
    countdown()
    race()

    window.mainloop()


if __name__ == '__main__':
    main()
