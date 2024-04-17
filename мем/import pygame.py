import pygame

pygame.mixer.init()


S = [1500, 1500]
G = True
win = pygame.display.set_mode((S[0], S[1]))
clock = pygame.time.Clock()
FPS = 60

background_im = pygame.image.load('мем/background.jpeg')
background_im = pygame.transform.scale(background_im, (S[0], S[1]))


actor = pygame.image.load('мем/Character.png')
actor = pygame.transform.scale(actor, (300, 650))
a_rect = actor.get_rect()
a_rect.x = 150
a_rect.y = 200
actor1 = pygame.image.load('мем/Character1.png')
actor1 = pygame.transform.scale(actor1, (300, 650))
a_rect1 = actor.get_rect()
a_rect1.x = 150
a_rect1.y = 200


# sound = pygame.mixer.music.load('мем/fonk.mp3')
# voice = pygame.mixer.Sound('мем/voice.wav')
# voice.play()

# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(-1)


while G:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            pass
    
    k_ = pygame.key.get_pressed()
    if k_[pygame.K_LEFT]:
        a_rect.x -= 10
    if k_[pygame.K_RIGHT]:
        a_rect.x += 10
    if k_[pygame.K_UP]:
        a_rect.y -= 10
    if k_[pygame.K_DOWN]:
        a_rect.y += 10

    if k_[pygame.K_a]:
        a_rect1.x -= 10
    if k_[pygame.K_d]:
        a_rect1.x += 10
    if k_[pygame.K_w]:
        a_rect1.y -= 10
    if k_[pygame.K_s]:
        a_rect1.y += 10
    
    m_ = pygame.mouse.get_pressed()
    m_p = pygame.mouse.get_pos()

    if m_[0]:
        a_rect.center = (m_p[0], m_p[1])

    win.blit(background_im, (0, 0))
    win.blit(actor, (a_rect.x, a_rect.y))
    win.blit(actor1, (a_rect1.x, a_rect1.y))

    pygame.display.update()
    clock.tick(FPS)
