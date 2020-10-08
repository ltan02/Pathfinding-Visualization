import pygame

##########################
# Color codes
##########################

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
orange = (255, 100, 10)
yellow = (255, 255, 0)
blue_green = (0, 255, 170)
marroon = (115, 0, 0)
lime = (180, 255, 100)
pink = (255, 100, 180)
purple = (240, 0, 255)
gray = (127, 127, 127)
magenta = (255, 0, 230)
brown = (100, 40, 0)
forest_green = (0, 50, 0)
navy_blue = (0, 0, 100)
rust = (210, 150, 75)
dandilion_yellow = (255, 200, 0)
highlighter = (255, 255, 100)
sky_blue = (0, 255, 255)
light_gray = (200, 200, 200)
dark_gray = (50, 50, 50)
tan = (230, 220, 170)
coffee_brown = (200, 190, 140)
moon_glow = (235, 245, 255)


class Node(object):
    def __init__(self, pos, color, cellSizeX, cellSizeY, gridX, gridY, win, gridSizeX, gridSizeY):
        self.pos = pos  # tuple (x, y))
        self.color = color

        #A*
        self.f = 0
        self.g = 0
        self.h = 0
        self.previous = None

        #Dijkstra's
        self.distance = float("inf")

        #Dijkstra and BFS
        self.parent = None

        #BFS
        self.discovered = False

        # Constants
        self.CELLSIZEX = cellSizeX
        self.CELLSIZEY = cellSizeY
        self.GRIDX = gridX
        self.GRIDY = gridY
        self.WIN = win
        self.GRIDSIZEX = gridSizeX
        self.GRIDSIZEY = gridSizeY

    def makeEmpty(self):
        self.color = white

    def makeStart(self):
        self.color = green

    def makeEnd(self):
        self.color = orange

    def makeBarrier(self):
        self.color = black

    def makeOpen(self):
        self.color = red

    def makeClosed(self):
        self.color = yellow

    def makePath(self):
        self.color = purple

    def isBarrier(self):
        return self.color == black

    def isEnd(self):
        return self.color == orange

    def isStart(self):
        return self.color == green

    def draw(self):
        x = (self.pos[0] * self.CELLSIZEX) + self.GRIDX + 1
        y = (self.pos[1] * self.CELLSIZEY) + self.GRIDY + 1
        width, height = self.CELLSIZEX, self.CELLSIZEY
        pygame.draw.rect(self.WIN, self.color, (x, y, width, height))

    def getNeighbours(self):
        neighbours = []
        dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        for dir in dirs:
            tempX = self.pos[0] + dir[0]
            tempY = self.pos[1] + dir[1]

            if 0 <= tempX < self.GRIDSIZEX and 0 <= tempY < self.GRIDSIZEY:
                neighbours.append((tempX, tempY))
        return neighbours

    def __eq__(self, other):
        return self.pos == other.pos

    def __repr__(self):
        return f"{self.pos} - g: {self.g} h: {self.h} f: {self.f}"

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f