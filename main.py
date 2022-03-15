from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from random import Random
from scoreboard import Scoreboard


sb = Scoreboard()
r = Random()
screen = Screen()
screen.tracer(0)
ball = Ball()
paddle1 = Paddle(starting_x = -390)
paddle2 = Paddle(starting_x = 390)
screen.setup(height=500, width=800)
screen.bgcolor('black')
screen.listen()
screen.onkeypress(paddle1.move_down, 's')
screen.onkeypress(paddle2.move_down, 'Down')
screen.onkeypress(paddle1.move_up, 'w')
screen.onkeypress(paddle2.move_up, 'Up')

isRunning = True

while isRunning:
    screen.update()
    time.sleep(0.01)
    paddle1.move()
    paddle2.move()
    ball.move()
    if ball.distance(paddle1) < 60 and ball.xcor() < -370:
        ball.bounce(False)
        ball.ball_speed *= 1.1
    if ball.distance(paddle2) < 60 and ball.xcor() > 370:
        ball.bounce(False)
        ball.ball_speed *= 1.1
    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            sb.l_point()
        elif ball.xcor() < - 400:
            sb.r_point()
        ball.scored()
        screen.update()
        time.sleep(0.5)
    if ball.ycor() < -240 or ball.ycor() > 240:
        ball.bounce(True)
    if paddle1.ycor() > 230:
        paddle1.move_down()
    if paddle2.ycor() > 230:
        paddle2.move_down()
    if paddle1.ycor() < -230:
        paddle1.move_up()
    if paddle2.ycor() < -230:
        paddle2.move_up()

screen.exitonclick()
