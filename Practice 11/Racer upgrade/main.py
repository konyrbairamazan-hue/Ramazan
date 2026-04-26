# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Init
pygame.init()
pygame.mixer.init()

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Game vars
SPEED = 5
MONEY_SCORE = 0
next_speed = 10

# Images
background = pygame.image.load("AnimatedStreet.png")
player_img = pygame.image.load("Player.png")
enemy_img = pygame.image.load("Enemy.png")

bronze_coin = pygame.image.load("bronze_coin.png")
silver_coin = pygame.image.load("silver_coin.png")
gold_coin = pygame.image.load("golden_coin.png")

# Sounds
bgsound = pygame.mixer.Sound("background.wav")
crash_sound = pygame.mixer.Sound("crash.wav")
coin_sound = pygame.mixer.Sound("lost_money.wav")

bgsound.set_volume(0.4)
crash_sound.set_volume(1.0)
coin_sound.set_volume(1.0)

bgsound.play(-1)  # цикл

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# -------- CLASSES --------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(160, 520))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH-40), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.types = [
            {"image": bronze_coin, "value": 1},
            {"image": silver_coin, "value": 2},
            {"image": gold_coin, "value": 3}
        ]
        self.reset()

    def reset(self):
        t = random.choice(self.types)
        self.image = t["image"]
        self.value = t["value"]
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH-40), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()


# -------- OBJECTS --------

P1 = Player()
E1 = Enemy()
M1 = Coin()

enemies = pygame.sprite.Group(E1)
money = pygame.sprite.Group(M1)
all_sprites = pygame.sprite.Group(P1, E1, M1)

# -------- GAME LOOP --------

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Speed up
    if MONEY_SCORE >= next_speed:
        SPEED += 2
        next_speed += 10

    # Background
    DISPLAYSURF.blit(background, (0, 0))

    # Move & draw
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Enemy collision
    if pygame.sprite.spritecollideany(P1, enemies):
        bgsound.stop()
        crash_sound.play()
        time.sleep(0.5)

        waiting = True
        while waiting:
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30, 250))

            score = font_small.render(f"Score: {MONEY_SCORE}", True, BLACK)
            DISPLAYSURF.blit(score, (150, 320))

            restart = font_small.render("R - restart", True, BLACK)
            quit_t = font_small.render("Q - quit", True, BLACK)

            DISPLAYSURF.blit(restart, (140, 500))
            DISPLAYSURF.blit(quit_t, (150, 530))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_r:
                        MONEY_SCORE = 0
                        SPEED = 5
                        next_speed = 10
                        E1.rect.top = 0
                        M1.reset()
                        bgsound.play(-1)
                        waiting = False

                    if event.key == K_q:
                        pygame.quit()
                        sys.exit()

    # Coin collision
    if pygame.sprite.spritecollideany(P1, money):
        coin_sound.play()
        MONEY_SCORE += M1.value
        M1.reset()

    # UI
    DISPLAYSURF.blit(bronze_coin, (5, 40))
    DISPLAYSURF.blit(silver_coin, (5, 70))
    DISPLAYSURF.blit(gold_coin, (5, 100))

    DISPLAYSURF.blit(font_small.render("1", True, BLACK), (30, 40))
    DISPLAYSURF.blit(font_small.render("2", True, BLACK), (30, 70))
    DISPLAYSURF.blit(font_small.render("3", True, BLACK), (30, 100))

    score_text = font_small.render(str(MONEY_SCORE), True, YELLOW)
    DISPLAYSURF.blit(score_text, (10, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)