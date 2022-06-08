import pygame.image
from classes.values_and_grids.constant_values import *
from classes.values_and_grids.grid import *
from classes.values_and_grids.grids_and_paths import *
from classes.decision_tree.decision_tree import *
from classes.searching.search import Search
from classes.objects_classes.table import Table
from classes.neural_networks.recognize_single_image import *
from classes.objects_classes.customers import *
from classes.objects_classes.order import *
from classes.objects_classes.meal import *
import time
import random
from random import choice as rchoice

# game screen with grid
pygame.init()
clock = pygame.time.Clock()
Screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Kelner")
Background = pygame.image.load('../grafiki/restauracja.png')
grid = Grid()
search = Search(testPath[1], testPath[5])

# variables
running = True
fresh_start = True
flag = False
priority = False
orders_taken = False
orders_delivered = False
carries_meal = False
waiter_step = 0

start_pos_x = 11
start_pos_y = 5

agent_x = start_pos_x
agent_y = start_pos_y

customers_limit = len(all_customers)
active_customers = []
used_tables = []
used_deposits = []
orders_list = []
undelivered_dish_list = []


def agent(x, y):
    pos_x = (square_size * x)
    pos_y = (square_size * y)
    Screen.blit(agentImg, (pos_x, pos_y))


def customer_spawn(x, y, customer_img):
    posx = (square_size * x)
    posy = (square_size * y)
    Screen.blit(customer_img, (posx, posy))


def dish(x, y, img):
    pos_x = (square_size * x)
    pos_y = (square_size * y)
    Screen.blit(img, (pos_x, pos_y))

def obst(x, y, img):
    pos_x = (square_size * x)
    pos_y = (square_size * y)
    Screen.blit(pygame.image.load(img), (pos_x, pos_y))

def obsticles():
    for i in range(0, len(G_cost) - 1):
        for j in range(0, len(G_cost[i]) - 1):
            if G_cost[i][j] == water:

                eke = '../grafiki/woda.png'
                obst(i, j, eke)
            elif G_cost[i][j] == banan:
                kek = '../grafiki/banan.png'
                obst(i, j, kek)

# simulation

while running:
    Screen.blit(Background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    if fresh_start:
        agentImg = pygame.image.load('../grafiki/kelner_prawo.png')
        first_angle = 0
        waiter_step = 0

    else:
        agent_x = last_x_coordinates
        agent_y = last_y_coordinates
        first_angle = 0
        waiter_step = 0

    # SPAWNOWANIE KLIENTOW
    if len(active_customers) < customers_limit:
        i = customers_limit - len(active_customers)
        for _ in range(i):

            customer = rchoice(all_customers)
            customer_spawned = customer.customer_spawn()
            used_tables.append(Table(customer_spawned[0], customer_spawned[1], customer))
            active_customers.append(
                [customer_spawned[3], customer_spawned[0], customer_spawned[1], pygame.image.load(customer_spawned[2]), 'waiting'])
            free_seats.remove(customer_spawned[3])

        for customers in active_customers:
            customer_spawn(customers[1], customers[2], customers[3])

    else:
        for customers in active_customers:
            customer_spawn(customers[1], customers[2], customers[3])

        if orders_taken == True:
            for meal_in_list in undelivered_dish_list:
                dish(meal_in_list[1], meal_in_list[2], meal_in_list[3])





    # ZBIERANIE ZAMOWIEN
    if len(active_customers) == customers_limit and orders_taken == False:

        waiting_client = rchoice(used_tables)
        while waiting_client.order:
            waiting_client = rchoice(used_tables)
        a_star_path = (a_star_strategy((agent_x, agent_y), (waiting_client.x, waiting_client.y), "Right", tuple_grid,G_cost))

        while waiter_step != len(a_star_path) - 1:
            if a_star_path[waiter_step] == 'Go':
                if first_angle == 0:
                    agent_x += 1
                elif first_angle == 90:
                    agent_y -= 1
                elif first_angle == 180:
                    agent_x -= 1
                elif first_angle == 270:
                    agent_y += 1
                agent(agent_x, agent_y)

            if a_star_path[waiter_step] == 'rotate Left':
                first_angle += 90
                if first_angle == 360:
                    first_angle = 0
                agentImg = search.angleSwitch(first_angle)
                agent(agent_x, agent_y)

            if a_star_path[waiter_step] == 'rotate Right':
                first_angle -= 90
                if first_angle < 0:
                    first_angle = 270
                agentImg = search.angleSwitch(first_angle)
                agent(agent_x, agent_y)

            obsticles()
            fresh_start = False
            last_x_coordinates = agent_x
            last_y_coordinates = agent_y

            waiter_step += 1

            grid.draw_grid(Screen)
            pygame.display.update()




            Screen.blit(Background, (0, 0))
            for customers in active_customers:
                customer_spawn(customers[1], customers[2], customers[3])

            clock.tick(10)




        # Screen.blit(Background, (0, 0))
        # akcja gdy kelner jest przy celu


        waiting_client.order = True
        waiting_client.customer.meal = predict_from_decision_tree(waiting_client.customer.age,
                                                                  waiting_client.customer.sex,
                                                                  waiting_client.customer.vegetarian,
                                                                  waiting_client.customer.budget,
                                                                  waiting_client.customer.d_type,
                                                                  waiting_client.customer.temperature,
                                                                  waiting_client.customer.weight)

        meal_image = meal.load_images(waiting_client.customer.meal)
        meal_name = dish_name(waiting_client.customer.meal)
        new_meal = meal(waiting_client.customer.meal, meal_name, 1)
        new_order = order([new_meal], 'inprogress', (waiting_client.x, waiting_client.y))
        orders_list.append(new_order)
        print(new_order.table)
        meal_spawned = meal_spawn()
        free_deposits.remove(meal_spawned[2])
        undelivered_dish_list.append([meal_spawned[2], meal_spawned[0], meal_spawned[1], meal_image, new_order.table])

        if len(orders_list) == 3:
            orders_taken = True



        grid.draw_grid(Screen)
        #pygame.display.update()


        continue

    if len(undelivered_dish_list) > 0 and orders_taken == True and orders_delivered == False and carries_meal == False:

        current_meal = rchoice(undelivered_dish_list)
        a_star_path = (a_star_strategy((agent_x, agent_y), (current_meal[1], current_meal[2]), "Right", tuple_grid, G_cost))  # Generowana jest trasa do stolika klienta

        while waiter_step != len(a_star_path) - 1:  # rozpoczynamy sciezke do klienta
            if a_star_path[waiter_step] == 'Go':
                if first_angle == 0:
                    agent_x += 1
                elif first_angle == 90:
                    agent_y -= 1
                elif first_angle == 180:
                    agent_x -= 1
                elif first_angle == 270:
                    agent_y += 1
                agent(agent_x, agent_y)

            if a_star_path[waiter_step] == 'rotate Left':
                first_angle += 90
                if first_angle == 360:
                    first_angle = 0
                agentImg = search.angleSwitch(first_angle)
                agent(agent_x, agent_y)

            if a_star_path[waiter_step] == 'rotate Right':
                first_angle -= 90
                if first_angle < 0:
                    first_angle = 270
                agentImg = search.angleSwitch(first_angle)
                agent(agent_x, agent_y)

            obsticles()
            fresh_start = False
            last_x_coordinates = agent_x
            last_y_coordinates = agent_y

            waiter_step += 1



            grid.draw_grid(Screen)
            pygame.display.update()


            Screen.blit(Background, (0, 0))
            for customers in active_customers:
                customer_spawn(customers[1], customers[2], customers[3])
            for meal_in_list in undelivered_dish_list:
                dish(meal_in_list[1], meal_in_list[2], meal_in_list[3])

            clock.tick(10)
        carries_meal = True
        continue

    if len(undelivered_dish_list) > 0 and orders_taken == True and orders_delivered == False and carries_meal == True:
        a_star_path = (a_star_strategy((agent_x, agent_y), current_meal[4], "Right", tuple_grid, G_cost))  # Generowana jest trasa do stolika klienta

        while waiter_step != len(a_star_path) - 1:  # rozpoczynamy sciezke do klienta
            if a_star_path[waiter_step] == 'Go':
                if first_angle == 0:
                    agent_x += 1
                elif first_angle == 90:
                    agent_y -= 1
                elif first_angle == 180:
                    agent_x -= 1
                elif first_angle == 270:
                    agent_y += 1
                agent(agent_x, agent_y)

            if a_star_path[waiter_step] == 'rotate Left':
                first_angle += 90
                if first_angle == 360:
                    first_angle = 0
                agentImg = search.angleSwitch(first_angle)
                agent(agent_x, agent_y)

            if a_star_path[waiter_step] == 'rotate Right':
                first_angle -= 90
                if first_angle < 0:
                    first_angle = 270
                agentImg = search.angleSwitch(first_angle)
                agent(agent_x, agent_y)

            obsticles()

            fresh_start = False
            last_x_coordinates = agent_x
            last_y_coordinates = agent_y

            waiter_step += 1


            grid.draw_grid(Screen)
            pygame.display.update()


            Screen.blit(Background, (0, 0))
            for customers in active_customers:
                customer_spawn(customers[1], customers[2], customers[3])
            for meal_in_list in undelivered_dish_list:
                dish(meal_in_list[1], meal_in_list[2], meal_in_list[3])

            clock.tick(10)
        undelivered_dish_list.remove(current_meal)
        carries_meal = False
        continue
    grid.draw_grid(Screen)
    pygame.display.update()


    Screen.blit(Background, (0, 0))