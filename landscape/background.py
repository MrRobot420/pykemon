import pygame
import random
from helper.helper import loadImage
from .grass import Grass
from .tree import Tree

class Background(pygame.sprite.Sprite):

    def __init__(self, width, height, screen):
        pygame.sprite.Sprite.__init__(self)

        self.grass_image = loadImage('resources/images/Grass.png')
        self.tree_image = loadImage('resources/images/Tree.png')
        self.image_rect = self.grass_image.get_rect()
        self.screen = screen
        self.width = width
        self.height = height
        self.grass_blocks = []
        self.trees = []

        for i in range(150):
            self.placeNewGrassBlock()

        for i in range(15):
            self.placeNewTree()


    def placeNewGrassBlock(self):
        rand_x = random.randint(0, self.width)
        rand_y = random.randint(0, self.height)
        found_occupied = False
        
        if len(self.grass_blocks) < 1:
            self.grass_blocks.append(Grass(rand_x, rand_y, self.screen))
        else:
            found_occupied = self.checkIfPlaceIsOccupied(rand_x, rand_y)
            if not found_occupied:
                self.grass_blocks.append(Grass(rand_x, rand_y, self.screen))
            else:
                self.placeNewGrassBlock()
    

    def placeNewTree(self):
        rand_x = random.randint(0, self.width)
        rand_y = random.randint(0, self.height)
        found_occupied = False
        
        if len(self.trees) < 1:
            self.trees.append(Tree(rand_x, rand_y, self.screen))
        else:
            found_occupied = self.checkIfPlaceIsOccupied(rand_x, rand_y)
            if not found_occupied:
                self.trees.append(Tree(rand_x, rand_y, self.screen))
            else:
                self.placeNewTree()


    def draw(self):
        for grass in self.grass_blocks:
            self.screen.blit(self.grass_image, (grass.x, grass.y))
        
        for tree in self.trees:
            self.screen.blit(self.tree_image, (tree.x, tree.y))


    def checkBoundaries(self, player):
        return self.y < 0 or self.y > height or self.x < 0 or self.x > height

    
    def move(self, speed, direction):
        for index in range(len(self.grass_blocks)):
            grass = self.grass_blocks[index]
            grass.move(speed, direction)
            grass_outside_screen = grass.checkBoundaries(self.width, self.height)
            if grass_outside_screen:
                self.grass_blocks.pop(index)
                self.grass_blocks.append(grass.replaceGrassBlock(direction, self))

        for index in range(len(self.trees)):
            tree = self.trees[index]
            tree.move(speed, direction)
            tree_outside_screen = tree.checkBoundaries(self.width, self.height)
            if tree_outside_screen:
                self.trees.pop(index)
                self.trees.append(tree.replaceTree(direction, self))


    def checkIfPlaceIsOccupied(self, rand_x, rand_y):
        for current_grass in self.grass_blocks:
            if current_grass.x == rand_x and current_grass.y == rand_y:
                print('Same rand pos! Creating NEW one...')
                return True

        for current_tree in self.trees:
            if current_tree.x == rand_x and current_tree.y == rand_y:
                print('Same rand pos! Creating NEW one...')
                return True