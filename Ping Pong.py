import turtle
import winsound

window = turtle.Screen()
window.title('Ping Pong Game')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer()

# Score
score1 = 0
score2 = 0

# Padder A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Padder B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.cx = 5
ball.cy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player 1: 0  Player 2: 0', align='center',
          font=('Courier', 16, 'normal'))


# Functions
def paddle_a_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddle_a_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddle_b_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddle_b_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keys
window.listen()

window.onkeypress(paddle_a_up, 'w')

window.onkeypress(paddle_a_down, 's')

window.onkeypress(paddle_b_up, 'Up')

window.onkeypress(paddle_b_down, 'Down')


while True:
    window.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.cx)
    ball.sety(ball.ycor() + ball.cy)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.cy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.cy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.cx *= -1
        score1 += 1
        pen.clear()
        pen.write('Player 1: {}  Player 2: {}'.format(score1, score2),
                  align='center', font=('Courier', 16, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.cx *= -1
        score2 += 1
        pen.clear()
        pen.write('Player 1: {}  Player 2: {}'.format(score1, score2),
                  align='center', font=('Courier', 16, 'normal'))

    # Paddle and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.cx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.cx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # AI Player
    #if paddleB.ycor() < ball.ycor() and abs(paddleB.ycor() - ball.ycor()) > 10:
       # paddle_b_up()

    #elif paddleB.ycor() > ball .ycor() and abs(paddleB.ycor() - ball.ycor()) > 10:
        #paddle_b_down()
