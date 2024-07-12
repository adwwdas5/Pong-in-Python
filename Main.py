import turtle

window = turtle.Screen()
window.title("Pong in Python")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score1 = 0
score2 = 0

player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

def player1Up():
	y = player1.ycor()
	y += 20
	player1.sety(y)

def player1Down():
	y = player1.ycor()
	y -= 20
	player1.sety(y)

def player2Up():
	y = player2.ycor()
	y += 20
	player2.sety(y)

def player2Down():
	y = player2.ycor()
	y -= 20
	player2.sety(y)

window.listen()
window.onkeypress(player1Up, "w")
window.onkeypress(player1Down, "s")
window.onkeypress(player2Up, "Up")
window.onkeypress(player2Down, "Down")

while True:
	window.update()

	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dy *= -1
		score1 +=1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dy *= -1
		score2 +=1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

	if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() -50):
		ball.setx(340)
		ball.dx *= -1

	if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() -50):
		ball.setx(-340)
		ball.dx *= -1