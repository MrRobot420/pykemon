import os
import pygame
from helper.helper import joinPath

def loadSound(name, state):
    name = 'resources/sounds/' + name
    pygame.mixer.init()
    pygame.mixer.music.load(joinPath(name))
    playSound(state)

def playSound(state):
    pygame.mixer.music.play(state)