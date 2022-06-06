import pygame
from classes.values_and_grids.GridsAndPaths import *
from classes.values_and_grids.ConstantValues import *
import random


'''
def customer_movement(x, y, customerImg):
   pos_x = (SquareSize * x)
   pos_y = (SquareSize * y)
   Screen.blit(customerImg, (pos_x, pos_y))
'''
Screen = pygame.display.set_mode((Height, Width))


class Customers:

    def __init__(self, random_seat):
        self.random_seat = random_seat

    def customer_spawn(self):

        random_seat = random.choice(free_seats)
        character_random = random.randint(0, 1)
        if character_random == 1:
            customerImg = pygame.image.load('../grafiki/klient_1.png')
        else:
            customerImg = pygame.image.load('../grafiki/klient_2.png')


        seat_num = seats.get(random_seat)

        return seat_num[0], seat_num[1], customerImg, random_seat




















