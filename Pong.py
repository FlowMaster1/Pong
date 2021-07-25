import time
import turtle

wn = turtle.Screen()

wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

score_a = 0
score_b = 0
speed = 0.4


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len= 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len= 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def paddleUp(paddle):
    y = paddle.ycor()
    y += 30
    paddle.sety(y)

def paddleDown(paddle):
    y = paddle.ycor()
    y -= 30
    paddle.sety(y)


wn.listen()
wn.onkeypress(lambda p = paddle_a: paddleUp(p), "w")
wn.onkeypress(lambda p = paddle_a: paddleDown(p), "s")



while(True):
    wn.update()

    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() >= 400:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx = -0.3
        ball.dy = 0.3
        speed = 0.2
        time.sleep(0.5)
    elif ball.xcor() < -400:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx = 0.3
        ball.dy = 0.3
        speed = 0.2   
        ball.goto(0, 0)
        time.sleep(0.5)

    if ball.ycor() >= 290 or ball.ycor() <= -285:
        ball.dy *= -1

    #collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1.1 
        ball.dy *= 1.1
        speed *= 1.05
    
    elif (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1.1
        ball.dy *= 1.1
        speed *= 1.07


    #Enemie Ai
    if paddle_b.ycor() < ball.ycor():
        
        paddle_b.sety(paddle_b.ycor() + speed)
    elif  paddle_b.ycor() > ball.ycor():
        paddle_b.sety(paddle_b.ycor() - speed)



    


    

