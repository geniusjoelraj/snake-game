from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape('turtle')
        self.pu()
        self.speed('fastest')
        self.shapesize(0.5, 0.5)
    
    def spawn(self):
        self.goto(random.randrange(-200, 200, 20), random.randrange(-200, 200, 20))