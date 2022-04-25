import pygame
from classes.Grid import *
from classes.Search import Search
from classes.ConstantValues import Height, Width, SquareSize
from SearchStrategy import *

testPath = [(1, 1), (2, 13), (13, 4), (3, 7), (4, 11), (3, 0)]
i = 0

# Game screen with grid
pygame.init()
clock = pygame.time.Clock()
Screen = pygame.display.set_mode((Height, Width))
pygame.display.set_caption("Kelner")
Background = pygame.image.load('../grafiki/restauracja.png')
grid = Grid()
search = Search(testPath[1], testPath[5])

############################
# obszar testowy bfs + succ, do dokonczenia movement na podstawie zwracanej sciezki (here linijka 25)
temp_grd = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [1, 1], [1, 2], [1, 5], [1, 6], [1, 9], [1, 10], [1, 13], [1, 14], [1, 15], [2, 1], [2, 2], [2, 5], [2, 6], [2, 9], [2, 10], [2, 13], [2, 14], [2, 15], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [3, 15], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14], [4, 15], [5, 1], [5, 2], [5, 5], [5, 6], [5, 9], [5, 10], [5, 13], [5, 14], [5, 15], [6, 1], [6, 2], [6, 5], [6, 6], [6, 9], [6, 10], [6, 13], [6, 14], [6, 15], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [8, 4], [8, 5], [9, 4], [9, 5], [10, 4], [10, 5], [11, 4], [11, 5], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [13, 4], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11]]
tuple_grid = [tuple(x) for x in temp_grd]
#print(tuple_grid)

print(bfs((2,13), (3,0), "Left", tuple_grid))

############################


search.reachingGoal()
search.pathCreating()


def agent(x, y):
    posX = (SquareSize * x)
    posY = (SquareSize * y)
    Screen.blit(agentImg, (posX, posY))


agentX = 0
agentY = 0
agentImg = pygame.image.load('../grafiki/kelner.png')

# Symulacja
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Screen.blit(Background, (0, 0))
    agentX, agentY = search.path[i]  # Przypisanie wspolrzednym agenta nastepnej wspolrzednej na drodze do celu
    agent(agentX, agentY)  # Narysowanie agenta
    if i != len(search.path) - 1:
        agentImg = search.angleSwitch(search.rotationCount(search.path[i], search.path[i + 1]))  # Obrot agenta
    i = i + 1
    if i == len(search.path):
        i = 0
    grid.drawGrid(Screen)
    pygame.display.update()
    clock.tick(1)


