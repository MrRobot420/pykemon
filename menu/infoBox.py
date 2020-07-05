import pygame

class InfoBox:

    def __init__(self, width, height, pos):
        self.width = width
        self.height = height
        self.x = pos['x']
        self.y = pos['y']


    def drawInfoBox(self, surface, color):
        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))