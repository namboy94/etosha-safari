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
    def __init__(self, resource, screen, animals):
        self.screen = screen
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

        self.animals = animals
        self.activeAnimal = None
        self.stepCounter = 0
        self.animalPos = x
        self.animals = animals
        self.photographed = False

    """
    Re-draws the car on the screen
    """
    def draw(self):
        self.screen.blit(self.bg1, self.bg1Rect)
        self.screen.blit(self.bg2, self.bg2Rect)

    def drawAnimals(self):
        if not self.activeAnimal is None:
            self.activeAnimal.draw()

    def checkPoints(self, mouseCursor):
        if self.activeAnimal is None or self.photographed: return 0
        else:
            x, y = mouseCursor.getMiddlePos()
            left = self.activeAnimal.animalRect.left
            top = self.activeAnimal.animalRect.top
            right = self.activeAnimal.animalRect.right
            bottom = self.activeAnimal.animalRect.bottom

            if x <= right and x >= left and y >= top and y <= bottom:
                self.photographed = True
                return self.activeAnimal.getPoints()
            else:
                return 0




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

        if not self.activeAnimal is None:
            self.activeAnimal.move(-speed, 0)
            self.animalPos -= speed
            if self.animalPos < -self.activeAnimal.animalRect.size[0]:
                self.animalPos = x
                self.activeAnimal.animalRect.move_ip(x, 0)
                self.activeAnimal = None
                self.photographed = False
        else:
            self.stepCounter += speed
            if self.stepCounter > 1000:
                for animal in self.animals:
                    if animal.search():
                        self.activeAnimal = animal(self.screen)
                        break
                self.stepCounter = 0

        self.draw()
