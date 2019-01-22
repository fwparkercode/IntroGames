#Emily Simon is bae

import pygame
import random
pygame.init()

# Define some colors
BLACK = (0, 0, 0)   # (red, green, blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

background_image = pygame.image.load("background.jpg")

fish_sound = pygame.mixer.Sound("good_block.wav")
shark_sound = pygame.mixer.Sound("bad_block.wav")

background_music = pygame.mixer.Sound("fish.ogg")
background_music.play(-1)
background_music.set_volume(0.2)



#splash = pygame.mixer.Sound("splash.wav")

pygame.display.set_caption("Fishbowl Final - Emily Simon")

done = False
score = 0
lives = 3
level = 1

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# make my font(s)
# SysFont('font_name', font_size, bold, italics)
def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Times New Roman", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        screen.blit(background_image, [0, 0])
        text = my_font.render("WELCOME TO FISHBOWL!!", True, WHITE)
        text2 = my_font.render("Move the bowl to catch the fish but avoid the sharks!", True, BLACK)
        text11 = my_font.render("Move the left and right arrows to control the bowl", True, BLACK)
        text5 = my_font.render("The orange fish is worth three points", True, BLACK)
        text6 = my_font.render("The green fish is worth two points", True, BLACK)
        text7 = my_font.render("The blue fish is worth one point", True, BLACK)
        text3 = my_font.render("Press the mouse to begin!", True, BLACK)
        screen.blit(text, [150, 0])
        screen.blit(text2, [0, 150])
        screen.blit(text11, [0, 200])
        screen.blit(text6, [0, 300])
        screen.blit(text7, [0, 250])
        screen.blit(text5, [0, 350])
        screen.blit(text3, [350, 470])
        pygame.display.flip()
        clock.tick(60)
done = intro_screen()

def end_screen():
    done = False
    my_font = pygame.font.SysFont("Times New Roman", 60, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        screen.blit(background_image, [0, 0])
        text = my_font.render("GAME OVER", True, WHITE)
        textt = my_font.render("GAME OVER", True, BLACK)


        screen.blit(text, [170, 225])
        screen.blit(textt, [172, 223])



        pygame.display.flip()
        clock.tick(60)



# CLASSES

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(BLACK)
        self.image = pygame.image.load("fishbowl.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 500
        self.speedx = 0
    def changespeed(self, x):
        self.speedx += x

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > 640:
            self.rect.x = 640
        if self.rect.x < 0:
            self.rect.x = 0

class Enemy_good(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(GREEN)
        self.image = pygame.image.load("fish1.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(0, 200)
        self.changey = 1
        self.value = 1
    def update(self):
        self.rect.y += self.changey
        if self.rect.y > 505:
            self.rect.y = -30

class Enemy_good2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(GREEN)
        self.image = pygame.image.load("fish2.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(0, 200)
        self.changey = 1
    def update(self):
        self.rect.y += self.changey
        if self.rect.y > 505:
            self.rect.y = -30

class Enemy_good3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(GREEN)
        self.image = pygame.image.load("fish3.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(0, 200)
        self.changey = 1
    def update(self):
        self.rect.y += self.changey
        if self.rect.y > 505:
            self.rect.y = -30

class Enemy_bad(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(RED)
        self.image = pygame.image.load("shark.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(0, 200)
        self.changey = 1
    def update(self):
        self.rect.y += self.changey
        if self.rect.y > 505:
            self.rect.y = -30


all_sprites_group = pygame.sprite.Group()
player = Player(0, 0)
player.rect.bottom = screen_height + 15
all_sprites_group.add(player)

enemy_good_group = pygame.sprite.Group()
enemy_bad_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()


for i in range(1):
    enemy = Enemy_good(0, 0)
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)
    enemy_good_group.add(enemy)
    enemy.changey = 5
    enemy.value = 3

for i in range(6):
    enemy = Enemy_good2(0, 0)
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)
    enemy_good_group.add(enemy)
    enemy.changey = 3
    enemy.value = 1

for i in range(3):
    enemy = Enemy_good3(0, 0)
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)
    enemy_good_group.add(enemy)
    enemy.changey = 4
    enemy.value = 2


for i in range(4):
    enemy = Enemy_bad(0, 0)
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)
    enemy_bad_group.add(enemy)
    enemy.changey = 1


bullet_group = pygame.sprite.Group()


pygame.mouse.set_visible(False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.speedx = 4
            if event.key == pygame.K_LEFT:
                player.speedx = -4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.speedx = 0
            if event.key == pygame.K_LEFT:
                player.speedx = 0



    # --- Game logic should go here
    all_sprites_group.update()



    hit_list = pygame.sprite.spritecollide(player, enemy_good_group, False)
    for hit in hit_list:
        hit.rect.bottom = 0
        score += hit.value
        fish_sound.play()


    for enemy in enemy_bad_group:
        hit_list = pygame.sprite.spritecollide(player, enemy_bad_group, True)
        for hit in hit_list:
            hit.rect.bottom = 0
            lives -= 1
            shark_sound.play()

# ---------LEVELS -------------

    if score >= 20 * level:
        level += 1
        enemy_good_group.empty()
        enemy_bad_group.empty()
        all_sprites_group.empty()
        all_sprites_group.add(player)

        for i in range(1):
            enemy = Enemy_good(0, 0)
            all_sprites_group.add(enemy)
            enemy_group.add(enemy)
            enemy_good_group.add(enemy)
            enemy.value = 3
            enemy.changey = 5 + (level/3)


        for i in range(6):
            enemy = Enemy_good2(0, 0)
            all_sprites_group.add(enemy)
            enemy_group.add(enemy)
            enemy_good_group.add(enemy)
            enemy.value = 1
            enemy.changey = 3 + (level/3)

        for i in range(3):
            enemy = Enemy_good3(0, 0)
            all_sprites_group.add(enemy)
            enemy_group.add(enemy)
            enemy_good_group.add(enemy)
            enemy.value = 2
            enemy.changey = 4 + (level/3)

        for i in range(4):
            enemy = Enemy_bad(0, 0)
            all_sprites_group.add(enemy)
            enemy_group.add(enemy)
            enemy_bad_group.add(enemy)
            enemy.changey = 1 + (level/2)


    if lives <= 0:
        end_screen()
        done = True

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)


    # --- Drawing code should go here
    screen.blit(background_image, [0,0])

    all_sprites_group.draw(screen)

    my_font = pygame.font.SysFont('Times New Roman', 30, True, False)


    my_text = my_font.render("Score: " + str(score), True, BLACK)
    screen.blit(my_text, [15, 12])

    my_lives = my_font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(my_lives, [240, 12])

    my_level = my_font.render("Level: " + str(level), True, BLACK)
    screen.blit(my_level, [450, 12])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()