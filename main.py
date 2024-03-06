import pygame
import random


SIZE = 500
FPS = 1
GAME = True
CLOCK = pygame.time.Clock()
WINDOW = pygame.display.set_mode((SIZE, SIZE))





while GAME:
    COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    WINDOW.fill(COLOR)


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                exit()


    pygame.display.update()
    CLOCK.tick(FPS)