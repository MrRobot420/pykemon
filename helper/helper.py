import os
import pygame


def loadImage(path):
    return pygame.image.load(joinPath(path))


def joinPath(path):
    return os.path.join(os.getcwd(), path)