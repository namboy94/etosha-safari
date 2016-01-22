import pygame
from objects.GenericObject import GenericObject

"""
Class that defines the background of a screen
@:author Hermann Krumrey<hermann@krumreh.com>
"""
class BackGround(GenericObject):

    """
    Creates a new background
    @:param resource - the resource image to be used
    @:param screen - the screen on which to display the background
    """
    def __init__(self, resource, screen, inanimates):
        self.screen = screen
        self.inanimates = inanimates
        self.bg1 = pygame.image.load(resource).convert()
        x, y = screen.get_size()

        self.bg1Pos = 0
        self.bg2Pos = x

        self.bg1 = pygame.transform.scale(self.bg1, (x, y))
        self.bg2 = pygame.transform.scale(self.bg1, (x, y))

        self.bg1Rect = self.bg1.get_rect()
        self.bg2Rect = self.bg2.get_rect()

        self.bg2Rect.move_ip(x, 0)

        screen.blit(self.bg1, self.bg1Rect)
        screen.blit(self.bg2, self.bg2Rect)

        for inanimate in inanimates:
            inanimate.draw()

    """
    Re-draws the car on the screen
    """
    def draw(self):
        self.screen.blit(self.bg1, self.bg1Rect)
        self.screen.blit(self.bg2, self.bg2Rect)
        for inanimate in self.inanimates:
            inanimate.draw()

    def move(self, speed=1):
        x, y = self.screen.get_size()

        self.bg1Rect = self.bg1Rect.move([-speed, 0])
        self.bg2Rect = self.bg2Rect.move([-speed, 0])

        self.bg1Pos -= speed
        self.bg2Pos -= speed

        if self.bg1Pos <= -x:
            self.bg1Pos = x
            self.bg1Rect = self.bg1Rect.move([2 * x, 0])

        if self.bg2Pos <= -x:
            self.bg2Pos = x
            self.bg2Rect = self.bg2Rect.move([2 * x, 0])

        for inanimate in self.inanimates:
            inanimate.move(-speed, 0)

        self.draw()
