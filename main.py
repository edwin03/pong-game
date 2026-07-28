from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

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
    time.sleep(ball.move_speed)

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x() 

    if ball.xcor() >= 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() <= -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()