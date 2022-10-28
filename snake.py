from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.score = 0
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in range(3):
            self.grow()

    def grow(self):
        self.score += 1
        snake = Turtle("square")
        snake.penup()
        snake.goto(snake.xcor() - len(self.snakes) * MOVE_DISTANCE, 0)
        snake.color("white")
        self.snakes.append(snake)

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i].goto(self.snakes[i - 1].xcor(), self.snakes[i - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
