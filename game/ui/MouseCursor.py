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

class MouseCursor(object):

    def __init__(self, screen):
        self.screen = screen
        self.mouseImage = pygame.image.load("../resources/ui/mouse.png").convert_alpha()
        self.mouseImage = pygame.transform.scale(self.mouseImage, (100, 100))
        self.mouseImageBackup = self.mouseImage
        pygame.mouse.set_visible(0)

        self.enlarged = False

    def drawIcon(self):
        x,y = pygame.mouse.get_pos()
        if self.enlarged:
            self.screen.blit(self.mouseImage, (x - 25, y - 25))
        else:
            self.screen.blit(self.mouseImage, (x, y))

    def onLeftClickPressed(self):
        enlargedMouse = pygame.image.load("../resources/ui/mouse.png").convert_alpha()
        self.mouseImage = pygame.transform.scale(enlargedMouse, (150, 150))
        self.enlarged = True

    def onLeftClickReleased(self):
        self.mouseImage = self.mouseImageBackup
        self.enlarged = False

    def getMiddlePos(self):
        x,y = pygame.mouse.get_pos()
        return (x + 50, y + 50)