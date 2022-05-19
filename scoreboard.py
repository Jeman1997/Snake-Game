from turtle import Turtle


class Scorebd(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open('highscore.txt') as hf:  
            self.highscore=int(hf.read())
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.upd()
        
    def upd(self):
        self.clear()
        self.write(f'score:{self.score} highscore: {self.highscore}',align='center',font=("Arial",24,"normal"))
        self.hideturtle()
        self.score+=1

    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score-1
            with open('highscore.txt',mode='w') as hf:
                hf.write(str(self.score-1))
        self.score = 0
        self.upd()
