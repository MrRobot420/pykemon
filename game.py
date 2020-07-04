import pygame
from infoBox import InfoBox as info
from player import Player
from pokeball import Pokeball
from background import Background

class Game:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Pykémon')
        self.window_width = width
        self.window_height = height
        self.win = pygame.display.set_mode((self.window_width, self.window_height))
        
        self.player = Player(self.window_width / 2, self.window_height / 2, self.win)
        self.pokeballs = []
        self.background = Background(self.window_width, self.window_height, self.win)

        self.run = True
    

    def mainLoop(self):
        while self.run:
            pygame.time.delay(50)  # Clock

            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # Check if X-Button has been clicked
                    self.run = False

            self.checkKeyPresses()

            self.win.fill((20, 200, 120))

            self.background.draw()  # BACKGROUND
            self.player.draw()      # PLAYER
            self.handlePokeballs()  # POKEBALLS
            
            pygame.display.update()


    def redrawGameWindow(self):
        self.win.fill((0, 0, 0))


    def checkKeyPresses(self):
        keys = pygame.key.get_pressed()
        vel = 15

        # Check for specific key presses
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.moveBackground()
            self.player.rotate(90)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.moveBackground()
            self.player.rotate(270)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.moveBackground()
            self.player.rotate(0)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.moveBackground()
            self.player.rotate(180)
        if keys[pygame.K_SPACE]:
            print('BALL got shot')
            self.pokeballs.append(Pokeball(self.player, self.win))


    def handlePokeballs(self):
        for pokeball in self.pokeballs:
            ball_outside_window = pokeball.checkBoundaries(self.window_width, self.window_height)
            if ball_outside_window:
                self.pokeballs.pop(0)
                print('BALLS on screen: %i' % len(self.pokeballs))
            else:
                pokeball.draw()
                pokeball.move(10)

    
    def moveBackground(self):
        self.background.move(15, self.player.direction)

    
game = Game(900, 900)
game.mainLoop()