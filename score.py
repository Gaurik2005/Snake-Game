from turtle import  Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.color("white")
        self.write(f"Score : {self.score}",align="center",font=("Arial",15,"normal"))

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Courier",15,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"WOOPS, GAME OVER! ",align="center",font=("IMPACTFUL",25,"bold"))

        
