import pygame
from classes.values_and_grids.grids_and_paths import *
from classes.values_and_grids.constant_values import *
import random

'''
def customer_spawn(x, y, customerImg):
   pos_x = (SquareSize * x)
   pos_y = (SquareSize * y)
   Screen.blit(customerImg, (pos_x, pos_y))
'''
Screen = pygame.display.set_mode((height, width))


class customers:

    def __init__(self, random_seat, age, sex, vegetarian, budget, d_type, temperature, weight, img):
        self.random_seat = random_seat
        self.age = age
        self.sex = sex
        self.vegetarian = vegetarian
        self.budget = budget
        self.d_type = d_type
        self.temperature = temperature
        self.weight = weight
        self.img = img
        self.meal = None

    def customer_spawn(self):

        random_seat = random.choice(free_seats)
        seat_num = seats.get(random_seat)

        return seat_num[0], seat_num[1], self.img, random_seat


all_customers = [customers(1, 55, 1, 1, 3, 1, 2, 2, "../grafiki/klient_1.png"),
                 customers(1, 20, 2, 0, 1, 2, 1, 1, "../grafiki/klient_2.png"),
                 customers(1, 36, 1, 0, 2, 1, 2, 1, "../grafiki/kelner.png")]