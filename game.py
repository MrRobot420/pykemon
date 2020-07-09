import pygame
from menu.infoBox import InfoBox as info
from objects.player import Player
from landscape.background import Background
from keys.keyHandler import checkKeyPresses

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
        self.pokemon = ''

        self.run = True
    

    def mainLoop(self):
        clock = pygame.time.Clock()
    
        while self.run:
            pygame.time.delay(40)  # Clock

            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # Check if X-Button has been clicked
                    self.run = False

            checkKeyPresses(self)

            self.win.fill((101, 67, 20))

            self.handlePokeballs()  # POKEBALLS
            self.background.draw()  # BACKGROUND
            self.player.draw()      # PLAYER
            self.handlePokemon()    # POKEMON
            
            pygame.display.update()


    def redrawGameWindow(self):
        self.win.fill((0, 0, 0))                


    def handlePokeballs(self):
        for pokeball in self.pokeballs:
            ball_outside_window = pokeball.checkBoundaries(self.window_width, self.window_height)
            if ball_outside_window:
                self.pokeballs.pop(0)
                print('BALLS on screen: %i' % len(self.pokeballs))
            else:
                pokeball.draw()
                pokeball.move(10)


    def handlePokemon(self):
        if (self.pokemon != ''):
            self.pokemon.draw()

    
    def moveBackground(self):
        self.background.move(15, self.player.direction)

    
game = Game(900, 900)
game.mainLoop()