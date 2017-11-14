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

"""
Class that models a generic Object
@:author Hermann Krumrey<Hermann@krumreyh.com>
"""
class GenericObject(object):

    """
    Redraws the object
    """
    def draw(self):
        raise NotImplementedError()

    """
    @:raises Exception
    """
    @staticmethod
    def scaleImageKeepAspect(image, x=-1, y=-1):
        if x == -1 and y == -1: return image
        if not x == -1 and not y == -1: raise Exception("Invalid parameter input")

        oriX, oriY = image.get_rect().size

        newImage = image

        if x == -1:
            newY = y
            ratio = oriY / newY
            newX = int(oriX / ratio)
            newImage = pygame.transform.scale(image, (newX, newY))

        if y == -1:
            newX = x
            ratio = oriX / newX
            newY = int(oriY / ratio)
            newImage = pygame.transform.scale(image, (newX, newY))

        return newImage