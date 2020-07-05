import pygame
import os

class Pokeball(pygame.sprite.Sprite):

    def __init__(self, player, screen):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = pygame.image.load(os.path.join(os.getcwd(), 'resources/images/Pokeball.png'))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = player.x + player.rect.width - self.rect.width
        self.y = player.y
        self.angle = 0
        self.direction = player.direction
    

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


    def move(self, speed):
        if self.direction == 'UP':
            self.y -= speed
        elif self.direction == 'RIGHT':
            self.x += speed
        elif self.direction == 'LEFT':
            self.x -= speed
        elif self.direction == 'DOWN':
            self.y += speed
    

    def rotate(self, angle):
        if (self.angle != angle):
            self.angle = angle
            self.image = pygame.transform.rotate(self.original_image, angle)


    def checkBoundaries(self, width, height):
        return self.y < 0 or self.y > height or self.x < 0 or self.x > height