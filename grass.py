import pygame

class Grass(pygame.sprite.Sprite):

    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = pygame.image.load('./resources/images/Grass.png')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = x
        self.y = y
    

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


    def checkBoundaries(self, width, height):
        return self.y < 0 or self.y > height or self.x < 0 or self.x > height