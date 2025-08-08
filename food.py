from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.new_pos()

    def new_pos(self):
        x_cor=random.randint(-280,280)
        y_cor=random.randint(-280,280)
        self.setposition(x_cor,y_cor)
