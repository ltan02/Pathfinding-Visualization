import pygame
import math

class Slider(object):
    def __init__(self, startPos, width, text, min, max):
        self.startX = startPos[0]
        self.startY = startPos[1]
        self.endX = self.startX + width
        self.endY = self.startY
        self.text = text
        self.min = min
        self.max = max
        self.circle = Circle((self.startX + self.endX) / 2, self.startY, 10)
        self.value = 0

    def draw(self, win):
        font = pygame.font.SysFont("Arial", 18)
        textSurface = font.render(self.text, True, (0, 0, 0))
        win.blit(textSurface, (((self.startX + self.endX) / 2) - (textSurface.get_width() / 2), self.startY - 40))

        pygame.draw.line(win, (0, 0, 0), (self.startX, self.startY), (self.endX, self.endY), 3)

        textSurface = font.render(str(self.min), True, (0, 0, 0))
        win.blit(textSurface, (self.startX - 10, (self.startY - (textSurface.get_height() / 2))))

        textSurface = font.render(str(self.max), True, (0, 0, 0))
        win.blit(textSurface, (self.endX + 10, (self.startY - (textSurface.get_height() / 2))))

        self.circle.draw(win)

class Circle(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, win):
        pygame.draw.circle(win, (50, 50, 50), (self.x , self.y), self.radius)

    def isPressed(self, posX, posY):
        return math.sqrt(((posX - self.x) ** 2) + ((posY - self.y) ** 2)) <= self.radius

    def update(self, sliderStart, sliderEnd, posX):
        if sliderStart <= posX <= sliderEnd:
            self.x = posX

    def updateSpeed(self, sliderStart, sliderEnd):
        newSpeed = ((sliderEnd - sliderStart) // 60) * (self.x - sliderStart - 10)
        if newSpeed <= 0:
            newSpeed = 0

        if newSpeed >= 60:
            newSpeed = 60

        return newSpeed

