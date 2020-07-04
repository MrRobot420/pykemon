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

        for i in range(100):
            self.placeNewGrassBlock()


    def placeNewGrassBlock(self):
        rand_x = random.randint(0, self.width)
        rand_y = random.randint(0, self.height)
        found_occupied = False
        
        if len(self.grass_blocks) < 1:
            self.grass_blocks.append(Grass(rand_x, rand_y, self.screen))
        else:
            found_occupied = self.checkIfPlaceIsOccupied(rand_x, rand_y)
            if not found_occupied:
                self.grass_blocks.append(Grass(rand_x, rand_y, self.screen))
            else:
                self.placeNewGrassBlock()


    def draw(self):
        for grass in self.grass_blocks:
            self.screen.blit(self.original_image, (grass.x, grass.y))


    def checkBoundaries(self, player):
        return self.y < 0 or self.y > height or self.x < 0 or self.x > height

    
    def move(self, speed, direction):
        for index in range(len(self.grass_blocks)):
            grass = self.grass_blocks[index]
            grass.move(speed, direction)
            grass_outside_screen = grass.checkBoundaries(self.width, self.height)
            if grass_outside_screen:
                self.grass_blocks.pop(index)
                self.grass_blocks.append(grass.replaceGrassBlock(direction, self))


    def checkIfPlaceIsOccupied(self, rand_x, rand_y):
        for current_grass in self.grass_blocks:
            if current_grass.x == rand_x and current_grass.y == rand_y:
                print('Same rand pos! Creating NEW one...')
                return True