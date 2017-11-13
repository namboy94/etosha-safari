"""
Copyright 2016-2017 Hermann Krumrey

This file is part of etosha-safari.

kudubot is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

kudubot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with kudubot.  If not, see <http://www.gnu.org/licenses/>.
"""

from objects.animals.GenericAnimal import GenericAnimal

class Cheetah(GenericAnimal):
    
    def __init__(self, screen, xPos=-1, yPos=-1, xSize=-1, ySize=-1):
        if xSize + ySize < -1:
            xSize = 300
            ySize = 137
        if xPos + yPos < -1:
            xPos, yPos = screen.get_size()
            yPos = yPos - ySize - 10

        super(Cheetah, self).__init__("../resources/sprites/animals/cheetah.png", screen, xPos, yPos, xSize, ySize)

    @staticmethod
    def search():
        return GenericAnimal.searcher(5)

    """
    Method that defines the points this animal gives when photographed.
    """
    def getPoints(self):
        return 10000