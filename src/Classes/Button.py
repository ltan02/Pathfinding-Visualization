import pygame

pygame.font.init()

class Button(object):
    def __init__(self, buttonName, x, y, width, height, text, textSize, win, show=True):
        self.name = buttonName
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bgcolor = (200, 200, 200)
        self.text = text
        self.textSize = textSize
        self.fontColor = (0, 0, 0)
        self.font = "Arial"
        self.win = win
        self.pressed = False
        self.show = show

    def draw(self):
        if self.show:
            if self.pressed:
                self.bgcolor = (50, 50, 50)
            else:
                self.bgcolor = (200, 200, 200)

            pygame.draw.rect(self.win, self.bgcolor, (self.x, self.y, self.width, self.height))
            font = pygame.font.SysFont(self.font, self.textSize)
            textSurface = font.render(self.text, True, self.fontColor)
            self.win.blit(textSurface, (((self.x + (self.x + self.width)) / 2) - (textSurface.get_width() / 2), \
                                        ((self.y + (self.y + self.height)) / 2) - (textSurface.get_height() / 2)))

    def isPressed(self, posX, posY):
        return self.x <= posX <= self.x + self.width and self.y <= posY <= self.y + self.height

    def dropDownButtons(self):
        pass