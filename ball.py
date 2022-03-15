from turtle import Turtle
from random import randint, choice
import time
COLLISION = False
BALL_SPEED = 0.4
class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.color('white')
        self.shape('circle')
        self.penup()
        self.move_y = 10
        self.move_x = 10
        self.ball_speed = BALL_SPEED
        self.angle = 0

    def bounce(self, is_wall):
        if is_wall:
            self.move_y *= -1
        if not is_wall:
            self.move_y *= choice((-1, 1))
            self.move_x *= -1

    def move(self):
        x = self.xcor() + self.move_x * self.ball_speed
        y = self.ycor() + self.move_y * self.ball_speed
        self.goto(x, y)

    def scored(self):
        self.ball_speed = BALL_SPEED
        self.goto(0, 0)
        self.move_x *= -1