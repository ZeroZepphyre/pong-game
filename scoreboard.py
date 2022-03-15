from turtle import Turtle
FONT = ('Courier', 40, 'normal')
ALIGNMENT = 'center'





class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.speed('fastest')
        self.shape('square')
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.refresh()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('Game Over!', move=False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.goto(0, -250)
        self.clear()
        self.draw_line()
        self.goto(x=-40, y=180)
        self.write(f'{self.l_score}', move=False, align=ALIGNMENT, font=FONT)
        self.goto(x=40, y=180)
        self.write(f'{self.r_score}', move=False, align=ALIGNMENT, font=FONT)

    def draw_line(self):
        self.pen(pensize=5)
        while self.ycor() < 250:
            self.setheading(90)
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)

    def l_point(self):
        self.l_score += 1
        self.refresh()

    def r_point(self):
        self.r_score += 1
        self.refresh()