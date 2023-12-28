from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.colormode(255)
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600) 
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')

score_board = ScoreBoard()

game_is_on = True
gap = 0.1
while game_is_on:
    screen.update()
    time.sleep(gap)
    snake.move()
    if food.distance(snake.head) < 16:
        snake.increment_turtle()

        color_tuple = food.pencolor()
        snake.change_color(color_tuple)
        food.move_to_randpos()
        food.change_to_randcolor()
        

        score_board.increase_score()

        gap -= 0.002

    x = snake.head.xcor()
    y = snake.head.ycor()
    if abs(x) > 290 or abs(y) > 290:
        game_is_on = False
        score_board.print_game_over()
    
    for tur in snake.turtles[1:]:
        if snake.head.distance(tur) < 10:
            game_is_on = False
            score_board.print_game_over() 
       

screen.exitonclick()