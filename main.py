from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Detect a miss by r_paddle
    if ball.xcor() > 340:
        ball.home()
        ball.x_move *= -1
        ball.y_move *= -1
        ball.move()
        scoreboard.l_point()
        ball.move_speed = 0.1

    # Detect a miss by l_paddle
    if ball.xcor() < -340:
        ball.home()
        ball.x_move *= -1
        ball.y_move *= -1
        ball.move()
        scoreboard.r_point()
        ball.move_speed = 0.1




screen.exitonclick()