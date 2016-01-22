import sys
import pygame
import vlc
from pygame.locals import *
from ui.MouseCursor import MouseCursor
from objects.Car import Car
from objects.BackGround import BackGround
from objects.animals.Cheetah import Cheetah
from objects.animals.Elephant import Elephant
from objects.animals.Giraffe import Giraffe
from objects.animals.Lion import Lion

#properties
size = width, height = 1920, 1080
bgColor = 255, 255, 0
speed = 10

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
screen.fill(bgColor)

mouseCursor = MouseCursor(screen)

animals = []
animals.append(Cheetah)
animals.append(Lion)
animals.append(Giraffe)
animals.append(Elephant)

score = 0

font = pygame.font.Font(None, 36)


back = BackGround("../resources/backgrounds/desert.png", screen, animals)
mainCar = Car("../resources/sprites/safaricar.png", screen)

pygame.display.flip()
pygame.display.set_caption('Etosha Safari')

p = vlc.MediaPlayer('../resources/sounds/bgmusic.mp3')
p.play()


while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            mouseCursor.onLeftClickPressed()
            score += back.checkPoints(mouseCursor)

        if event.type == MOUSEBUTTONUP:
            mouseCursor.onLeftClickReleased()

    if pygame.key.get_pressed()[pygame.K_F4]:
        pygame.display.toggle_fullscreen()

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        back.move(speed)
        mainCar.draw()

    back.draw()

    text = font.render(str(score), 1, (10, 10, 10))
    textRect = text.get_rect()
    screen.blit(text, textRect)

    mainCar.draw()
    back.drawAnimals()
    mouseCursor.drawIcon()

    pygame.display.flip()