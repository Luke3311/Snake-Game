from turtle import Turtle
#Constant variables
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        #Snake is created at start, with 3 segments.
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)


    def add_segment(self,pos):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(pos)
        self.segments.append(new_snake)




    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_number in range(len(self.segments)-1,0,-1 ):
            x_new = self.segments[seg_number -1].xcor()
            y_new = self.segments[seg_number -1].ycor()
            self.segments[seg_number].goto(x_new,y_new)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)