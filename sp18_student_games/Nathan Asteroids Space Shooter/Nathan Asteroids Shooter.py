# PROGRAMMING FINAL

# Imports
import pygame
import random

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
LIGHT_BLUE = (175, 225, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (220, 100, 0)
FIREORANGE = (255, 160, 0)
PINK = (255, 200, 200)
MAROON = (150, 0, 0)
DULLGREEN = (125, 150, 75)
PPYBROWN = (150, 83, 17)
MATRIX = (21, 255, 0)
DANKBLUE = (49, 58, 104)
MINT = (80, 210, 110)
colorG = 255
colorB = 255

# Initialize Pygame
pygame.init()

# Set Display
pygame.display.set_caption("PROGRAMMING FINAL")

# Screen Size
screen_width = 800
screen_height = 650
screen = pygame.display.set_mode([screen_width, screen_height])

# Set Clock and Frames
clock = pygame.time.Clock()

# Game Variables
score = 0
health = 5
level = 0
frames = 0
done = False

# Text
font = pygame.font.SysFont('Calibri', 40, True, False)

# Sounds
laser_sound = pygame.mixer.Sound("laser.wav")
collide_sound = pygame.mixer.Sound("collide.wav")
death_sound = pygame.mixer.Sound("death.wav")
background_music = pygame.mixer.Sound("background.wav")

# Player Image
player_image = pygame.image.load("player.png")

# Classes
class Player(pygame.sprite.Sprite): # Defining the player class.
    def __init__(self, x, y):
        super().__init__()

        self.image = player_image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 570

        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0

class Enemy(pygame.sprite.Sprite): # Defining the first type of enemy, asteroids.
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speedx = random.randrange(-4, 5)
        self.speedy = 3
    def update(self):
        self.rect.y = self.rect.y + 5
        if self.rect.top > screen_height:
            self.rect.bottom = 0
            self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.x = self.rect.x + self.speedx
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.speedx = self.speedx * -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = self.speedx * -1

class Enemy2(pygame.sprite.Sprite): # Defining the second type of enemy, spaceships.
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speedx = random.randrange(-4, 5)
        self.speedy = 3
    def update(self):
        self.rect.y = self.rect.y + 5
        if self.rect.top > screen_height:
            self.rect.bottom = 0
            self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.x = self.rect.x + self.speedx
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.speedx = self.speedx * -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = self.speedx * -1

class Bullet(pygame.sprite.Sprite): # Defining the player's bullets.
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png")
        self.rect = self.image.get_rect()
        self.speedy = -10
    def update(self):
        self.rect.y = self.rect.y + self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Laser(pygame.sprite.Sprite): # Defining the enemy's bullets.
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy_laser.png")
        self.rect = self.image.get_rect()
        self.speedy = 12
    def update(self):
        self.rect.y = self.rect.y + self.speedy
        if self.rect.top > screen_height:
            self.kill()

# Functions
def intro_screen(): # Defining the intro screen before the game starts.
    done = False
    my_font = pygame.font.SysFont("Calibri", 100, True, False)
    my_font2 = pygame.font.SysFont("Calibri", 50, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(BLACK)
        text = my_font.render("ASTEROID FIELD", True, RED)
        text2 = my_font2.render("USE ARROW KEYS TO MOVE", True, LIGHT_BLUE)
        text3 = my_font2.render("USE SPACE BAR TO SHOOT", True, LIGHT_BLUE)
        text4 = my_font2.render("PRESS ANY KEY TO CONTINUE", True, LIGHT_BLUE)
        text5 = my_font2.render("TRY TO GET THE HIGHEST SCORE!", True, LIGHT_BLUE)
        screen.blit(text, [80, 100])
        screen.blit(text2, [80, 400])
        screen.blit(text3, [80, 480])
        screen.blit(text4, [80, 560])
        screen.blit(text5, [80, 320])
        pygame.display.flip()
        clock.tick(60)

def end_screen(): # Defining the end screen after the player loses.
    done = False
    my_font = pygame.font.SysFont("Calibri", 100, True, False)
    my_font2 = pygame.font.SysFont("Calibri", 50, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)
        text = my_font.render("YOU DIED IN SPACE", True, LIGHT_BLUE)
        text2 = my_font2.render("TO PLAY AGAIN, EXIT AND RELOAD", True, LIGHT_BLUE)
        text3 = my_font2.render("FINAL SCORE: " + str(score), True, RED)
        screen.blit(text, [20, 100])
        screen.blit(text2, [40, 400])
        screen.blit(text3, [220, 200])
        pygame.display.flip()
        clock.tick(60)

# Define Lists
all_sprites_list = pygame.sprite.Group()
good_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_bullet_list = pygame.sprite.Group()
alien_list = pygame.sprite.Group()
star_list = []

# Create Sprites
player = Player(355, 0) # Creating the player.
all_sprites_list.add(player)

for i in range(5): # Creating the enemies.
    enemy = Enemy()
    enemy.rect.x = random.randrange(0, screen_width - enemy.rect.width)
    enemy.rect.y = random.randrange(-screen_height - enemy.rect.height, 0)
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)

for i in range(500): # Creating the stars for the background.
    x = random.randrange(screen_width)
    y = random.randrange(screen_height)
    speed = random.random() + .1
    star_list.append([x, y, speed])

# Game Loop --------------------------------------------------------------------

# Create the Intro Screen.
intro_screen()

# Play Background Music
background_music.play(-1)

# Main Game Code
while not done:

    # Get player Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN: # Setting up left-right controls with arrow keys.
            if event.key == pygame.K_LEFT:
                player.changespeed(-12, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(12, 0)

            elif event.key == pygame.K_SPACE: # Setting up shooting controls with space bar.
                bullet = Bullet()
                bullet.rect.centerx = player.rect.centerx
                bullet.rect.centery = player.rect.centery
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                laser_sound.play()

        elif event.type == pygame.KEYUP: # Releasing movement keys.
            if event.key == pygame.K_LEFT:
                player.changespeed(12, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-12, 0)

    # Filling Screen with Black Space
    screen.fill(BLACK)

    # Blitting Stars onto Background
    for i in range(len(star_list)):
        star_list[i][1] += star_list[i][2]
        if star_list[i][1] > 650:
            star_list[i][1] = -4
        pygame.draw.ellipse(screen, WHITE, [star_list[i][0], star_list[i][1], 1, 1])

    # Updating Lists
    all_sprites_list.update()
    enemy_list.update()
    bullet_list.update()
    enemy_bullet_list.update()

    # Level Mechanics
    for alien in alien_list:
        if random.randrange(60 - (level + 3)) == 0:
            laser = Laser()
            laser_sound.play()
            laser.rect.center = alien.rect.center
            enemy_bullet_list.add(laser)
            all_sprites_list.add(laser)

    if len(enemy_list) == 0:
        level = level + 1
        for i in range(level + 5):
            enemy = Enemy()
            enemy.speedy = level * 1.5
            enemy.rect.x = random.randrange(0, screen_width - enemy.rect.width)
            enemy.rect.y = random.randrange(-screen_height - enemy.rect.height, 0)
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)

        for i in range(level):
            alien = Enemy2()
            alien.speedy = level * 1.5
            alien.rect.x = random.randrange(0, screen_width - enemy.rect.width)
            alien.rect.y = random.randrange(-screen_height - enemy.rect.height, 0)
            all_sprites_list.add(alien)
            alien_list.add(alien)
            enemy_list.add(alien)

    # Collision Checks
    hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
    for enemy in hit_list:
        collide_sound.play()
        colorG -= 50
        colorB -= 60
        health -= 1

    for bullet in bullet_list:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        for enemy in hit_list:
            collide_sound.play()
            bullet.kill()
            score += 1

    hit_list = pygame.sprite.spritecollide(player, enemy_bullet_list, True)
    for laser in hit_list:
        collide_sound.play()
        colorG -= 50
        colorB -= 60
        health -= 1

    # Health Check
    if health <= 0:
        done = True
        background_music.stop()
        death_sound.play()
        end_screen()

    # Drawing Sprites to the Screen
    all_sprites_list.draw(screen)

    # Blitting Text for Score, Level, and Health
    text = font.render("Score: " + str(score), True, WHITE)
    text2 = font.render("Level: " + str(level), True, WHITE)
    text3 = font.render("Health: " + str(health), True, [255, colorG, colorB])
    screen.blit(text, [5, 5])
    screen.blit(text3, [5, 75])
    screen.blit(text2, [5, 40])

    # Update Screen
    pygame.display.flip()

    # Set Frames
    clock.tick(30)

# Quit Pygame
pygame.quit()