import random
import pygame
from main import enemy_laser


class Meteorite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("meteorite.png")
        size = random.randint(70, 150)

        self.image = pygame.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (800, random.randint(0, 600 - size))

        self.step_x = random.randint(1, 3)
        self.step_y = random.randint(-1, 1)
    def update(self):
        self.rect.topleft = (
            self.rect.x - self.step_x,
            self.rect.y + self.step_y
        )
class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("mouse.png")
        size = random.randint(70, 150)

        self.image = pygame.transform.scale(self.image, (size, size))
        self.image = pygame.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, 600 - size), 0)

        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(1, 2)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if random.randint(1, 100) == 1:
            enemy_laser.add(E_Laser(self.rect.midbottom))
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("laser.png")

        self.image = pygame.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect(midbottom=pos)

        self.speed = 2
    def update(self):
        self.rect.y -= self.speed
class E_Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("e_laser.png")
        self.image = pygame.transform.scale(self.image, (20, 60))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect(midbottom = pos)

        self.speed = 4
    def update(self):
        self.rect.y += self.speed
class Starship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image = pygame.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midleft = (0, 300)
        self.x = self.rect.x
        self.mode  = 'vertical'
    def update(self):
        keys = pygame.key.get_pressed()
        if self.mode == "horizontal":
            if keys[pygame.K_LEFT] and self.rect.left - 3 >= 0:
                self.rect.x -= 3
            if keys[pygame.K_RIGHT] and self.rect.right + 3 <= 800:
                self.rect.x += 3
        if self.mode == "vertical":
            if keys[pygame.K_UP] and self.rect.top - 3 >= 0:
                self.rect.y -= 3
            if keys[pygame.K_DOWN] and self.rect.bottom + 3 <= 600:
                self.rect.y += 3
    def switch_mode(self):
        self.image = pygame.image.load("ship_r.png")
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (400, 580)

        self.mode = "horizontal"
class Cats(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(self.image, (400, 400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30, 600)

        self.mode = "up"
    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = "stay"
class Captain(Cats):
    def __init__(self):
        self.image = pygame.image.load("captain.png")
        Cats.__init__(self)
class Alien(Cats):
    def __init__(self):
        self.image = pygame.image.load("alien.png")
        Cats.__init__(self)
