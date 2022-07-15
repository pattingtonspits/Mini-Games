import random

print("welcome to the minigames!")


def guessnumber():
    print("Welcome to Russian Roulette.")
    print("The rules are choose a number 1-6.")
    print("If its the bullet, you die.")
    print("Had to make that clear.")
    print("If its not the bullet, you live.")
    print("But its fun! You'll have fun ")
    print("if you get out alive.")
    print("Have fun and good luck.")
    contin = True
    while contin == True:
        tries = 5
        num = random.randint(1, 6)
        choice = num - 1
        while choice != num:
            choice = input()
            if int(choice) == num:
                print("Bang ya dead")
                print("play again? 7 for yes, 8 for no")
                choice = input()
                if int(choice) == 7:
                    contin = True
                    break
                if int(choice) == 8:
                    print("Have fun burning in the Underworld.")
                    contin = False
                    exit(0)
            else:
                tries -= 1
                if tries > 0:
                    print("Try Again")
                elif tries == 0:
                    print("You're alive, called it John. Pay up")
                    exit(0)


def beats(p1, p2):
    if p1 == 1:
        if p2 == 2:
            return False
        if p2 == 3:
            return True
    if p1 == 2:
        if p2 == 3:
            return False
        if p2 == 1:
            return True
    if p1 == 3:
        if p2 == 1:
            return False
        if p2 == 2:
            return True


def rps():
    while 1 == 1:
        print("1 = Rock, 2 = Paper, 3 = Scissors")
        print("Player 1: Make your decision")
        choice_player = input()
        choice_cpu = random.randint(1, 3)
        print(choice_cpu)
        if int(choice_player) == choice_cpu:
            print("EMOTINAL DAMAGE! WHY IT TIE! YOU WIN NOT TIE!")
        elif beats(int(choice_player), choice_cpu):
            print("You won? YOU WON! LETS$$# GO000000OO0O0O!")
        else:
            print("Faliure ")


def wordle():
    words = ["Basic", "Happy", "Lists", "Pines", "Major", "Clock", "Lakes", "Plane", "Heart", "Knees", "Print"]
    word = random.choice(words)

    while 1 == 1:
        print(" Make Your Guess. 5 Letters!")
        choice = input()
        if word == choice:
            print("Good Job! The word was", word)
            exit()
        else:
            i = 0
            while i < 5:
                if word[i] == choice[i]:
                    print(choice[i].upper(), end="")
                else:
                    print(choice[i], end="")
                i += 1


def pong():
    import turtle
    import time

    screen = turtle.Screen()
    screen.tracer(0)
    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=1000, height=600)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 200)
    pen.write("0                0", align="center",
              font=("candera", 50, "bold"))

    global p1arr, p2arr, ball, delay

    p1arr = []
    p2arr = []

    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.penup()

    for x in range(0, 4):
        p1arr.append(turtle.Turtle())
        p1arr[x].shape("square")
        p1arr[x].color("white")
        p1arr[x].penup()
        p2arr.append(turtle.Turtle())
        p2arr[x].shape("square")
        p2arr[x].color("white")
        p2arr[x].penup()

    def resetGame():
        global delay, p1arr, p2arr
        delay = 0.08

        for x in range(0, 4):
            p1arr[x].goto(-450, 20 * x)
            p2arr[x].goto(450, 20 * x)

        ball.goto(0, 0)
        ball.dx = 1
        ball.dy = 1

    def p1moveup():
        moveup(p1arr)

    def p1movedown():
        movedown(p1arr)

    def p2moveup():
        moveup(p2arr)

    def p2movedown():
        movedown(p2arr)

    screen.listen()
    screen.onkeypress(p1moveup, 'w')
    screen.onkeypress(p1movedown, 's')
    screen.onkeypress(p2moveup, 'Up')
    screen.onkeypress(p2movedown, 'Down')

    def movedown(turtlearr):
        for turtle in turtlearr:
            y = turtle.ycor()
            if y > -270:
                turtle.sety(turtle.ycor() - 20)
            else:
                return

    def moveup(turtlearr):
        for turtle in reversed(turtlearr):
            y = turtle.ycor()
            if y < 270:
                turtle.sety(turtle.ycor() + 20)
            else:
                return



    def moveball(ball):
        global delay, p1arr, p2arr, score1, score2
        x = ball.xcor()
        y = ball.ycor()

        if (y + 20 * ball.dy > 300 or y + 20 * ball.dy < -300):
            ball.dy = -ball.dy
        for p1 in p1arr:
            if ball.distance(p1) < 20:
                ball.dx = -ball.dx
                delay -= 0.003

        for p2 in p2arr:
            if ball.distance(p2) < 20:
                ball.dx = -ball.dx
                delay -= 0.003

        ball.setx(x + 10 * ball.dx)
        ball.sety(y + 10 * ball.dy)

    resetGame()

    global score1, score2
    score1 = 0
    score2 = 0

    while True:
        screen.update()
        moveball(ball)
        if ball.xcor() > 500:
            score1 += 1
            pen.clear()
            pen.write("{}                {}".format(score1, score2), align="center",
                      font=("candera", 50, "bold"))
            resetGame()
        if ball.xcor() < -500:
            score2 += 1
            pen.clear()
            pen.write("{}                {}".format(score1, score2), align="center",
                      font=("candera", 50, "bold"))
            resetGame()
        time.sleep(delay)
    screen.mailloop()


print("Select a game!")
print("1: Roshambo 2: Russian Roulette 3: Wordle 4: Pong")
ch = input()
if int(ch) == 1:
    rps()
elif int(ch) == 2:
    guessnumber()
if int(ch) == 3:
    wordle()
if int(ch) == 4:
    pong()
