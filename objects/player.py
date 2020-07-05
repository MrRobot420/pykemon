import pygame
from helper.helper import loadImage

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = loadImage('resources/images/Player.png')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = x - self.rect.width / 2
        self.y = y - self.rect.height / 2
        self.angle = 0
        self.direction = 'UP'
        
        self.money = 500
    
    
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


    def move(self, x, y):
        self.x = x
        self.y = y
    

    def rotate(self, angle):
        if (self.angle != angle):
            self.angle = angle
            self.changeDirection()
            self.image = pygame.transform.rotate(self.original_image, angle)


    def changeDirection(self):
        if self.angle == 0:
            self.direction = 'UP'
        elif self.angle == 90:
            self.direction = 'LEFT'
        elif self.angle == 180:
            self.direction = 'DOWN'
        elif self.angle == 270:
            self.direction = 'RIGHT'