from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

ball = Ball(0, 0)

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

screen.exitonclick()