import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = pygame.image.load('./resources/images/Player.png')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = 0
        
        self.money = 500
    
    def draw(self):
        self.screen.blit(self.image, (self.x - self.rect.width / 2, self.y - self.rect.height / 2))
        # pygame.draw.rect(self.screen, (255, 0, 0), self.image)


    def move(self, x, y):
        self.x = x
        self.y = y
    
    def rotate(self, angle):
        if (self.angle != angle):
            self.angle = angle
            self.image = pygame.transform.rotate(self.original_image, angle)