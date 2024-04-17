import pygame
import random


S = (400, 400)
win = pygame.display.set_mode((S[0], S[1]))
clock = pygame.time.Clock()
FPS = 100


head = pygame.Rect(0, 0, 60, 60)
eye_1 = pygame.Rect(head.width // 4 - 10, head.height // 4 - 10, 20, 20)
eye_2 = pygame.Rect(round(head.width * 0.75) - 10, head.height // 4 - 10, 20, 20)
m = [head.width // 2, head.height // 3 * 2]
r = 10

a = (S[0] - head.right) // 2
head.x += a
eye_1.x += a
eye_2.x += a
m[0] += a

a = (S[1] - head.bottom) // 2
head.y += a
eye_1.y += a
eye_2.y += a
m[1] += a

d = 1
c = 0
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
c_1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
c_2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
T = pygame.time.get_ticks()
O = 0
while True:
    if T + O < pygame.time.get_ticks():
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        O = random.randint(100, 500)
        T = pygame.time.get_ticks()
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
    m[0] += d

    pygame.draw.rect(win, (255, 0, 0), head)
    pygame.draw.rect(win, c_1, eye_1)
    pygame.draw.rect(win, c_2, eye_2)
    pygame.draw.circle(win, (255, 255, 255), (m[0], m[1]), r)
    pygame.draw.rect(win, (255, 0, 0), (m[0] - r, m[1] - r, 2 * r, r))


    pygame.display.update()
    clock.tick(FPS)

    if c == FPS:
        c = 0
