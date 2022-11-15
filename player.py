from turtle import Turtle

POS_X = 0
POS_Y = -280


class Player:

    def __init__(self):
        self.fly = Turtle()
        self.fly.penup()
        self.fly.shape("triangle")
        self.fly.color("green")
        self.fly.shapesize(1,3)
        self.fly.goto(POS_X, POS_Y)
        self.fly.left(90)

    def move_right(self):
        pos_x = self.fly.xcor()
        new_pos = pos_x + 10
        self.fly.goto(x=new_pos, y=POS_Y)
        if self.fly.xcor() > 380:
            new_pos = pos_x
            self.fly.goto(x=new_pos, y=POS_Y)

    def move_left(self):
        pos_x = self.fly.xcor()
        new_pos = pos_x - 10
        self.fly.goto(x=new_pos, y=POS_Y)
        if self.fly.xcor() > 380:
            new_pos = pos_x
            self.fly.goto(x=new_pos, y=POS_Y)