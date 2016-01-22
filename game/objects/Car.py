import pygame
from objects.GenericObject import GenericObject

"""
Class that models a car object.
@:author Hermann Krumrey<hermann@krumreh.com>
"""
class Car(GenericObject):

    """
    Creates a new car object and places it on the screen
    @:param resource - the resource image to be used
    @:param screen - the screen on which to display the car
    @:param xPos - the x Position of the car on the screen
    @:param yPos - the y Position of the car on the screen
    @:param xSize - the width of the car
    @:param ySize - the height of the car
    """
    def __init__(self, resource, screen, xPos=-1, yPos=-1, xSize=-1, ySize=-1):
        self.screen = screen
        self.car = pygame.image.load(resource).convert_alpha()
        x, y = screen.get_size()
        if xSize + ySize < -1:
            xSize = int(x/4)
        self.car = GenericObject.scaleImageKeepAspect(self.car, xSize)
        self.carRect = self.car.get_rect()
        ySize = self.carRect.size[1]
        if xPos + yPos < -1:
            xPos = 10
            yPos = y - 10 - ySize
        self.carRect.move_ip(xPos, yPos)
        screen.blit(self.car, self.carRect)

    """
    Re-draws the car on the screen
    """
    def draw(self):
        self.screen.blit(self.car, self.carRect)