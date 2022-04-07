import queue
import time
from math import atan2, degrees, pi
import pygame.transform
from classes.Grid import Grid


class Search:

    def __init__(self, start, goal):
        self.frontier = queue.Queue()
        self.came_from = dict()
        self.path = []
        self.start = start
        self.goal = goal

    def reachingGoal(self):
        grid = Grid()
        grid.createGridArray()
        grid.colliders()
        self.frontier.put(self.start)
        self.came_from[self.start] = None
        print(grid.gridArray)

        while not self.frontier.empty():
            current = self.frontier.get()

            if current == self.goal:
                break

            for nextPoint in grid.neighbors(current):
                nextPoint = tuple(nextPoint)
                if nextPoint not in self.came_from:
                    self.frontier.put(nextPoint)
                    self.came_from[nextPoint] = current

    def pathCreating(self):
        current = self.goal
        while current != self.start:
            self.path.append(current)
            current = self.came_from[current]
        self.path.append(self.start)
        self.path.reverse()

    def rotationCount(self, xy1, xy2):
        dx = xy2[0] - xy1[0]
        dy = xy2[1] - xy1[1]
        rads = atan2(-dy, dx)
        rads %= 2 * pi
        degs = degrees(rads)
        return degs

    def angleSwitch(self, angle):
        if angle == 0:
            image = pygame.image.load('../grafiki/kelner_prawo.png')
        if angle == 90:
            image = pygame.image.load('../grafiki/kelner_gora.png')
        if angle == 180:
            image = pygame.image.load('../grafiki/kelner_lewo.png')
        if angle == 270:
            image = pygame.image.load('../grafiki/kelner.png')
        return image
