from turtle import Turtle


class Snake:

    def __init__(self):
        self.turtles = []
        self.createSnake()
        self.head = self.turtles[0]

    def createSnake(self):
        for i in range(3):
            new_turtle = Turtle(shape='square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.setx(-20*i)
            self.turtles.append(new_turtle)

    def move(self):
        for tur_num in range(len(self.turtles) - 1, 0, -1):
            position = self.turtles[tur_num - 1].position()
            self.turtles[tur_num].setposition(position)
        self.head.fd(20)
    
    def change_color(self, color_tuple):
        r = int(color_tuple[0])
        g = int(color_tuple[1])
        b = int(color_tuple[2])
        for tur in self.turtles:
            tur.color(r, g, b)

    def increment_turtle(self):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        last_pos = self.turtles[-1].position()
        new_turtle.setposition(last_pos)
        self.turtles.append(new_turtle)


    def up(self):
        current_heading = self.head.heading()
        if abs((current_heading - 90)) == 180:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        current_heading = self.head.heading()
        if abs((current_heading - 270)) == 180:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        current_heading = self.head.heading()
        if abs((current_heading - 180)) == 180:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        current_heading = self.head.heading()
        if abs((current_heading - 0)) == 180:
            pass
        else:
            self.head.setheading(0)