from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detects when snake collides with food
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        score.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 11:
            game_on = False
            score.game_over()

screen.exitonclick()
