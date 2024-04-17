from typing import Any
import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)

        self.image = pygame.image.load('Character.png') 
        self.image = pygame.transform.scale(self.image, (300, 650))
        self.rect = self.image.get_rect()
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
        