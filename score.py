from turtle import  Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("high_score.txt","r") as file:
            self.high_score=int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.color("white")
        self.write(f"Score : {self.score}  High Score : {self.high_score}",align="center",font=("Courier",15,"normal"))

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}",align="center",font=("Courier",15,"normal"))

    def game_over(self):
        if self.score>self.high_score:
            self.high_score=self.score
        with open("high_score.txt","w") as file:
            file.write(f"{self.high_score}")
        self.goto(0,0)
        self.write(f"WOOPS, GAME OVER! ",align="center",font=("IMPACTFUL",25,"bold"))

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
        with open("high_score.txt","w") as file:
            file.write(f"{self.high_score}")

        self.score=0
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}",align="center" , font=("Courier", 15, "normal"))
