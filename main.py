from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score_board

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)  # Turns off the screen updates for faster drawing

my_snake = Snake()
all_snakes = my_snake.all_turtles
my_food = Food()
my_score=Score_board()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")  
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")  
my_screen.onkey(my_snake.right, "Right")
   

game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(my_food)<15:
        my_food.new_pos()
        my_score.update_score()
        my_snake.extend_snake()
    
    for snake in my_snake.all_turtles:
        if snake == my_snake.head:
            pass
        elif my_snake.head.distance(snake)<10:
            my_score.game_over()
            game_on= False

            


    
    

   












my_screen.exitonclick()