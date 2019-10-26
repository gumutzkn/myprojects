import turtle
import time
import winsound

wn = turtle.Screen()
wn.title("PONG BY @SİKİCİ")
wn.bgcolor("gray")
wn.setup(width = 1200 , height=800)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=10, stretch_len=2)
paddle_a.goto(-560, 0)


# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=10, stretch_len=2)
paddle_b.goto(560, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("brown")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 #delta demek delta x
ball.dy = -0.2 #delta demek delta y

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Player 1: 0 | Player 2: 0", align="center", font=("Courier",26,"bold"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 35
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 35
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 35
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 35
    paddle_b.sety(y)


# Keyboard binding(bağlamak)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 605:
        ball.setx(ball.xcor() + ball.dx)
        score_a += 1
        time.sleep(0.5)
        ball.goto(0, 0)
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_a, score_b), align="center", font=("Courier",26,"bold"))

    if ball.xcor() < -610:
        ball.setx(ball.xcor() + ball.dx)
        score_b += 1
        time.sleep(0.5)
        ball.goto(0, 0)
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_a, score_b), align="center", font=("Courier",26,"bold"))


    # Paddle and ball collisions
    if (ball.xcor() > 540 and ball.xcor() < 560) and (ball.ycor() < paddle_b.ycor() + 100 and ball.ycor() > paddle_b.ycor() -100):
        ball.setx(540)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -540 and ball.xcor() > -560) and (ball.ycor() < paddle_a.ycor() + 100 and ball.ycor() > paddle_a.ycor() -100):
        ball.setx(-540)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
