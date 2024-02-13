import turtle
wind = turtle.getscreen()
wind.title("Ping Pong By Fawzi")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)   #  stop the windows from updating automatic

#madrap 1
madrap1=turtle.Turtle()
madrap1.speed(0)
madrap1.shape("square")
madrap1.color("blue")
madrap1.shapesize(stretch_wid=5,stretch_len=1)
madrap1.penup() # stop the object from drawing lines
madrap1.goto(-350,0)

# madrap2
madrap2=turtle.Turtle()
madrap2.speed(0)
madrap2.shape("square")
madrap2.color("red")
madrap2.shapesize(stretch_wid=5,stretch_len=1)
madrap2.penup()
madrap2.goto(350,0)


#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.3
#score
score1=0
score2=0
score =turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0 Player 2: 0", align="center",font=("Courier",24,"normal"))


#function
def madrab1_up():
    y=madrap1.ycor()
    y+=20
    madrap1.sety(y)

def madrab1_down():
    y=madrap1.ycor()
    y-=20
    madrap1.sety(y)


def madrab2_up():
    y=madrap2.ycor() #get the y coordinat of madrap
    y+=20
    madrap2.sety(y)

def madrab2_down():
    y=madrap2.ycor()
    y-=20
    madrap2.sety(y)



#keyboard bindings
wind.listen() # tell the window expect keyboard inputs
wind.onkeypress(madrab1_up,"w")
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")




while True :
    wind.update() # update the screen everytime
    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border check
    if ball.ycor()>290 :
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290 :
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390 :
        ball.goto(0,0)
        ball.dx*=-1
        score1+=1
        score.clear()

        score.write("Player 1: {} Player 2: {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor()<-390 :
        ball.goto(0,0)
        ball.dx*=-1
        score2+=1
        score.clear()

        score.write("player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    #tasadom madrap and ball
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<madrap2.ycor()+40 and ball.ycor()>madrap2.ycor()-40) :
        ball.setx(340)
        ball.dx *=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<madrap1.ycor()+40 and ball.ycor()>madrap1.ycor()-40) :
        ball.setx(-340)
        ball.dx *=-1










