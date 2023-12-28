from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('white')
        self.penup()
        self.move_to_randpos()
        self.change_to_randcolor()

    def move_to_randpos(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)

    def change_to_randcolor(self):
        r = randint(0, 220)
        g = randint(0, 220)
        b = randint(0, 220)
        self.color(r, g, b)
