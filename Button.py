import pygame

pygame.font.init()

class Button(object):
    def __init__(self, x, y, width, height, bgcolor, text, textSize, fontColor, font, win):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bgcolor = bgcolor
        self.text = text
        self.textSize = textSize
        self.fontColor = fontColor
        self.font = font
        self.win = win
        self.pressed = False

    def draw(self):
        pygame.draw.rect(self.win, self.bgcolor, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont(self.font, self.textSize)
        textSurface = font.render(self.text, True, self.fontColor)
        self.win.blit(textSurface, (((self.x + (self.x + self.width)) / 2) - (textSurface.get_width() / 2), \
                               ((self.y + (self.y + self.height)) / 2) - (textSurface.get_height() / 2)))

    def isPressed(self, posX, posY):
        return self.x <= posX <= self.x + self.width and self.y <= posY <= self.y + self.height

    def dropDownButtons(self):
        pass

