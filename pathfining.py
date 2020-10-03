import pygame
from pygame.locals import *
import sys
import heapq

##########################
# Color codes
##########################

white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))

##########################
# Helper Functions
##########################

def drawGrid(nodes):
	for x in range(GRIDX, GRIDX + GRIDWIDTH + 1, CELLSIZEX):
		pygame.draw.line(WIN, black, (x, GRIDY), (x, GRIDY + GRIDHEIGHT))
	for y in range(GRIDY, GRIDY + GRIDHEIGHT + 1, CELLSIZEY):
		pygame.draw.line(WIN, black, (GRIDX, y), (GRIDX + GRIDWIDTH, y))

def drawBackground():
	WIN.fill(white)
	pygame.draw.rect(WIN, black, (GRIDX, GRIDY, GRIDWIDTH, GRIDHEIGHT), 1)

	#Start node
	pygame.draw.rect(WIN, green, (40, 765, 25, 25))
	textSurface = FONT.render("Start Node", False, (0, 0, 0))
	WIN.blit(textSurface, (75, 765))

	#End Node
	pygame.draw.rect(WIN, orange, (175, 765, 25, 25))
	textSurface = FONT.render("End Node", False, (0, 0, 0))
	WIN.blit(textSurface, (210, 765))

	#Barrier Node
	pygame.draw.rect(WIN, black, (300, 765, 25, 25))
	textSurface = FONT.render("Barrier Node", False, (0, 0, 0))
	WIN.blit(textSurface, (335, 765))

	#Unvisited Node
	pygame.draw.rect(WIN, black, (445, 765, 25, 25), 1)
	textSurface = FONT.render("Unvisited Node", False, (0, 0, 0))
	WIN.blit(textSurface, (480, 765))

	#Visited Nodes
	pygame.draw.rect(WIN, red, (600, 765, 25, 25))
	pygame.draw.rect(WIN, yellow, (630, 765, 25, 25))
	textSurface = FONT.render("Visited Nodes", False, (0, 0, 0))
	WIN.blit(textSurface, (665, 765))

	#Shortest-path Node
	pygame.draw.rect(WIN, purple, (780, 765, 25, 25))
	textSurface = FONT.render("Shortest-path Node", False, (0, 0, 0))
	WIN.blit(textSurface, (815, 765))

def redrawGameWindow(nodes):
	drawBackground()
	for row in range(len(nodes)):
		for col in nodes[row]:
			col.draw()

	drawGrid(nodes)
	
	pygame.display.update()

def createNodes():
	nodes = []
	for row in range(GRIDSIZE):
			temp = []
			for col in range(GRIDSIZE):
				temp.append(Node((row, col), white))
			nodes.append(temp)
	return nodes

##########################
# A* Algorithm
##########################

def heuristic(a, b):
	(x1, y1) = a
	(x2, y2) = b
	return abs(x1 - x2) + abs(y1 - y2)

def astar(start, end, barriers, nodes):
	neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
	close_set = set()
	came_from = {}
	gscore = {start:0}
	fscore = {start:heuristic(start, end)}
	oheap = []
	heapq.heappush(oheap, (fscore[start], start))
	while oheap:
	    current = heapq.heappop(oheap)[1]
	    if current == end:
	        data = []
	        while current in came_from:
	            data.append(current)
	            current = came_from[current]
	        return data

	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            sys.exit()

	    close_set.add(current)
	    for i, j in neighbors:
	        if current[0] + i >= 0 and current[1] + j >= 0 and current[0] + i < GRIDSIZE and current[1] + j < GRIDSIZE:
	            neighbor = current[0] + i, current[1] + j
	        else:
	        	continue
	        if (neighbor[0], neighbor[1]) != start and (neighbor[0], neighbor[1]) != end and not(nodes[neighbor[0]][neighbor[1]] in barriers):
	        	nodes[neighbor[0]][neighbor[1]].makeOpen()
	        	redrawGameWindow(nodes)
	        tentative_g_score = gscore[current] + heuristic(current, neighbor)
	        if neighbor[0] < 0 or neighbor[0] >= GRIDSIZE or neighbor[1] < 0 or neighbor[1] >= GRIDSIZE or nodes[neighbor[0]][neighbor[1]] in barriers:
	        	continue
	        if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
	            continue
	        if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
	            came_from[neighbor] = current
	            if (current[0], current[1]) != start and (current[0], current[1] != end) and not(nodes[current[0]][current[1]] in barriers):
	            	nodes[current[0]][current[1]].makeClosed()
	            	redrawGameWindow(nodes)
	            gscore[neighbor] = tentative_g_score
	            fscore[neighbor] = tentative_g_score + heuristic(neighbor, end)
	            heapq.heappush(oheap, (fscore[neighbor], neighbor))
	return False

##########################
# Node Class
##########################

class Node(object):
	def __init__(self, pos, color):
		self.pos = pos #tuple (y, x)
		self.color = color

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

	def draw(self):
		x = (self.pos[1] * CELLSIZEX) + GRIDX
		y = (self.pos[0] * CELLSIZEY) + GRIDY
		width, height = CELLSIZEX, CELLSIZEY
		pygame.draw.rect(WIN, self.color, (x, y, width, height))

	def __eq__(self, other):
		return self.pos == other.pos

	def __repr__(self):
		return f"{self.pos} - g: {self.g} h: {self.h} f: {self.f}"

	def __lt__(self, other):
		return self.f < other.f

	def __gt__(self, other):
		return self.f > other.f

##########################
# Main Function
##########################

def main():
	global FONT, CLOCK, WIN, SCREENWIDTH, SCREENHEIGHT, GRIDSIZE, CELLSIZEX, CELLSIZEY, GRIDX, GRIDY, GRIDWIDTH, GRIDHEIGHT
	pygame.init()
	pygame.font.init()
	FONT = pygame.font.SysFont("Comic Sans MS", 15, 1)
	CLOCK = pygame.time.Clock()
	SCREENWIDTH, SCREENHEIGHT = 1000, 800
	WIN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
	GRIDX = 0
	GRIDY = 50
	GRIDWIDTH = 900
	GRIDHEIGHT = 700
	GRIDSIZE = 20
	CELLSIZEX = GRIDWIDTH // GRIDSIZE
	CELLSIZEY = GRIDHEIGHT // GRIDSIZE
	pygame.display.set_caption("Pathfining Algorithm Visualizer")
	nodes = createNodes()
	start = False
	end = False
	startNode = None
	endNode = None
	barrierNodes = []
	while True:
		CLOCK.tick(100)

		for event in pygame.event.get(): #checking for events
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if pygame.mouse.get_pressed()[0]:
				try:
					pos = pygame.mouse.get_pos()
					col = (pos[0] - GRIDX) // CELLSIZEX
					row = (pos[1] - GRIDY) // CELLSIZEY
					if not(start) and (row, col) != endNode:
						nodes[row][col].makeStart()
						startNode = (row, col)
						start = True
					elif not(end) and (row, col) != startNode:
						nodes[row][col].makeEnd()
						endNode = (row, col)
						end = True
					elif (row, col) != startNode and (row, col) != endNode:
						nodes[row][col].makeBarrier()
						barrierNodes.append(nodes[row][col])
				except AttributeError:
					pass
			if pygame.mouse.get_pressed()[2]:
				try:
					pass
				except AttributeError:
					pass

		keys = pygame.key.get_pressed() #to check key pressed (or held down)
		if keys[pygame.K_BACKSPACE]:
			nodes = createNodes()
			start = False
			end = False
			startNode = None
			endNode = None
			barrierNodes = []
		if keys[pygame.K_SPACE]:
			path = astar(startNode, endNode, barrierNodes, nodes)
			if path != False:
				for node in range(1, len(path)):
					nodes[path[node][0]][path[node][1]].makePath()
			else:
				print("No path found")

		redrawGameWindow(nodes)

main()