import pygame
from pygame.locals import *
import sys

##########################
# Importing files to main
##########################

from Classes.Node import *
from Classes.Button import *
from MazeGen.RecursiveMaze import *
from Pathfinder.astar import *
from Pathfinder.astar import *

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
    buttons.append(Button("Choose Pathfinder Button", 100, 10, 270, 80, "Choose Pathfinder", 40, WIN))
    buttons.append(Button("Choose Maze Generator Button", 400, 10, 270, 80, "Choose Maze Generator", 30, WIN))
    buttons.append(Button("Reset Button", 1170, 10, 100, 35, "Reset", 25, WIN))
    buttons.append(Button("Run Button", 1290, 10, 100, 35, "Run", 25, WIN))
    buttons.append(Button("Stop Button", 1290, 55, 100, 35, "Stop", 25, WIN))
    buttons.append(Button("Resume Button", 1170, 55, 100, 35, "Resume", 25, WIN, False))
    return buttons


def generateDropDownPathfinder():
    dropDown = []
    dropDown.append(Button("A* Algorithm Button", 100, 90, 270, 80, "A* Algorithm", 40, WIN, False))
    dropDown.append(Button("Dijkstra's Algorithm Button", 100, 170, 270, 80, "Dijkstra's Algorithm", 40, WIN, False))
    return dropDown


def generateDropDownMaze():
    dropDown = []
    return dropDown


def createNodes():
    nodes = []
    for row in range(GRIDSIZEY):
        temp = []
        for col in range(GRIDSIZEX):
            temp.append(Node((col, row), white, CELLSIZEX, CELLSIZEY, GRIDX, GRIDY, WIN, GRIDSIZEX, GRIDSIZEY))
        nodes.append(temp)
    return nodes


def dropDownMode(dropDownButtons):
    if len(dropDownButtons) > 0:
        run = True
        while run:
            for dropDown in dropDownButtons:
                dropDown.show = True

            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    if buttons[0].isPressed(pos[0], pos[1]):
                        buttons[0].pressed = False
                        run = False
                        continue

                    for button in dropDownButtons:
                        if button.isPressed(pos[0], pos[1]):
                            buttons[0].text = button.text
                            run = False

            redrawGameWindow(dropDownButtons)

        for dropDownButton in dropDownButtons:
            dropDownButton.show = False


def redrawGameWindow(dropDownButtons=[]):
    drawBackground()

    for row in range(len(nodes)):
        for col in nodes[row]:
            col.draw()

    drawGrid()

    for button in buttons:
        button.draw()

    for dropDown in dropDownButtons:
        dropDown.draw()

    # Choose maze generation algorithm
    # Run maze generation button
    # Stop maze generation button

    # Select Grid Size (rows and cols)
    # Select speed of algorithm  (frame rate)

    # Draw the information about the different colors

    pygame.display.update()

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

    do_dijkstra = False
    unexplored = []

    buttons = generateButtons()

    midrun = False
    pathfinderDropDown = generateDropDownPathfinder()
    mazeDropDown = generateDropDownMaze()
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
                    if not(start) and not(currNode.isEnd()):
                        currNode.makeStart()
                        currNode.distance = 0
                        startNode = currNode
                        start = True
                    elif not(end) and not(currNode.isStart()):
                        currNode.makeEnd()
                        endNode = currNode
                        end = True
                    elif not(currNode.isEnd()) and not(currNode.isStart()):
                        currNode.makeBarrier()

                for button in buttons:
                    if button.isPressed(pos[0], pos[1]):
                        button.pressed = True
                        if button.name == "Run Button" and button.pressed:
                            if start and end:
                                if buttons[0].text == "A* Algorithm":
                                    do_astar = True
                                    openSet.append(startNode)
                                elif buttons[0].text == "Dijkstra's Algorithm":
                                    do_dijkstra = True
                                    unexplored = [nodes[row][col] for row in range(len(nodes)) for col in range(len(nodes[row]))]
                                else:
                                    button.pressed = False
                            else:
                                button.pressed = False
                        if button.name == "Reset Button":
                            nodes = createNodes()
                            start = False
                            end = False
                            startNode = None
                            endNode = None
                            openSet = []
                            closedSet = []
                            button.pressed = False
                            midrun = False
                            pathfinderRunning = ""
                            buttons[5].show = False
                            buttons[0].text = "Choose Pathfinder"
                            buttons[1].text = "Choose Maze Generator"
                            for button in buttons:
                                button.pressed = False
                        if button.name == "Stop Button":
                            if buttons[3].pressed:
                                buttons[5].show = True
                                if do_astar:
                                    do_astar = False
                                    button.pressed = False
                                    pathfinderRunning = "astar"
                            else:
                                button.pressed = False
                        if button.name == "Resume Button":
                            if midrun and pathfinderRunning == "astar":
                                do_astar = True
                                button.show = False
                                button.pressed = False
                        if button.name == "Choose Pathfinder Button":
                            if not(midrun):
                                button.text = "Choose Pathfinder"
                                dropDownMode(pathfinderDropDown)
                                buttons[0].pressed = False
                            else:
                                button.pressed = False
                        if button.name == "Choose Maze Generator Button":
                            if not(midrun):
                                dropDownMode(mazeDropDown)
                                buttons[1].pressed = False
                            else:
                                button.pressed = False

            if pygame.mouse.get_pressed()[2]:
                pos2 = pygame.mouse.get_pos()
                col2 = int((pos2[0] - GRIDX) // CELLSIZEX)
                row2 = int((pos2[1] - GRIDY) // CELLSIZEY)
                if 0 <= row2 < GRIDSIZEY and 0 <= col2 < GRIDSIZEX:
                    node = nodes[row2][col2]
                    if node.isBarrier() and not(node.isEnd()) and not(node.isStart()):
                        node.makeEmpty()
                    elif node.isStart() and not(node.isEnd()) and not(node.isBarrier()):
                        node.makeEmpty()
                        node.distance = float("inf")
                        startNode = None
                        start = False
                    elif node.isEnd() and not(node.isStart()) and not(node.isBarrier()):
                        node.makeEmpty()
                        endNode = None
                        end = False

        if do_astar:
            if len(openSet) > 0:
                loop = astar(startNode, endNode, nodes, openSet, closedSet)
                if loop != True:
                    openSet, closedSet = loop
                    do_astar = True
                    midrun = True
                else:
                    do_astar = False
                    midrun = False
                    buttons[3].pressed = False
            else:
                print("No solution found")
                do_astar = False
                midrun = False
                buttons[3].pressed = False
        elif do_dijkstra:
            if len(unexplored) > 0:
                loop = dijkstra(endNode, nodes, unexplored)
                if loop != True:
                    unexplored = loop
                    do_dijkstra = True
                    midrun = True
                else:
                    do_dijkstra = False
                    midrun = False
                    buttons[3].pressed = False

        redrawGameWindow()


main()