import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


if __name__ == "__main__":
    snakes = []
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Left", fun=snake.left)

    screen.update()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.grow()
            scoreboard.upgrade_score()
        # Collision with wall
        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            scoreboard.game_over()
            game_is_on = False
        # Collision with tail
        for piece in snake.snakes[1:]:
            if snake.head.distance(piece) < 10:
                scoreboard.game_over()
                game_is_on = False

    screen.exitonclick()
