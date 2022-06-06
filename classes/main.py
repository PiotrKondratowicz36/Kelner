from classes.values_and_grids.ConstantValues import *
from classes.values_and_grids.Grid import *
from classes.values_and_grids.GridsAndPaths import *
from classes.decision_tree.Decision_Tree import *
from classes.searching.Search import Search
from classes.neural_networks.recognizesingleimage import *
from classes.objects_classes.Customer import *
import time
import random


# Game screen with grid
pygame.init()
clock = pygame.time.Clock()
Screen = pygame.display.set_mode((Height, Width))
pygame.display.set_caption("Kelner")
Background = pygame.image.load('../grafiki/restauracja.png')
grid = Grid()
search = Search(testPath[1], testPath[5])
cust = Customers(1)





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
cust_iter = 0
cust_timing = 0
priority = False
active_customers = []

while running:
    if cust_iter > 10:
        flag = False
        priority = False
        cust_iter = 0
        cust_timing = 0

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
    plate1 = pygame.image.load('../grafiki/zjedzeniem50x50.jpg')
    plate2 = pygame.image.load('../grafiki/bezjedzenia50x50.jpg')
    # dish(2, 3, plate1)
    dish(2, 3, plate2)

    #klient_stuff_ghetto_code

    #losuje liczbe, jesli trafi to przechodzi do spawnowania nowego klienta
    customer_lucky_num = random.randint(0, 3)
    if (customer_lucky_num == 3 and len(free_seats) > 0 and flag == False) or priority == True:

        #warunek stania przy drzwiach
        if cust_timing == 0:

            res = cust.customer_spawn()
            cust_timing = 1
            priority == True
            customer_movement(4, 15, res[2]) #spawn przy wejsciu

            for customers in active_customers:
                customer_movement(customers[1], customers[2], customers[3])  #printuj wszystkich klientow

            active_customers.append([res[3],res[0],res[1],res[2]]) #tablica tablic z obecnymi klientami
            free_seats.remove(res[3]) #zajmuje miejsce
        else:
            for customers in active_customers:
                customer_movement(customers[1], customers[2], customers[3]) #printuj klientow
    else:
        for customers in active_customers:
            customer_movement(customers[1], customers[2], customers[3])

    cust_iter = cust_iter + 1


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
    clock.tick(1)

    if j == len(a_star_path) - 1:
        classify(model, image_transforms, 'neural_networks/testplates/bezjedzenia.jpg', platestates)
        predict = predict_from_decision_tree(35, 2, 0, 3, 1, 2, 1)
        dish_name(predict)
        grid.drawGrid(Screen)
        pygame.display.update()
        time.sleep(6)
