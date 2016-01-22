import sys
import pygame
from pygame.locals import *
from objects.Car import Car
from objects.BackGround import BackGround
from objects.animals.Cheetah import Cheetah

#properties
size = width, height = 1280, 720
bgColor = 255, 255, 0
speed = 10

pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
screen.fill(bgColor)

animals = []

animals.append(Cheetah(screen))
back = BackGround("../resources/backgrounds/desert.png", screen, animals)

mainCar = Car("../resources/sprites/safaricar.png", screen)

pygame.display.flip()


while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_F4]:
        pygame.display.toggle_fullscreen()

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        back.move(speed)
        mainCar.draw()

    pygame.display.flip()