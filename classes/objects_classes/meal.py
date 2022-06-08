import random
from classes.values_and_grids.grids_and_paths import *

import pygame


class meal:

    def __init__(self, id, name, prepareTime):
        self.id = id
        self.name = name
        self.prepareTime = prepareTime

    def load_images(predict):
        if predict == [1]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/soup.png')
            return dish

        if predict == [2]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/scallops.png')
            return dish

        if predict == [3]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/chicken.png')
            return dish

        if predict == [4]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/porkchop.png')
            return dish

        if predict == [5]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/risotto.png')
            return dish

        if predict == [6]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/duck.png')
            return dish

        if predict == [7]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/steak.png')
            return dish

        if predict == [8]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/ratatouille.png')
            return dish

        if predict == [9]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/icecream.png')
            return dish

        if predict == [10]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/pavlova.png')
            return dish

        if predict == [11]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/pannacotta.png')
            return dish

        if predict == [12]:
            dish = pygame.image.load('../grafiki/decisiontreeimages/souffle.png')
            return dish


def meal_spawn():
    random_deposit = random.choice(free_deposits)
    deposit_num = meal_deposit.get(random_deposit)

    return deposit_num[0], deposit_num[1], random_deposit


listofmeals = [meal(1, 'Soup', 60),
               meal(2, 'Scallops', 45),
               meal(3, 'Chicken', 80),
               meal(4, 'Pork Chop', 82),
               meal(5, 'Risotto', 70),
               meal(6, 'Duck', 60),
               meal(7, 'Steak', 45),
               meal(8, 'Ratatouille', 35),
               meal(9, 'Ice cream', 10),
               meal(10, 'Pavlova', 20),
               meal(11, 'Panna Cotta', 22),
               meal(12, 'Souffle', 25)]
