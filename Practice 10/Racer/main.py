import pygame, sys
from pygame.locals import *
import random, time

# Initialize Pygame engines
pygame.init()

# Setup Frames Per Second (FPS)
FPS = 60
FramePerSec = pygame.time.Clock()

# Define color constants (RGB)
RED    = (255, 0, 0)
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
YELLOW = (255, 255, 0)

# Game constants and variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
MONEY_SCORE = 0

# Create the game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# --- LOAD AND SCALE ASSETS ---
# Load background and scale it to fit the screen
background = pygame.transform.scale(pygame.image.load("animatedstreet.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load UI icon for money
moneta_img = pygame.transform.scale(pygame.image.load("money.png"), (30, 30))

# Setup Fonts for scoring and game over message
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)
game_over_txt = font_big.render("Game Over", True, BLACK)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # Load and resize coin image
        self.image = pygame.transform.scale(pygame.image.load("money.png"), (30, 30))
        self.rect = self.image.get_rect()
        # Initial random position at the top
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        # Move down and reset if it leaves the screen
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # Load and resize enemy car image
        self.image = pygame.transform.scale(pygame.image.load("enemy.png"), (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # Load and resize player car image
        self.image = pygame.transform.scale(pygame.image.load("player.png"), (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        # Handle player movement with arrow keys
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Initialize Sprites and Groups
P1 = Player()
E1 = Enemy()
M1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

money_group = pygame.sprite.Group()
money_group.add(M1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)

# Main Game Loop
while True:
    # Event handling (Exit game)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw Background
    DISPLAYSURF.blit(background, (0,0))
    
    # Render and draw Score UI
    scores_text = font_small.render(str(MONEY_SCORE), True, YELLOW)
    DISPLAYSURF.blit(moneta_img, (10, 10))
    DISPLAYSURF.blit(scores_text, (45, 13))
    
    # Update position and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Handle Coin collection
    if pygame.sprite.spritecollideany(P1, money_group):
        MONEY_SCORE += 1
        M1.rect.top = 0 # Reset coin position
        M1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Handle Collision with Enemy (Game Over)
    if pygame.sprite.spritecollideany(P1, enemies):
        try:
            pygame.mixer.Sound('crash.wav').play() # Play sound if available
        except: 
            pass 
        
        time.sleep(0.5)
        DISPLAYSURF.fill(RED) # Flash red screen
        DISPLAYSURF.blit(game_over_txt, (30, 250))
        pygame.display.update()
        time.sleep(2) # Pause before quitting
        pygame.quit()
        sys.exit()        
            
    # Refresh screen and maintain FPS
    pygame.display.update()
    FramePerSec.tick(FPS)