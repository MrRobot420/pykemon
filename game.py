import pygame
from infoBox import InfoBox as info
from player import Player

class Game:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Pykémon')
        self.window_width = width
        self.window_height = height
        self.win = pygame.display.set_mode((self.window_width, self.window_height))
        
        self.player = Player(self.window_width / 2, self.window_height / 2, self.win)
        self.run = True
    
    def mainLoop(self):
        while self.run:
            pygame.time.delay(100)  # Clock

            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # Check if X-Button has been clicked
                    self.run = False

            self.checkKeyPresses()

            self.win.fill((20, 20, 20))
            self.player.draw()

            pygame.display.update()


    def redrawGameWindow(self):
        self.win.fill(BLACK)

    def checkKeyPresses(self):
        keys = pygame.key.get_pressed()
        vel = 15

        # Check for specific key presses
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:             
            self.player.x -= vel
            self.player.rotate(90)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.x += vel
            self.player.rotate(270)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.y -= vel
            self.player.rotate(0)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.y += vel
            self.player.rotate(180)

    
game = Game(900, 900)
game.mainLoop()