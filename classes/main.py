import pygame.image
from classes.values_and_grids.grid import *
from classes.decision_tree.decision_tree import *
from classes.searching.search import Search
from classes.objects_classes.customers import *
from classes.objects_classes.order import *
from classes.objects_classes.meal import *
from classes.neural_networks.recognize_single_image import *
import time
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
speed = 40

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


# methods

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


def obstacles():
    for i in range(0, len(G_cost) - 1):
        for j in range(0, len(G_cost[i]) - 1):
            if G_cost[i][j] == water:

                woda_png = '../grafiki/woda.png'
                obst(i, j, woda_png)
            elif G_cost[i][j] == banan:
                banan_png = '../grafiki/banan.png'
                obst(i, j, banan_png)


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

    if len(orders_list) == 3:
        orders_taken = True
    else:
        orders_taken = False

    # SPAWNOWANIE KLIENTOW
    if len(active_customers) < customers_limit:
        i = customers_limit - len(active_customers)
        for _ in range(i):
            customer = rchoice(all_customers)
            customer_spawned = customer.customer_spawn()
            used_tables.append(Table(customer_spawned[0], customer_spawned[1], customer))
            active_customers.append(
                [customer_spawned[3], customer_spawned[0], customer_spawned[1], pygame.image.load(customer_spawned[2]),
                 'waiting', 0, random.randint(5, 10), customer_spawned[2]])
            free_seats.remove(customer_spawned[3])

        for customers in active_customers:
            customer_spawn(customers[1], customers[2], customers[3])

    else:
        for customers in active_customers:
            customer_spawn(customers[1], customers[2], customers[3])

            if customers[4] == 'eating':
                if customers[5] == customers[6]:
                    customers[3] = pygame.image.load('../grafiki/bezjedzenia50x50.jpg')
                    customers [7] = '../grafiki/bezjedzenia50x50.jpg'
                else:
                    customers[5] += 1

        if orders_taken == True:
            for meal_in_list in undelivered_dish_list:
                dish(meal_in_list[1], meal_in_list[2], meal_in_list[3])


    # ZBIERANIE ZAMOWIEN
    if orders_taken == False:

        eating_client = rchoice(used_tables)
        while eating_client.order:
            eating_client = rchoice(used_tables)
        a_star_path = (
            a_star_strategy((agent_x, agent_y), (eating_client.x, eating_client.y), "Right", tuple_grid, G_cost))

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

            obstacles()
            fresh_start = False
            last_x_coordinates = agent_x
            last_y_coordinates = agent_y
            clock.tick(speed)
            waiter_step += 1

            grid.draw_grid(Screen)
            pygame.display.update()

            Screen.blit(Background, (0, 0))
            for customers in active_customers:
                customer_spawn(customers[1], customers[2], customers[3])

        # Screen.blit(Background, (0, 0))
        # akcja gdy kelner jest przy celu

        eating_client.order = True
        eating_client.customer.meal = predict_from_decision_tree(eating_client.customer.age,
                                                                 eating_client.customer.sex,
                                                                 eating_client.customer.vegetarian,
                                                                 eating_client.customer.budget,
                                                                 eating_client.customer.d_type,
                                                                 eating_client.customer.temperature,
                                                                 eating_client.customer.weight)

        meal_image = meal.load_images(eating_client.customer.meal)
        meal_name = dish_name(eating_client.customer.meal)
        new_meal = meal(eating_client.customer.meal, meal_name, 1)
        new_order = order([new_meal], 'inprogress', (eating_client.x, eating_client.y))
        orders_list.append(new_order)
        print(new_order.table)
        meal_spawned = meal_spawn()
        free_deposits.remove(meal_spawned[2])
        undelivered_dish_list.append([meal_spawned[2], meal_spawned[0], meal_spawned[1], meal_image, new_order.table])

        grid.draw_grid(Screen)
        # pygame.display.update()

        continue

    # POJSCIE DO KUCHNI PO ZAMOWIENIE

    if len(undelivered_dish_list) > 0 and orders_taken == True and orders_delivered == False and carries_meal == False:

        current_meal = rchoice(undelivered_dish_list)
        a_star_path = (a_star_strategy((agent_x, agent_y), (current_meal[1], current_meal[2]), "Right", tuple_grid,
                                       G_cost))

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

            obstacles()
            last_x_coordinates = agent_x
            last_y_coordinates = agent_y

            waiter_step += 1

            grid.draw_grid(Screen)
            pygame.display.update()
            clock.tick(speed)

            Screen.blit(Background, (0, 0))
            for customers in active_customers:
                customer_spawn(customers[1], customers[2], customers[3])
            for meal_in_list in undelivered_dish_list:
                dish(meal_in_list[1], meal_in_list[2], meal_in_list[3])

        carries_meal = True
        continue

    # POJSCIE DO KLIENTA Z JEGO ZAMOWIENIEM

    if len(undelivered_dish_list) > 0 and orders_taken == True and orders_delivered == False and carries_meal == True:

        a_star_path = (a_star_strategy((agent_x, agent_y), current_meal[4], "Right", tuple_grid,
                                       G_cost))

        for waiting_customer in active_customers:
            if (waiting_customer[1],waiting_customer[2]) == current_meal[4]:
                current_customer = waiting_customer
                break

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

            obstacles()
            fresh_start = False
            last_x_coordinates = agent_x
            last_y_coordinates = agent_y

            waiter_step += 1

            grid.draw_grid(Screen)
            pygame.display.update()
            clock.tick(speed)

            Screen.blit(Background, (0, 0))
            for customers in active_customers:
                customer_spawn(customers[1], customers[2], customers[3])
            for meal_in_list in undelivered_dish_list:
                dish(meal_in_list[1], meal_in_list[2], meal_in_list[3])

        current_customer[3] = pygame.image.load('../grafiki/zjedzeniem50x50.jpg')
        current_customer[7] = '../grafiki/zjedzeniem50x50.jpg'
        current_customer[4] = 'eating'
        print(f"klient ze stolika {current_customer[0]} zaczal wlasnie jesc")

        undelivered_dish_list.remove(current_meal)
        carries_meal = False
        continue

    # SPRAWDZANIE U KLIENTOW CZY JUZ ZJEDLI

    if len(undelivered_dish_list) == 0:

        eating_client = rchoice(active_customers)
        a_star_path = (
            a_star_strategy((agent_x, agent_y), (eating_client[1], eating_client[2]), "Right", tuple_grid, G_cost))

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

            clock.tick(speed)

            last_x_coordinates = agent_x
            last_y_coordinates = agent_y

            waiter_step += 1
            obstacles()
            grid.draw_grid(Screen)
            pygame.display.update()
            Screen.blit(Background, (0, 0))
            for customers in active_customers:
                customer_spawn(customers[1], customers[2], customers[3])

        ocena = classify(model, image_transforms, eating_client[7], platestates)
        if ocena == 'Talerz jest pusty':
            print(ocena)
            print(f"Klient ze stolika {eating_client[0]} wlasnie zjadl")