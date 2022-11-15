import time
from turtle import *
from player import Player
from asteroid import Material
from fuel import Fuel
from score import Board
import random

game_speed = 0.05
screen = Screen()
screen.setup(width=800, height=640)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
asteroid = Material()
fuel = Fuel()
board = Board()

screen.listen()
screen.onkeypress(fun=player.move_right, key="Right")
screen.onkeypress(fun=player.move_left, key="Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(game_speed)
    asteroid.create_asteroid()
    asteroid.fall()
    fuel.create_fuel()
    fuel.start()
    board.update_board()

    for one_asteroid in asteroid.asteroids:
        if one_asteroid.distance(player.fly) < 20:
            player.fly.color("red")
            board.game_over()
            time.sleep(2)
            is_on= False

    for square in fuel.fuel_list:
        if square.distance(player.fly) < 25:
            square.goto(1000, 1000)
            board.incrase_score()

    if board.score == 200:
        asteroid.star_speed = 10

    if board.score == 500:
        asteroid.star_speed = 15
    if board.score == 1000:
        asteroid.star_speed = 25
    if board.score == 2500:
        asteroid.star_speed = 35
        asteroid.create_special_asteroid()













screen.mainloop()