import os
import pygame


def loadImage(path):
    return pygame.image.load(os.path.join(os.getcwd(), path))