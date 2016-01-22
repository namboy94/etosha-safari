import pygame
import random
from objects.GenericObject import GenericObject

"""
Class that models a Generic animal
@:author Hermann Krumrey<hermann@krumreyh.com>
"""
class GenericAnimal(GenericObject):

    def __init__(self, resource, screen, encounterrate, xPos, yPos, xSize, ySize):
        self.screen = screen
        self.animal = pygame.image.load(resource).convert_alpha()
        self.animal = pygame.transform.scale(self.animal, (xSize, ySize))
        self.animalRect = self.animal.get_rect()
        self.animalRect.move_ip(xPos, yPos)
        self.encounterrate = encounterrate

    def draw(self):
        self.screen.blit(self.animal, self.animalRect)

    def move(self, x, y):
        self.animalRect = self.animalRect.move([x, y])

    def search(self):
        searchResult = random.randint(0, int(1000 / self.encounterrate))

    """
    Makes the animal run away
    """
    def runAway(self):
        raise NotImplementedError()