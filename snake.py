from turtle import Turtle, Screen
import time
screen = Screen()
no_death = False

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(2):
            new_segment = Turtle()
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.pu()
            new_segment.goto(-20*i, 0)
            self.segments.append(new_segment)
    def move(self):
        screen.update()
        time.sleep(0.1)
        for i in range(len(self.segments)-1, 0, -1):
            xcor = self.segments[i-1].xcor()
            ycor = self.segments[i-1].ycor()
            self.segments[i].goto(xcor, ycor)
        self.segments[0].fd(20)
        if no_death:
            if xcor > 650:
                self.segments[0].goto(-650, ycor)
            elif xcor < -650:
                self.segments[0].goto(650, ycor)
            elif ycor > 340:
                self.segments[0].goto(xcor, -340)
            elif ycor < -340:
                self.segments[0].goto(xcor, 340)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)    

    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.pu()
        xcor = self.segments[-1].xcor()
        ycor = self.segments[-1].ycor()
        new_segment.goto(xcor, ycor)
        self.segments.append(new_segment)