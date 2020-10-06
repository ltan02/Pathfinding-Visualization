import pygame
from pygame.locals import *
import sys
from Node import Node
from astar import astar

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
maroon = (115, 0, 0)
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

##########################
# Global Variables
##########################

pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont("Comic Sans MS", 15, True)
CLOCK = pygame.time.Clock()
SCREENWIDTH, SCREENHEIGHT = 1650, 1000
WIN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GRIDX = 25
SIDEBAR = 200
GRIDY = 100
GRIDWIDTH = SCREENWIDTH - GRIDX - SIDEBAR
GRIDHEIGHT = SCREENHEIGHT - (GRIDY * 2)
GRIDSIZEX = 35
GRIDSIZEY = 20
CELLSIZEX = GRIDWIDTH / GRIDSIZEX
CELLSIZEY = GRIDHEIGHT / GRIDSIZEY

##########################
# Helper Functions
##########################

def drawGrid():
    for x in range(GRIDSIZEX+1):
        pygame.draw.line(WIN, black, (GRIDX + (CELLSIZEX * x), GRIDY), (GRIDX + (CELLSIZEX * x), GRIDY + GRIDHEIGHT))

    for y in range(GRIDSIZEY+1):
        pygame.draw.line(WIN, black, (GRIDX, GRIDY + (CELLSIZEY * y)), (GRIDX + GRIDWIDTH, GRIDY + (CELLSIZEY * y)))


def drawBackground():
    WIN.fill(white)
    pygame.draw.rect(WIN, black, (GRIDX, GRIDY, GRIDWIDTH, GRIDHEIGHT), 1)

    # Start node
    pygame.draw.rect(WIN, green, (40, 765, 25, 25))
    textSurface = FONT.render("Start Node", False, (0, 0, 0))
    WIN.blit(textSurface, (75, 765))

    # End Node
    pygame.draw.rect(WIN, orange, (175, 765, 25, 25))
    textSurface = FONT.render("End Node", False, (0, 0, 0))
    WIN.blit(textSurface, (210, 765))

    # Barrier Node
    pygame.draw.rect(WIN, black, (300, 765, 25, 25))
    textSurface = FONT.render("Barrier Node", False, (0, 0, 0))
    WIN.blit(textSurface, (335, 765))

    # Unvisited Node
    pygame.draw.rect(WIN, black, (445, 765, 25, 25), 1)
    textSurface = FONT.render("Unvisited Node", False, (0, 0, 0))
    WIN.blit(textSurface, (480, 765))

    # Visited Nodes
    pygame.draw.rect(WIN, red, (600, 765, 25, 25))
    pygame.draw.rect(WIN, yellow, (630, 765, 25, 25))
    textSurface = FONT.render("Visited Nodes", False, (0, 0, 0))
    WIN.blit(textSurface, (665, 765))

    # Shortest-path Node
    pygame.draw.rect(WIN, purple, (780, 765, 25, 25))
    textSurface = FONT.render("Shortest-path Node", False, (0, 0, 0))
    WIN.blit(textSurface, (815, 765))


def drawPathfindingAlgorithmButton():
    pygame.draw.rect(WIN, light_gray, (100, 10, 270, 80))
    font = pygame.font.SysFont("Arial", 40, False)
    textSurface = font.render("Choose Pathfinder", False, (0, 0, 0))
    WIN.blit(textSurface, (107, 38))


def pathfindingAlgorithmButtonPressed(posx, posy):
    return 100 <= posx <= 370 and 10 <= posy <= 90


def runPathfindingButton():
    pass


def runPathfindingButtonPressed():
    pass


def stopPathfindingButton():
    pass


def stopPathfindingButtonPressed():
    pass


def drawMazeGenerationButton():
    pass


def mazeGenerationButtonPressed():
    pass


def runMazeGenerationButton():
    pass


def runMazeGenerationButtonPressed():
    pass


def stopMazeGenerationButton():
    pass


def stopMazeGenerationButtonPressed():
    pass


def redrawGameWindow(mode):
    WIN.fill(white)
    if mode == "main":
        for row in range(len(nodes)):
            for col in nodes[row]:
                col.draw()

        drawGrid()

        drawPathfindingAlgorithmButton()
        runPathfindingButton()
        stopPathfindingButton()
        # Choose pathfinding algorithm
        # Run pathfinding button
        # Stop pathfinding button

        drawMazeGenerationButton()
        runMazeGenerationButton()
        stopMazeGenerationButton()
        # Choose maze generation algorithm
        # Run maze generation button
        # Stop maze generation button

        # Select Grid Size (rows and cols)
        # Select speed of algorithm  (frame rate)

        # Draw the information about the different colors
    elif mode == "choosePathfinder":
        pass

    pygame.display.update()


def createNodes():
    nodes = []
    for row in range(GRIDSIZEY):
        temp = []
        for col in range(GRIDSIZEX):
            temp.append(Node((col, row), white, CELLSIZEX, CELLSIZEY, GRIDX, GRIDY, WIN, GRIDSIZEX, GRIDSIZEY))
        nodes.append(temp)
    return nodes

##########################
# Choose Pathfinding Algorithm Function
##########################

def choosePathfinder():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                sys.exit()

        redrawGameWindow("choosePathfinder")



##########################
# Main Function
##########################

def main():
    global nodes
    pygame.display.set_caption("Pathfining Algorithm Visualizer")
    nodes = createNodes()
    start = False
    end = False
    startNode = None
    endNode = None
    do_astar = False
    openSet = []
    closedSet = []
    main_screen = True
    while main_screen:
        CLOCK.tick(60)

        for event in pygame.event.get():  # checking for events
            if event.type == QUIT:
                main_screen = False
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col = int((pos[0] - GRIDX) // CELLSIZEX)
                row = int((pos[1] - GRIDY) // CELLSIZEY)
                if 0 <= row < GRIDSIZEY and 0 <= col < GRIDSIZEX:
                    currNode = nodes[row][col]
                    if not (start) and not(currNode.isEnd()):
                        currNode.makeStart()
                        startNode = currNode
                        start = True
                    elif not (end) and not(currNode.isStart()):
                        currNode.makeEnd()
                        endNode = currNode
                        end = True
                    elif not(currNode.isEnd()) and not(currNode.isStart()):
                        nodes[row][col].makeBarrier()

                if pathfindingAlgorithmButtonPressed(pos[0], pos[1]):
                    choosePathfinder()

        keys = pygame.key.get_pressed()  # to check key pressed (or held down)
        if keys[pygame.K_BACKSPACE]:
            nodes = createNodes()
            start = False
            end = False
            startNode = None
            endNode = None
            openSet = []
            closedSet = []
        if keys[pygame.K_SPACE] or do_astar:
            if do_astar == False:
                openSet.append(startNode)
            if len(openSet) > 0:
                loop = astar(startNode, endNode, nodes, openSet, closedSet)
                if loop != True:
                    openSet, closedSet = loop
                    do_astar = True
                else:
                    do_astar = False
            else:
                print("No solution found")
                do_astar = False

        redrawGameWindow("main")


main()
