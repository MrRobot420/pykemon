import pygame
import random
from grass import Grass

class Background(pygame.sprite.Sprite):

    def __init__(self, width, height, screen):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = pygame.image.load('./resources/images/Grass.png')
        self.image_rect = self.original_image.get_rect()
        self.screen = screen
        self.width = width
        self.height = height
        self.grass_blocks = []

        for i in range(200):
            rand_x = random.randint(0, self.width)
            rand_y = random.randint(0, self.height)
            self.grass_blocks.append(Grass(rand_x, rand_y, self.screen))

    

    def draw(self):
        for grass in self.grass_blocks:
            self.screen.blit(self.original_image, (grass.x, grass.y))


    def checkBoundaries(self, width, height):
        return self.y < 0 or self.y > height or self.x < 0 or self.x > height