from turtle import Turtle

FONT = ('ARIAL', 30, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-270,260)
        self.update()


    def livel_up(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center',font=FONT)