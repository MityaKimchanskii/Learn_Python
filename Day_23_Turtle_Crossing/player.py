from turtle import Turtle

START = (0, -280)
MOVE = 10
FINISH = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.goto_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE)

    def go_down(self):
        self.back(MOVE)

    def is_at_finish(self):
        if self.ycor() > FINISH:
            return True
        else:
            return  False

    def goto_start(self):
        self.goto(START)