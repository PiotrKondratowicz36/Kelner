from classes.values_and_grids.ConstantValues import *
from classes.values_and_grids.Grid import *
from classes.values_and_grids.GridsAndPaths import *
from classes.decision_tree.Decision_Tree import *
from classes.searching.Search import Search
from classes.neural_networks.recognizesingleimage import *
import time


# Game screen with grid
pygame.init()
clock = pygame.time.Clock()
Screen = pygame.display.set_mode((Height, Width))
pygame.display.set_caption("Kelner")
Background = pygame.image.load('../grafiki/restauracja.png')
grid = Grid()
search = Search(testPath[1], testPath[5])


def agent(x, y):
    pos_x = (SquareSize * x)
    pos_y = (SquareSize * y)
    Screen.blit(agentImg, (pos_x, pos_y))


def dish(x, y, img):
    pos_x = (SquareSize * x)
    pos_y = (SquareSize * y)
    Screen.blit(img, (pos_x, pos_y))


# Symulacja
running = True
j = 0
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
    plate1 = pygame.image.load('../grafiki/zjedzeniem50x50.jpg')
    plate2 = pygame.image.load('../grafiki/bezjedzenia50x50.jpg')
    # dish(2, 3, plate1)
    dish(2, 3, plate2)

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
    clock.tick(3)
    if j == len(a_star_path) - 1:
        classify(model, image_transforms, 'neural_networks/testplates/bezjedzenia.jpg', platestates)
        predict = predict_from_decision_tree(35, 2, 0, 3, 1, 2, 1)
        dish_name(predict)
        grid.drawGrid(Screen)
        pygame.display.update()
        time.sleep(20)
