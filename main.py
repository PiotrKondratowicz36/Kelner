from time import sleep

import pygame
from random import randint

#Start gry
pygame.init()
clock = pygame.time.Clock()

#Ekran gry
height, width = 800, 800
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("Kelner")


#Tło
background = pygame.image.load('grafiki\\restauracja.png')

#Agent
agentImg = pygame.image.load('grafiki\\kelner.png')
agentX = 1
agentY = 1

def agent(x, y):
    posX = (squareSize * x)
    posY = (squareSize * y)
    screen.blit(agentImg, (posX,posY)) #draws something on the game screen

#siatka
collumns, rows = 16, 16
squareSize = width//collumns
squareList = []
for x in range(collumns):
    for y in range(rows):
        squareList.append([x,y])
i = 0
def drawGrid():
    for x in range(0, width, squareSize):
        for y in range(0, height, squareSize):
            rect = pygame.Rect(x,y,squareSize,squareSize)
            pygame.draw.rect(screen,(0,0,0),rect,1)

#Zamówienia




#Symulacja
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    drawGrid()
    agentX, agentY = squareList[i]
    i = i + 1
    if i == 256:
        i = 0
    agent(agentX, agentY)
    pygame.display.update()
    clock.tick(1)
