"""
 RUBY RADIS'S FINAL GAME!
 SIMON SAYS
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (119, 66, 244)
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Simon Says!- Ruby Radis")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Text resources
my_font = pygame.font.SysFont('Times new Roman', 30, False, True)
lose_font = pygame.font.SysFont('Times new Roman', 200, False, False)
lose_text = my_font.render("WRONG! YOU LOOSE", True, WHITE)

# define variables
level = 1
index = 0
frame = 1

# music
click_sound = pygame.mixer.Sound("click.ogg")
background_music = pygame.mixer.Sound("Beach_01.ogg")
background_music.play()
# define lists
block_pattern = [0, 0, 0, 0]
player_pattern = []

# Button Class will create the main four sprites.
class Button(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([200, 200])
        self.rect = self.image.get_rect()
        self.color = color
        self.rect.x = x
        self.rect.y = y
        self.flash = 0

    def update(self): # This code make the sequence show up and flash.
        self.flash -= 1
        if self.flash < 0:
            self.image.fill(self.color)
        else:
            self.image.fill(WHITE)

# First cut screen
# This code will state the instructions and the change to the game once the screen is clicked
def cut_screen():
    done = False # this is defining the local variable
    my_font = pygame.font.SysFont('Times New Roman', 50, False, False)
    the_font = pygame.font.SysFont('Times New Roman', 20, False, False)
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        # --- Screen-clearing code goes here
        #Instructions
        screen.fill(BLACK)
        my_text = my_font.render("Welcome to Simon Says!", True, PURPLE)
        screen.blit(my_text, [100, screen_height / 2 - 50])
        the_text = the_font.render("You will see a light sequence show up. Use your mouse to copy the pattern.", True, YELLOW)
        screen.blit(the_text, [30, 260])
        the_text = the_font.render("Click the screen to begin!", True, YELLOW)
        screen.blit(the_text, [30, 300])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

cut_screen()
# Making the boxes
# Red Block
red_block = Button(RED, 50, 260)
red_block.number = 0
# Yellow Block
yellow_block = Button(YELLOW, 50, 40)
yellow_block.number = 1
# Green Block
green_block = Button(GREEN, 400, 260)
green_block.number = 2
# Blue Block
blue_block = Button(BLUE, 400, 40)
blue_block.number = 3

# Adding blocks(sprites) to the block group
block_group = pygame.sprite.Group()
block_group.add(red_block)
block_group.add(yellow_block)
block_group.add(green_block)
block_group.add(blue_block)

# Adding blocks(sprites) to the sprites group
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(red_block)
all_sprites_group.add(yellow_block)
all_sprites_group.add(green_block)
all_sprites_group.add(blue_block)

# This code goes through the length of the block pattern and flashes the block pattern and also draws the screen.
def play_pattern():
    for i in range(len(block_pattern)):  # Goes through length of block list
        for block in block_group:
            if block.number == block_pattern[i]:
                block.flash = 25  # flashes for this long
                for j in range(40):
                    all_sprites_group.update()
                    screen.fill(BLACK)

                    # drawing the blocks
                    all_sprites_group.draw(screen)

                    # Render the level text
                    # Blit text to screen
                    my_text = my_font.render("LEVEL:" + str(level), True, WHITE)
                    screen.blit(my_text, [260, 250])

                    # --- Go ahead and update the screen with what we've drawn.
                    pygame.display.flip()
                    clock.tick(60)


play_pattern() # runs player_pattern class

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if red_block.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, WHITE, [50, 260, 200, 200])  # draws white rectangle on top of color to make it look like it is flashing
                red_block.flash = 10  # flash for that long
                player_pattern.append(0)  # assigns a number to each block
                click_sound.play() # plays sound
            if yellow_block.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, WHITE, [50, 40, 200, 200])
                yellow_block.flash = 10
                player_pattern.append(1)
                click_sound.play()
            if green_block.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, WHITE, [400, 260, 200, 200])
                green_block.flash = 10
                player_pattern.append(2)
                click_sound.play()
            if blue_block.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, WHITE, [400, 40, 200, 200])
                blue_block.flash = 10
                player_pattern.append(3)
                click_sound.play()

    # --- Game logic should go here
    # mouse controls
    x, y = pygame.mouse.get_pos()

    # next level code
    if player_pattern == block_pattern:
        level += 1
        block_pattern.append(random.randrange(4))  # adds a random number to list
        player_pattern = []  # resets the player list
        play_pattern()  # runs player pattern class

    for i in range(len(player_pattern)):
        if player_pattern[i] != block_pattern[i]: # if the lists don't equal each other
                done = False  # this is defining the local variable
                my_font = pygame.font.SysFont('Times New Roman', 50, False, False)
                the_font = pygame.font.SysFont('Times New Roman', 20, False, False)
                while not done:
                    # --- Main event loop
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            done = True

                    # --- Screen-clearing code goes here
                    screen.fill(BLACK)
                    my_text = my_font.render("YOU LOSE :(", True, PURPLE)
                    screen.blit(my_text, [150, screen_height / 2 - 50])
                    the_text = the_font.render("SIMON SAYS GOOD LUCK NEXT TIME.", True, YELLOW)
                    screen.blit(the_text, [150, 260])

                    # --- Go ahead and update the screen with what we've drawn.
                    pygame.display.flip()

                    # --- Limit to 60 frames per second
                    clock.tick(60)
                done = True

    all_sprites_group.update()
    # --- Screen-clearing code goes here
    screen.fill(BLACK)

    # --- Drawing code should go here
    # drawing the blocks
    all_sprites_group.draw(screen)


    # Render the level text
    my_text = my_font.render("LEVEL:" + str(level), True, WHITE)
    screen.blit(my_text, [260, 250])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()