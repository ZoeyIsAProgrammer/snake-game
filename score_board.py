from turtle import  Turtle, Screen
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.setpos(0, 270)
        self.print_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def print_score(self):
        self.write(arg=f"Score: {self.score}", align='center', font=('Courier', 18, 'normal'))

    def print_game_over(self):
        self.setpos(0, 0)
        self.write(arg="Game Over", align='center', font=('Courier', 24, 'bold'))