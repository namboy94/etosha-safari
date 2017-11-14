"""
Copyright 2016-2017 Hermann Krumrey <hermann@krumreyh.com>

This file is part of etosha-safari.

etosha-safari is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

etosha-safari is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with etosha-safari.  If not, see <http://www.gnu.org/licenses/>.
"""

import pygame
import random
from objects.GenericObject import GenericObject

"""
Class that models a Generic animal
@:author Hermann Krumrey<hermann@krumreyh.com>
"""
class GenericAnimal(GenericObject):

    def __init__(self, resource, screen, xPos, yPos, xSize, ySize):
        self.screen = screen
        self.animal = pygame.image.load(resource).convert_alpha()
        self.animal = pygame.transform.scale(self.animal, (xSize, ySize))
        self.animalRect = self.animal.get_rect()
        self.animalRect.move_ip(xPos, yPos)

    def draw(self):
        self.screen.blit(self.animal, self.animalRect)

    def move(self, x, y):
        self.animalRect = self.animalRect.move([x, y])

    """
    Makes the animal run away
    """
    def runAway(self):
        raise NotImplementedError()

    @staticmethod
    def searcher(encounterrate):
        searchResult = random.randint(0, int(1000 / encounterrate))
        if searchResult == 1: return True
        else: return False