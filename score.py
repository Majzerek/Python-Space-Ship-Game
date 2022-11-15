from turtle import Turtle
FONT_OVER = ("Courier", 44, "bold")
class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("highscore.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            with open("highscore.txt", mode="w") as data:
                self.high_score = data.write(str(self.score))
        finally:
            self.penup()
            self.hideturtle()
            self.color("red")








    def update_board(self):
        self.goto(x=-350, y=250)
        self.write(arg=f"Score: {self.score}\nHighScore: {self.high_score} ", font=("Arial", 18, "bold"))

    def incrase_score(self):
        self.score += 50
        self.clear()
        self.update_board()

    def game_over(self):
        self.update_board()
        self.goto(0, 0)
        self.color("Blue")
        self.write("GAME OVER", False, align="center", font=FONT_OVER)
        self.goto(-40,-30)
        self.write(arg=f"score: {self.score}", font=("Arial", 18, "bold"))
        if self.score > self.high_score:
            self.high_score = str(self.score)
            with open("highscore.txt", mode="w") as data:
                data.write(self.high_score)
