import pygame
from classes.Grid import Grid
from classes.Search import Search
from classes.ConstantValues import Height, Width, SquareSize

testPath = [(3, 1), (3, 7), (13, 4), (3, 7), (4, 11), (13, 5)]
i = 0

# Game screen with grid
pygame.init()
clock = pygame.time.Clock()
Screen = pygame.display.set_mode((Height, Width))
pygame.display.set_caption("Kelner")
Background = pygame.image.load('../grafiki/restauracja.png')
grid = Grid()

search = Search(testPath[1], testPath[5])
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
    clock.tick(5)
