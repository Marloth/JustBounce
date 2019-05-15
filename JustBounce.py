import turtle
import time

turtle.register_shape("Pilka1.gif")
turtle.register_shape("kolce.gif")
turtle.register_shape("background.gif")
turtle.register_shape("Chmura.gif")
turtle.register_shape("Chmura1.gif")

wn = turtle.Screen()
wn.title("Simple Game")
wn.bgpic("Background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-320, 250)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

go_pen = turtle.Turtle()
go_pen.speed(0)
go_pen.color("white")
go_pen.penup()
go_pen.setposition(-0, 0)
scorestring = ""
go_pen.write(scorestring, False, align="left", font=("Arial", 36, "normal"))
go_pen.hideturtle()

# Pilka
Pilka = turtle.Turtle()
Pilka.speed(0)
Pilka.shape("Pilka1.gif")
Pilka.color("black")
Pilka.shapesize(stretch_wid=3, stretch_len=3)
Pilka.penup()
Pilka.goto(-300, -200)
Pilka.dy = 0
Pilka.gravity = 0
Pilka.gameover = 0
Pilka.jumps = 0

# Podloga
Podloda = turtle.Turtle()
Podloda.speed(0)
Podloda.shape("square")
Podloda.color("#248f24")
Podloda.shapesize(stretch_wid=5, stretch_len=800)
Podloda.penup()
Podloda.goto(0, -300)

# Kolec
Kolec = turtle.Turtle()
Kolec.speed(0)
Kolec.shape("kolce.gif")
Kolec.color("black")
Kolec.shapesize(stretch_wid=6, stretch_len=4)
Kolec.tilt(180)
Kolec.penup()
Kolec.goto(400, -210)

# Chmura
Chmura = turtle.Turtle()
Chmura.speed(0)
Chmura.shape("Chmura.gif")
Chmura.tilt(180)
Chmura.penup()
Chmura.goto(400, 100)
Chmura1 = turtle.Turtle()
Chmura1.speed(0)
Chmura1.shape("Chmura1.gif")
Chmura1.tilt(0)
Chmura1.penup()
Chmura1.goto(800, 150)

# Functions
def bounce():
    if Pilka.jumps < 2:
        Pilka.dy = 2
        Pilka.gravity = 0.02
        Pilka.jumps += 1

def gameover():
    Pilka.gameover = 1

# Keyboard bindings
wn.listen()
wn.onkeypress(bounce, "w")

# main game loop
while True:
    Pilka.dy -= Pilka.gravity
    Pilka.sety(Pilka.ycor() + Pilka.dy)
    if Pilka.ycor() <= -200:
        Pilka.goto(-300, -200)
        Pilka.dy = 0
        Pilka.gravity = 0
        Pilka.jumps = 0

    Kolec.setx(Kolec.xcor() -1.5 -(score / 100))

    if Kolec.xcor() <= -400:
        Kolec.setx(400)
        score += 10
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    Chmura.setx(Chmura.xcor() - 0.06)
    if Chmura.xcor() <= -600:
        Chmura.setx(600)
    Chmura1.setx(Chmura1.xcor() - 0.04)
    if Chmura1.xcor() <= -600:
        Chmura1.setx(1000)

    #Game Over
    if Pilka.distance(Kolec) < 90:
        go_pen.clear()
        go_pen.write("GAME OVER", False, align="center", font=("Arial", 36, "normal"))
        time.sleep(2)
        Kolec.goto(400, -210)
        Chmura1.goto(800, 150)
        Chmura.goto(400, 100)
        Pilka.goto(-300, -200)
        Pilka.dy = 0
        Pilka.gravity = 0
        score = 0
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        go_pen.clear()
    wn.update()
