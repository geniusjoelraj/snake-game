import turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
screen.bgcolor('black')
screen.title = "Snake Game"
screen.tracer(0)
screen.listen()
turtle.screensize(canvheight=680, canvwidth=1300)

scoreboard = ScoreBoard()

def start():
    screen.update()
    global game_on
    game_on = True
    while game_on:
        screen.update()
        snake.move()
        if snake.segments[0].distance(food) <= 10:
            snake.add_segment()
            scoreboard.update()
            food.spawn()
        for seg in snake.segments[1:]:
            if snake.segments[0].distance(seg) <= 10:
                game_on = False
                scoreboard.game_over()
        if (snake.segments[0].xcor() >= 700 or snake.segments[0].xcor() <= -700 or
            snake.segments[0].ycor() >= 400 or snake.segments[0].ycor() <= -400):
            game_on = False
            scoreboard.game_over()

def reset_game():
    screen.update()
    global snake, food, scoreboard
    screen.clear()
    screen.bgcolor('black')
    screen.title = "Snake Game"
    screen.tracer(0)
    screen.listen()
    turtle.screensize(canvheight=680, canvwidth=1300)
    snake = Snake()
    food = Food()
    food.spawn()
    scoreboard = ScoreBoard()
    
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(start, " ")
    screen.onkey(reset_game, "r")

    start()

snake = Snake()
food = Food()
food.spawn()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(start, " ")
screen.onkey(reset_game, "r")

screen.update()
screen.mainloop()
