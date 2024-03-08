import pygame
import random


S = (400, 400)
win = pygame.display.set_mode((S[0], S[1]))
clock = pygame.time.Clock()
FPS = 1000


head = pygame.Rect(0, 0, 60, 60)
eye_1 = pygame.Rect(head.width // 4 - 10, head.height // 4 - 10, 20, 20)
eye_2 = pygame.Rect(round(head.width * 0.75) - 10, head.height // 4 - 10, 20, 20)

a = (S[0] - head.right) // 2
head.x += a
eye_1.x += a
eye_2.x += a

a = (S[1] - head.bottom) // 2
head.y += a
eye_1.y += a
eye_2.y += a


d = 1
c = 0
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
c_1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
c_2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
while True:
    if c % (FPS // 2) == 0:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    c += 1
    if c % (FPS // 5) == 0:
        c_1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if c % (FPS // 7) == 0:
        c_2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    win.fill(color)

    if head.x <= 0 or head.right >= S[1]:
        d *= -1

    head.x += d
    eye_1.x += d
    eye_2.x += d

    pygame.draw.rect(win, (255, 0, 0), head)
    pygame.draw.rect(win, c_1, eye_1)
    pygame.draw.rect(win, c_2, eye_2)

    pygame.display.update()
    clock.tick(FPS)

    if c == FPS:
        c = 0
