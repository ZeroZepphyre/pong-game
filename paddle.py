from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, starting_x):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.moving = 10
        self.goto(x=starting_x, y=0)
        self.speed = 0.5
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.move_up()

    def move(self):
        self.goto(x=self.xcor(), y=self.ycor() + self.moving*self.speed)

    def move_up(self):
        self.moving = 10

    def move_down(self):
        self.moving = -10



