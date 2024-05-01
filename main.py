# Import
import pygame
enemy_laser = pygame.sprite.Group()

if __name__ == '__main__':
    import time
    from sprite import *


    # Init modules
    pygame.init()
    pygame.mixer.init()


    # Init constants 
    S = (800, 600)                                      # Size
    W = pygame.display.set_mode(S)                      # Window
    pygame.display.set_caption("Космические коты")      # Renaming window 
    FPS = 120                                           # FPS
    F = pygame.font.Font('font.otf', 25)                # Font
    C = pygame.time.Clock()                             # Clock
    G = True                                            # Is_game (bool)
    M = "start_scene"                                   # Mode
    TN = 0                                              # Text number
    T = time.time()

    # Init variables
    start_text = ["Мы засекли сигнал с планеты Мур.",
                "",
                "Наши друзья, инопланетные коты,",
                "нуждаются в помощи.",
                "Космические мыши хотят съесть их луну,",
                "потому что она похожа на сыр.",
                "Как долго наш народ страдал от них, ",
                "теперь и муряне в беде...",
                "Мы должны помочь им.",
                "Вылетаем прямо сейчас.",
                "Спасибо, что починил звездолёт, штурман. ",
                "Наконец-то функция автопилота работает.",
                "Поехали!",
                ""]
    alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
                "",
                "Мыши уже начали грызть луну...",
                "Скоро куски луны будут падать на нас.",
                "Спасите муриан!", 
                ""]
    final_text = ["Огромное вам спасибо,",
                "друзья с планеты Мяу!",
                "Как вас называть? Мяуанцы? Мяуриане?",
                "В любом случае, ",
                "теперь наша планета спасена!",
                "Мы хотим отблагодарить вас.",
                "Капитан Василий и его штурман получают",
                "орден 'Страж планеты Мур'.",
                "А также несколько бутылок нашей",
                "лучшей валерьянки.",
                "",
                ""]
    moods = ['start_scene', 
            'meteorites', 
            'alien_scene', 
            'moon', 
            'final_scene']


    # Load
    background = pygame.image.load('background.png')
    background = pygame.transform.scale(background, S)
    heart = pygame.image.load('heart.png').convert_alpha()
    heart = pygame.transform.scale(heart, (30, 30))
    hearts = 3
    laser_counter = 5


    # Classes and functions
    def dialogue_mode(sprite, text):
        global TN, M, T, G
        try:
            sprite.update()
            W.blit(sprite.image, sprite.rect)
            text_1 = F.render(text[TN], True, pygame.Color('white'))
            W.blit(text_1, (280, 450))
            text_2 = F.render(text[TN + 1], True, pygame.Color('white'))
            W.blit(text_2, (280, 480))
        except IndexError:
            if M != 'final_scene':
                M = moods[moods.index(M) + 1]
            else:
                G = False
            TN = 0
            T = time.time()


    # Create objects
    captain = Captain()
    alien = Alien()
    ship = Starship()

    meteorites = pygame.sprite.Group()
    mice = pygame.sprite.Group()
    lasers = pygame.sprite.Group()

    # Game circle
    while G:
        W.blit(background, (0, 0))

        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if M in ['start_scene', 'alien_scene', 'final_scene']:
                    TN += 2
                if e.key == pygame.K_SPACE and M == 'moon' and laser_counter > 0:
                    lasers.add(Laser(ship.rect.midtop))
                    laser_counter -= 1

        # Update
        if M == "start_scene":
            dialogue_mode(captain, start_text)
            # M = "final_scene"
        if M == "meteorites":
            for i in range(hearts):
                W.blit(heart, (i * 30, 0))

            ship.update()
            W.blit(ship.image, ship.rect)
            if random.randint(1, 50) == 1:
                meteorites.add(Meteorite())
            meteorites.update()
            meteorites.draw(W)
            hits = pygame.sprite.spritecollide(ship, meteorites, True)
            for h in hits:
                hearts -= 1
                if hearts == 0:
                    exit()
            if T + 20 <= time.time():
                M = 'alien_scene'
        if M == "alien_scene":
            dialogue_mode(alien, alien_text)
            ship.switch_mode()
        
        if M == "moon":
            for i in range(hearts):
                W.blit(heart, (i * 30, 0))

            ship.update()
            W.blit(ship.image, ship.rect)

            if random.randint(1, 50) == 1:
                mice.add(Mouse())

            mice.update()
            mice.draw(W)
            lasers.update()
            lasers.draw(W)
            enemy_laser.update()
            enemy_laser.draw(W)

            hits = pygame.sprite.spritecollide(ship, mice, True)
            for h in hits:
                hearts -= 1
                if hearts == 0:
                    exit()
            hits = pygame.sprite.spritecollide(ship, enemy_laser, True)
            for h in hits:
                hearts -= 1
                if hearts == 0:
                    exit()
            hunt = pygame.sprite.groupcollide(lasers, mice, True, True)
            for i in hunt:
                laser_counter += 1


            text = F.render(f'Lasers: {laser_counter}', True, pygame.Color('white'))
            W.blit(text, (200, 40))

            if T + 20 <= time.time():
                M = 'final_scene'


        if M == "final_scene":
            dialogue_mode(alien, final_text)

        pygame.display.flip()
        C.tick(FPS)
