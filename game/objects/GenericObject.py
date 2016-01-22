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