import pygame
from pygame.locals import *
import sys
from Node import Node
from astar import astar
from Button import Button

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
    for x in range(GRIDSIZEX + 1):
        pygame.draw.line(WIN, black, (GRIDX + (CELLSIZEX * x), GRIDY), (GRIDX + (CELLSIZEX * x), GRIDY + GRIDHEIGHT))

    for y in range(GRIDSIZEY + 1):
        pygame.draw.line(WIN, black, (GRIDX, GRIDY + (CELLSIZEY * y)), (GRIDX + GRIDWIDTH, GRIDY + (CELLSIZEY * y)))


def drawKey(x, y, size, color, font, text, border=0):
    pygame.draw.rect(WIN, color, (x, y, size, size), border)
    textSurface = font.render(text, True, (0, 0, 0))
    WIN.blit(textSurface, (x + size + 10, y + (size / 2) - 5))
    return size + 10 + textSurface.get_width()


def drawBackground():
    WIN.fill(white)
    pygame.draw.rect(WIN, black, (GRIDX, GRIDY, GRIDWIDTH, GRIDHEIGHT), 1)

    font = pygame.font.SysFont("Arial", 20)
    square_size = 40

    yPos = GRIDHEIGHT + GRIDY + 20
    xPos = GRIDX + 20

    # Start node
    keyWidth = drawKey(xPos, yPos, square_size, green, font, "Start Node")
    keyWidth += 30

    # End Node
    keyWidth += drawKey(xPos + keyWidth, yPos, square_size, orange, font, "End Node")
    keyWidth += 30

    # Barrier Node
    keyWidth += drawKey(xPos + keyWidth, yPos, square_size, (0, 0, 0), font, "Barrier Node")
    keyWidth += 30

    # Unvisited Node
    keyWidth += drawKey(xPos + keyWidth, yPos, square_size, black, font, "Unvisited Node", 1)
    keyWidth += 30

    # Visited Nodes
    keyWidth += drawKey(xPos + keyWidth, yPos, square_size, red, font, "Closed Node")
    keyWidth += 30

    keyWidth += drawKey(xPos + keyWidth, yPos, square_size, yellow, font, "Open Node")
    keyWidth += 30

    # Shortest-path Node
    keyWidth += drawKey(xPos + keyWidth, yPos, square_size, purple, font, "Shortest-path Node")

def generateButtons():
    buttons = []
    buttons.append(Button(100, 10, 270, 80, light_gray, "Choose Pathfinder", 40, (0, 0, 0), "Arial", WIN))
    buttons.append(Button(390, 10, 100, 35, light_gray, "Run", 25, (0, 0, 0), "Arial", WIN))
    buttons.append(Button(390, 55, 100, 35, light_gray, "Stop", 25, (0, 0, 0), "Arial", WIN))
    buttons.append(Button(1000, 10, 270, 80, light_gray, "Choose Maze Generator", 30, (0, 0, 0), "Arial", WIN))
    buttons.append(Button(1290, 10, 100, 35, light_gray, "Run", 25, (0, 0, 0), "Arial", WIN))
    buttons.append(Button(1290, 55, 100, 35, light_gray, "Stop", 25, (0, 0, 0), "Arial", WIN))
    return buttons


def redrawGameWindow():
    drawBackground()

    for row in range(len(nodes)):
        for col in nodes[row]:
            col.draw()

    drawGrid()

    for button in buttons:
        button.draw()

    # Choose maze generation algorithm
    # Run maze generation button
    # Stop maze generation button

    # Select Grid Size (rows and cols)
    # Select speed of algorithm  (frame rate)

    # Draw the information about the different colors

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
# Main Function
##########################


def main():
    global nodes, buttons
    pygame.display.set_caption("Pathfining Algorithm Visualizer")
    nodes = createNodes()
    start = False
    end = False
    startNode = None
    endNode = None
    do_astar = False
    openSet = []
    closedSet = []
    buttons = generateButtons()
    while True:
        CLOCK.tick(60)

        for event in pygame.event.get():  # checking for events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col = int((pos[0] - GRIDX) // CELLSIZEX)
                row = int((pos[1] - GRIDY) // CELLSIZEY)
                if 0 <= row < GRIDSIZEY and 0 <= col < GRIDSIZEX:
                    currNode = nodes[row][col]
                    if not (start) and not (currNode.isEnd()):
                        currNode.makeStart()
                        startNode = currNode
                        start = True
                    elif not (end) and not (currNode.isStart()):
                        currNode.makeEnd()
                        endNode = currNode
                        end = True
                    elif not (currNode.isEnd()) and not (currNode.isStart()):
                        nodes[row][col].makeBarrier()

                for button in buttons:
                    if button.text == "Choose Pathfinder" and button.isPressed(pos[0], pos[1]):
                        button.pressed = True

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

        redrawGameWindow()


main()
