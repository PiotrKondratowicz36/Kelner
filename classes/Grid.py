import pygame
from ConstantValues import Width, Collumns, Rows


class Grid:

    def __init__(self):
        self.gridArray = []

    def drawGrid(self, Screen):
        for x in range(Rows):
            pygame.draw.line(Screen, (0, 0, 0), (0, x * 50), (Width, x * 50))
            for y in range(Collumns):
                pygame.draw.line(Screen, (0, 0, 0), (y * 50, 0), (y * 50, Width))

    def colliders(self):
        collisionKitchen = []
        for x in range(8, 16):
            for y in range(0, 16):
                if x in [8, 9, 10, 11] and y not in [4, 5] or x in [12, 13] and y not in [4, 5, 6, 7, 8, 9, 10,
                                                                                          11] or x in [14, 15]:
                    collisionKitchen.append([x, y])
        collisionRestauran = [[0, 0], [0, 15], [1, 0], [1, 3], [1, 4], [1, 7], [1, 8],
                              [1, 11], [1, 12], [2, 0], [2, 3], [2, 4], [2, 7], [2, 8],
                              [2, 11], [2, 12],
                              [7, 0], [7, 15], [5, 0], [5, 3], [5, 4], [5, 7], [5, 8],
                              [5, 11], [5, 12], [6, 0], [6, 3], [6, 4], [6, 7], [6, 8],
                              [6, 11], [6, 12]]
        collisionFinal = collisionRestauran + collisionKitchen
        for c in collisionFinal:
            if c in self.gridArray:
                self.gridArray.remove(c)

    def neighbors(self, node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            neighbor = [node[0] + dir[0], node[1] + dir[1]]
            if neighbor in self.gridArray:
                result.append(neighbor)
        return result

    def createGridArray(self):
        for x in range(Collumns):
            for y in range(Rows):
                self.gridArray.append([x, y])
