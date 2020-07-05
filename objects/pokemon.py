import pygame
from helper.helper import loadImage

class Pokemon:

    def __init__(self, name, attacks, element, health, effect, screen, width, height, isEnemy = False):
        self.screen = screen
        self.screen_width = width
        self.screen_height = height
        self.original_image = loadImage('resources/images/%s.png' % name)
        self.image = pygame.transform.scale(self.original_image, (90, 90))
        self.rect = self.image.get_rect()
        self.element = element
        self.attacks = attacks
        self.effect = effect
        self.health = health
        self.alive = True
        self.level = 1
        self.isEnemy = isEnemy


    def draw(self):
        if (self.isEnemy):
            self.screen.blit(self.image, (self.screen_width - self.rect.width, 0))
        else:
            self.screen.blit(self.image, (0, self.screen_height - self.rect.height))