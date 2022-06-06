from classes.values_and_grids.ConstantValues import *
from classes.values_and_grids.Grid import *
from classes.values_and_grids.GridsAndPaths import *
from classes.decision_tree.Decision_Tree import *
from classes.searching.Search import Search
from classes.objects_classes.Table import Table
from classes.neural_networks.recognizesingleimage import *
from classes.objects_classes.Customer import *
import time
import random
from random import choice as rchoice

# Game screen with grid
pygame.init()
clock = pygame.time.Clock()
Screen = pygame.display.set_mode((Height, Width))
pygame.display.set_caption("Kelner")
Background = pygame.image.load('../grafiki/restauracja.png')
grid = Grid()
search = Search(testPath[1], testPath[5])
usedtables = []


def agent(x, y):
    pos_x = (SquareSize * x)
    pos_y = (SquareSize * y)
    Screen.blit(agentImg, (pos_x, pos_y))


def customer_movement(x, y, customerImg):
    posx = (SquareSize * x)
    posy = (SquareSize * y)
    Screen.blit(customerImg, (posx, posy))


def dish(x, y, img):
    pos_x = (SquareSize * x)
    pos_y = (SquareSize * y)
    Screen.blit(img, (pos_x, pos_y))


# Symulacja
running = True
j = 0
flag = False
priority = False


agentX = 11
agentY = 5

active_customers = []
while running:

    if j == 0 or j == len(a_star_path) - 1:
        agentX = 11
        agentY = 5
        agentImg = pygame.image.load('../grafiki/kelner_prawo.png')
        first_angle = 0
        j = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Screen.blit(Background, (0, 0))

    # klient_stuff_ghetto_code

    # spawnowanie nowego klienta

    if len(active_customers) < 3:
            i = 3 - len(active_customers)
            for _ in range(i):

                '''cust = rchoice(all_customers)  # losujemy klienta a potem go usuwamy z listy klientow
                all_customers.remove(cust)
                res = cust.customer_spawn()
                usedtables.append(Table(res[0], res[1], cust))  # dodajemy stolik do listy uzywanych stolikow
                cust_timing = 1
                priority == True
                customer_movement(4, 15, pygame.image.load(res[2]))  # spawn przy wejsciu
                '''
                cust = rchoice(all_customers)  # losujemy klienta a potem go usuwamy z listy klientow
                res = cust.customer_spawn()
                usedtables.append(Table(res[0],res[1], cust))

                active_customers.append([res[3], res[0], res[1], pygame.image.load(res[2]), 'waiting'])  # tablica tablic z obecnymi klientami
                free_seats.remove(res[3])


            for customers in active_customers:
                customer_movement(customers[1], customers[2], customers[3])

    else:
        for customers in active_customers:
            customer_movement(customers[1], customers[2], customers[3])



    if len(active_customers) == 3:  # jesli wszyscy klienci siedza juz na miejscach rozpoczynamy zbieranie zamowien

        incoming = rchoice(usedtables)
        while incoming.order:  # losujemy dopoki nie znajdziemy klienta bez zamowienia
            incoming = rchoice(usedtables)
        a_star_path = (a_star_strategy((agentX, agentY), (incoming.x, incoming.y), "Right", tuple_grid, G_cost))

        while j != len(a_star_path) - 1:
            if a_star_path[j] == 'Go':
                if first_angle == 0:
                    agentX += 1
                elif first_angle == 90:
                    agentY -= 1
                elif first_angle == 180:
                    agentX -= 1
                elif first_angle == 270:
                    agentY += 1
                agent(agentX, agentY)

            if a_star_path[j] == 'rotate Left':
                first_angle += 90
                if first_angle == 360:
                    first_angle = 0
                agentImg = search.angleSwitch(first_angle)
                agent(agentX, agentY)

            if a_star_path[j] == 'rotate Right':
                first_angle -= 90
                if first_angle < 0:
                    first_angle = 270
                agentImg = search.angleSwitch(first_angle)
                agent(agentX, agentY)

            j += 1
            grid.drawGrid(Screen)

            pygame.display.update()
            Screen.blit(Background, (0, 0))
            for customers in active_customers:
                customer_movement(customers[1], customers[2], customers[3])


            clock.tick(2)
        #Screen.blit(Background, (0, 0))
        # akcja gdy kelner jest przy celu
        incoming.order = True
        incoming.customer.meal = predict_from_decision_tree(incoming.customer.age,
                                                            incoming.customer.sex,
                                                            incoming.customer.vegetarian,
                                                            incoming.customer.budget,
                                                            incoming.customer.d_type,
                                                            incoming.customer.temperature,
                                                            incoming.customer.weight)  # przypisujemy klientowi posilek
        print(incoming.customer.meal)
        grid.drawGrid(Screen)

        pygame.display.update()

        #time.sleep(3)
