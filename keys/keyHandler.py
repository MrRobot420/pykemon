import pygame
from objects.pokeball import Pokeball
from objects.pokemon import Pokemon
from sound.soundHandler import loadSound, playSound


def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False


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
        loadSound('hop.ogg', 0)
        self.pokeballs.append(Pokeball(self.player, self.win))
    if keys[pygame.K_p]:
        if (self.pokemon == ''):
            print('POKEMON was spawned')
            self.pokemon = Pokemon('Pikachu', ['Blitzkugel'], 'ELECTRO', 100, 'funny', self.win, self.window_width, self.window_height)
        else: self.pokemon = ''