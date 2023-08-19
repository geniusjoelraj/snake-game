from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.pu()
        self.goto(0, 300)
        self.write(f"Score: {self.score}", align="center", font=('Courier', 24, 'normal'))
    
    def game_over(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.pu()
        self.write("Game Over!", align="center", font=('Courier', 24, 'normal'))



    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=('Courier', 24, 'normal'))
