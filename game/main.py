"""
Copyright 2016-2017 Hermann Krumrey

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
speed = 0
accelCount = -1

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

tacho0 = pygame.transform.scale(pygame.image.load("../resources/ui/tacho0.png").convert_alpha(), (250, 250))
tacho05 = pygame.transform.scale(pygame.image.load("../resources/ui/tacho05.png").convert_alpha(), (250, 250))
tacho1 = pygame.transform.scale(pygame.image.load("../resources/ui/tacho1.png").convert_alpha(), (250, 250))

currentTacho = tacho0

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
        if speed < 26: accelCount += 1
        if accelCount % 5 == 0: speed += 1; accelCount = -1
        back.move(speed)
        mainCar.draw()
    else:
        if speed > 0:
            speed -= 1

    if speed < 10: currentTacho = tacho0
    elif speed < 18: currentTacho = tacho05
    elif speed > 18: currentTacho = tacho1

    back.draw()

    text = font.render(str(score), 1, (10, 10, 10))
    textRect = text.get_rect()
    screen.blit(text, textRect)
    screen.blit(currentTacho, (1600, 50))

    mainCar.draw()
    back.drawAnimals()
    mouseCursor.drawIcon()

    pygame.display.flip()