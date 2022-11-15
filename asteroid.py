from turtle import Turtle
import random

POS_Y = 330
STARTING_MOVE_DISTANCE = 5
class Material():

    def __init__(self):
        self.star_speed = STARTING_MOVE_DISTANCE
        self.asteroids = []



    def create_asteroid(self):
        rand_change = random.randint(1,3)
        if rand_change == 1:
            new_asteroid = Turtle()
            new_asteroid.penup()
            new_asteroid.shape("circle")
            new_asteroid.shapesize(1, 2)
            new_asteroid.color("white")
            rand_x = random.randint(-360, 360)
            new_asteroid.goto(rand_x, 360)
            new_asteroid.left(90)
            self.asteroids.append(new_asteroid)

    def fall(self):
        for asteroid in self.asteroids:
            asteroid.back(self.star_speed)

    def create_special_asteroid(self):
        rand_change = random.randint(1,2)
        if rand_change == 1:
            new_asteroid = Turtle()
            new_asteroid.penup()
            new_asteroid.shape("circle")
            new_asteroid.shapesize(1, 2)
            new_asteroid.color("white")
            rand_x = random.randint(-360, 360)
            new_asteroid.goto(rand_x, 360)
            new_asteroid.left(90)
            self.asteroids.append(new_asteroid)
