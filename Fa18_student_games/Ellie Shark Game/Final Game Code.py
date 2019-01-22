"""
 Pygame base template for opening a window
 Intro to Programming

 Ellie Buono
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (153, 215, 255)

pygame.init() #Starts Pygame

# Set the width and height of the screen [width, height]
screen_width = 1000
screen_height = 563
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Fish Game")

# Adding turtle to screen
class Turtle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("turtle.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

# Adding fish
class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("fish.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.change_x = 0
        self.change_y = 0
    def changesheep(self, x, y):
        self.change_x += x
        self.change_y += y
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

# Adding Shark
class Shark(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("shark.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.amount = 1
        self.change_x = random.randrange(-1, 0)
        self.change_y = random.randrange(-1, 0)

all_sprites_group = pygame.sprite.Group()
fish = Fish(0, 0)

enemy_group = pygame.sprite.Group()
for i in range(1):
    shark = Shark(0, 0)
    shark.rect.x = random.randrange(screen_width - shark.rect.width)
    shark.rect.y = random.randrange(screen_height - shark.rect.height)
    all_sprites_group.add(shark)

all_sprites_group.add(fish)
enemy_group.add(shark)

turtle_group = pygame.sprite.Group()
turtle = Turtle(0, 0)
turtle.rect.x = random.randrange(0, screen_width)
turtle.rect.y = random.randrange(0, screen_height)
all_sprites_group.add(turtle)
turtle_group.add(turtle)
'level = 1'


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

fish_x = 0
fish_y = 0
fish_xspeed = 0
fish_yspeed = 0
x_speed = 0
y_speed = 0
score = 1

# Begging screen
def cut_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 40, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLUE)
        my_text = my_font.render("Welcome to Nemo vs Shark", True, WHITE)
        my_text2 = my_font.render("Collect the turtle to get an extra point", True, WHITE)
        my_text3 = my_font.render("Click to Continue", True, WHITE)
        screen.blit(my_text, [310, 150])
        screen.blit(my_text2, [245, 200])
        screen.blit(my_text3, [380, 250])
        pygame.display.flip()
        clock.tick(60)
cut_screen()
# Images
background_image = pygame.image.load("ocean2.jpg")
fish_image = pygame.image.load("fish.png")
shark_image = pygame.image.load("shark.png")
turtle_image = pygame.image.load("turtle.png")

background_music = pygame.mixer.Sound("Baby Shark.wav")
# Musics
background_music.set_volume(1)
background_music.play(-1)


# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # How to move characters around
        # User pressed down on a key
        if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                fish.change_x = -5
            elif event.key == pygame.K_RIGHT:
                fish.change_x = 5
            elif event.key == pygame.K_UP:
                fish.change_y = -5
            elif event.key == pygame.K_DOWN:
                fish.change_y = 5

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fish.change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                fish.change_y = 0

    # --- Game logic should go here
    x, y = pygame.mouse.get_pos()
    all_sprites_group.update()
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    if x > 908:
        x = 908

    if y > 438:
        y = 438
# Hit list and death screen
    hit_list = pygame.sprite.spritecollide(fish, enemy_group, True)
    for shark in hit_list:
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            screen.fill(BLUE)
            my_font = pygame.font.SysFont("Calibri", 55, True, False)
            my_text = my_font.render("You Died!", True, WHITE)
            screen.blit(my_text,[411, 200])
            my_font = pygame.font.SysFont("Calibri", 45, True, False)
            my_text = my_font.render("Score: " + str(score), True, WHITE)
            screen.blit(my_text, [430, 240])
            pygame.display.flip()
            clock.tick(60)

    if fish.rect.x <= 0:
        fish.rect.x = 0
    if fish.rect.y <= 0:
        fish.rect.y = 0

    if fish.rect.y >= 450:
        fish.rect.y = 450

# Fish wins
    if fish.rect.x > screen_width:
        fish.rect.x = 0
        fish.rect.y = 0
        for i in range(1):
            shark = Shark(0, 0)
            shark.rect.x = random.randrange(screen_width - shark.rect.width)
            shark.rect.y = random.randrange(screen_height - shark.rect.height)
            all_sprites_group.add(shark)
            enemy_group.add(shark)
        for i in range(1):
            turtle = Turtle(0, 0)
            turtle.rect.x = random.randrange(0, screen_width)
            turtle.rect.y = random.randrange(0, screen_height)
            all_sprites_group.add(turtle)
            turtle_group.add(turtle)

# Moves shark around
    for shark in enemy_group:
        shark.rect.x += shark.change_x
        shark.rect.y += shark.change_y

        if shark.rect.x >= screen_width:
            shark.rect.x = screen_width
            shark.change_x *= -1
        if shark.rect.y >= screen_height:
            shark.rect.y = screen_height
            shark.change_y *= -1

        if shark.rect.x <= 0:
            shark.rect.x = 0
            shark.change_x *= -1
        if shark.rect.y <= 0:
            shark.rect.y = 0
            shark.change_y *= -1

        hit_list = pygame.sprite.spritecollide(fish, turtle_group,True)
        for turtle in hit_list:
            score += 1
            my_sound = pygame.mixer.Sound("Ding.wav")
            my_sound.play()

    # --- Screen-clearing code goes here

    screen.fill(WHITE)

    # --- Drawing code should go here
    # Writing the score
    screen.blit(background_image, [0, 0])
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    my_text = my_font.render("Score: " + str(score), True, WHITE)
    screen.blit(my_text, [40, 40])
    all_sprites_group.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()