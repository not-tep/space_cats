import pygame
import random
import pygame.gfxdraw


win = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
FPS = 60
win.fill((152, 238, 245))


def draw_cloud(x, y, n) -> None:
    for i in range(n):
        pygame.gfxdraw.filled_circle(win, x, y, random.randint(10, 50), (255, 255, 255, random.randint(50, 100)))
        x += random.randint(-5, 15)
        y += random.randint(-5, 5)
def draw_trunk(x, y) -> int:
    c = random.randint(10, 30)
    width = random.randint(7, 10)
    height = random.randint(150, 200)
    pygame.draw.rect(win, (255 - c, 255 - c, 255 - c), (x, y - height, width, height))
    y1 = y
    while y1 - 15 > y - height:
        y1 -= random.randint(10, 12)
        c = random.randint(20, 100)
        w = random.randint(2, 5)
        pygame.draw.rect(win, (c, c, c), (x, y1, width, w))
    return y - height
def draw_bereza(x, y) -> None:
    end_y = draw_trunk(x, y)
    draw_crow(x, y, end_y)
def draw_crow(x, y, end_y) -> None:
    y -= 75
    while True:
        pygame.gfxdraw.filled_circle(win, x, y, random.randint(40, 50), (13, 255, 0, random.randint(75, 150)))
        y -= random.randint(5, 20)
        x += random.randint(-5, 5)
        if y - 10 <= end_y:
            return


density = random.randint(4, 12)
for n in range(13):
    for i in range(11):
        draw_cloud(70 * i + random.randint(-30, 30), 35 * n + random.randint(-50, 50), density)

pygame.draw.rect(win, (64, 255, 64), (0, 450, 750, 750))

for i in range(7):
    draw_bereza(100 * (i + 1) - 25, 500)

pygame.display.update()
while True:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    
