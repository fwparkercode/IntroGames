# Final Game

import pygame
import random

# Define some colors
BLACK = (0, 0, 0) # (red ,green ,blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
YellOW = (255,255,0)
CYAN = ( 0, 255, 255)
MAGENTA = (255, 0 , 255)

pygame.init()

enemy_sound = pygame.mixer.Sound("shooting_star.wav")
enemy_sound.set_volume(0.5)
background_sound = pygame.mixer.Sound("Battle.ogg")
background_sound.play(-1)

# Set the width and height of the screen [width, height]
screen_height = 500
screen_width = 700
size = (screen_width, screen_height)
pygame.display.set_caption("Care Beat scare")

screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Text resources
my_font = pygame.font.SysFont('Calibri', 30, True, False)

# Image resources
background_image = pygame.image.load("rainbowland.png")

# Vairables
# Current score
score = 0

# level
level = 1

# Lives

lives = 5



# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# CLASSES

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Cheerbear.png")
        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width)
        self.rect.y = random.randrange(-screen_height, 0)
        self.change_y = 1
    def update(self):
        self.rect.y+= self.change_y


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 8])
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.speed_y = -12

    def update(self):

        self.rect.y+= self.speed_y
        if self.rect.bottom <0:
            self.kill()


all_sprites_group = pygame.sprite.Group()
player = Player()
player.rect.bottom = screen_height
all_sprites_group.add(player)

enemy_group = pygame.sprite.Group()
for i in range(level * 10):
    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)

bullet_group = pygame.sprite.Group()
pygame.mouse.set_visable = False

def cut_screen():
    done = False
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True


        screen.fill(WHITE)


        # Render the score text
        my_text = my_font.render("Hi Welcome to Care Bear Scare!", True, CYAN)
        screen.blit(my_text, [18, 50])



        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)



cut_screen()


def end_screen():
    done = False
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True


        screen.fill(WHITE)


        # Render the score text
        my_text = my_font.render("GAME OVER THANKS FOR PLAYING!", True, MAGENTA)
        screen.blit(my_text, [18, 50])



        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)





# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.centerx = event.pos[0]
            bullet.rect.centery = player.rect.centery
            bullet_group.add(bullet)
            all_sprites_group.add(bullet)

            # --- Game logic should go here
    all_sprites_group.update()
    pos = pygame.mouse.get_pos()
    player.rect.centerx = pos[0]

    '''hit_list = pygame.sprite.spritecollide(player, enemy_group, True)
    for hit in hit_list:
        lives -= 1
        if lives <= 0:
            done = True
            '''
    for enemy in enemy_group:
        if enemy.rect.top > screen_height:
            enemy.rect.y = random.randrange(-screen_height, 0)
            lives -= 1
            if lives <= 0:
                end_screen()
                done = True

    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for hit in hit_list:
            enemy_sound.play()
            score += 1
            print(score)



        for hit in hit_list:
            bullet.kill()


    if len(enemy_group) == 0:
        level += 1
        for i in range( 2 * level):
            enemy = Enemy()
            enemy.change_y += level / 2
            enemy.rect.x = random.randrange(screen_width)
            enemy.rect.y = random.randrange(-screen_height, 0)
            enemy_group.add(enemy)
            all_sprites_group.add(enemy)















    # --- Screen-clearing code goes here
    screen.fill(WHITE)
    screen.blit(background_image, [-75, -30])

    # Render the score text
    my_text = my_font.render("Score: " + str(score), True, BLUE)
    screen.blit(my_text, [50, 50])
    my_text = my_font.render("Level: " + str(level), True, BLUE)
    screen.blit(my_text, [50, 70 ])
    my_text = my_font.render("Lives: " + str(lives), True, BLUE)
    screen.blit(my_text, [50, 90])

    # --- Drawing code should go below here!!
    all_sprites_group.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
