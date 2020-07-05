import pygame
import random
from helper.helper import loadImage

class Grass(pygame.sprite.Sprite):

    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = loadImage('resources/images/Grass.png')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = x
        self.y = y
    

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


    def move(self, speed, direction):
        if direction == 'UP':
            self.y += speed
        elif direction == 'LEFT':
            self.x += speed
        elif direction == 'RIGHT':
            self.x -= speed
        elif direction == 'DOWN':
            self.y -= speed


    def checkBoundaries(self, width, height):
        return self.y < 0 or self.y > height or self.x < 0 or self.x > height

    
    def replaceGrassBlock(self, direction, background):
        if direction == 'UP':
            rand_x = random.randint(0, background.width)
            rand_y = 0
            return Grass(rand_x, rand_y, self.screen)
        elif direction == 'LEFT':
            rand_x = 0
            rand_y = random.randint(0, background.height)
            return Grass(rand_x, rand_y, self.screen)
        elif direction == 'RIGHT':
            rand_x = background.width
            rand_y = random.randint(0, background.height)
            return Grass(rand_x, rand_y, self.screen)
        elif direction == 'DOWN':
            rand_x = random.randint(0, background.width)
            rand_y = background.height
            return Grass(rand_x, rand_y, self.screen)