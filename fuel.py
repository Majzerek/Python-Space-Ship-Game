from turtle import Turtle
import random
COLORS = ["red", "white", "yellow", "blue"]
start_speed = 10
class Fuel:

    def __init__(self):
        self.fuel_list = []
        self.create_fuel()

    def create_fuel(self):
        rand_change = random.randint(1, 8)
        if rand_change == 3:
            fuel = Turtle()
            fuel.penup()
            fuel.shape("triangle")
            fuel.shapesize(0.5, 0.5)
            fuel.color(random.choice(COLORS))
            rand_x = random.randint(-300, 300)
            fuel.goto(rand_x, 360)
            fuel.left(90)
            self.fuel_list.append(fuel)

    def start(self):
        for fuel in self.fuel_list:
            fuel.back(start_speed)