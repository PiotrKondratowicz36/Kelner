import pygame
from classes.Grid import Grid
from classes.ConstantValues import Height, Width, SquareSize

#Game screen with grid
pygame.init()
clock = pygame.time.Clock()
Screen = pygame.display.set_mode((Height, Width))
pygame.display.set_caption("Kelner")
Background = pygame.image.load('../grafiki/restauracja.png')
grid = Grid()
grid.createGridArray()
grid.colliders()

#Agent
agentImg = pygame.image.load('../grafiki/kelner.png')
agentX = 1
agentY = 1
i = 0
def agent(x, y):
    posX = (SquareSize * x)
    posY = (SquareSize * y)
    Screen.blit(agentImg, (posX,posY))

#Symulacja
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Screen.blit(Background, (0, 0))
    grid.drawGrid(Screen)
    agentX, agentY = grid.gridArray[i]
    i = i + 1
    if i == len(grid.gridArray):
        i = 0
    agent(agentX, agentY)
    pygame.display.update()
    clock.tick(30)