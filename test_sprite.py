import pygame
from class_char import *


S = [1500, 1500]
G = True
FPS = 60
clock = pygame.time.Clock()
win = pygame.display.set_mode((S[0], S[1]))

background_im = pygame.image.load('background.jpeg')
background_im = pygame.transform.scale(background_im, (S[0], S[1]))

actor = Character()

while G:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    actor.update()
    
    win.blit(background_im, (0, 0))
    win.blit(actor.image, actor.rect)

    pygame.display.update()
    clock.tick(FPS)
