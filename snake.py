from turtle import Turtle
pos = [(0,0),(-20,0),(-40,0)]
speed = 20
WALL=290

class Snake():

    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head=self.all_turtles[0]

    def add_snake(self,position):
        my_turtle = Turtle()
        my_turtle.shape("square")
        my_turtle.color("white")
        my_turtle.speed("fastest")
        my_turtle.penup()
        my_turtle.goto(position)
        self.all_turtles.append(my_turtle)


    def create_snake(self):
        for position in pos:
            self.add_snake(position)

    


    def extend_snake(self):
        self.add_snake(self.all_turtles[-1].position())

    def move(self):
        for i in range(len(self.all_turtles) - 1, 0, -1):
            x_cord = self.all_turtles[i - 1].xcor()
            y_cord = self.all_turtles[i - 1].ycor()
            self.all_turtles[i].goto(x_cord, y_cord)
        self.head.forward(speed)
        self.wall_col()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def wall_col(self):
        
        if self.head.ycor()>WALL:
            self.head.goto(self.head.xcor(),-WALL)
        elif self.head.ycor()< -WALL:
                self.head.goto(self.head.xcor(),WALL)
        elif self.head.xcor()>WALL:
            self.head.goto(-WALL,self.head.ycor())
        elif self.head.xcor()< -WALL:
                self.head.goto(WALL,self.head.ycor())


    