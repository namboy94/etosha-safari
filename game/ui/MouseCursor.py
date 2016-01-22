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