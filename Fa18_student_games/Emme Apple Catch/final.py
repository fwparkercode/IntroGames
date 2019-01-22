"""
 Pygame base template for opening a window

Into to programming
Emme Silverman 2018
"""

import pygame
import random
pygame.init()

# Define some colors
BLACK = (0, 0, 0) # (red, green, blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


background_music = pygame.mixer.Sound("bensound-jazzcomedy.wav")
background_music.set_volume(0.5)
background_music.play()


apple_sound = pygame.mixer.Sound("apple_sound.wav")
bomb_sound = pygame.mixer.Sound("Buzzer-SoundBible.com-188422102.wav")

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
block_list = pygame.sprite.Group()
level = 1

pygame.display.set_caption("My Game")
background_image = pygame.image.load("background_image.png")
# names itc


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("basket.png")
        self.rect = self.image.get_rect()

class Block(pygame.sprite.Sprite):
    def __init__(self, file):
        super().__init__()
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.speed = random.randrange(5, 12)
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= screen_height:
            self.rect.y = -5
        if self.rect.y >= screen_width:
            self.rect.y = -10 * screen_height







all_sprites_group = pygame.sprite.Group()
player = Player()
player.rect.bottom = screen_height
all_sprites_group.add(player)

# Sprites lists
all_sprites_list = pygame.sprite.Group()
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
my_font = pygame.font.SysFont('Calibri', 30, True, False)

def intro_screen():

    done = False
    while not done:
        # --- Intro event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        screen.fill(WHITE)

        # --- Drawing code should go here
        intro_text = my_font.render("Welcome to Apple Hunt", True, BLACK)
        my_text = my_font.render("Click to Continue", True, BLACK)
        instruct_text = my_font.render("Avoid the bombs and catch as many apples as possible.", True, BLACK)
        instruct_text3 = my_font.render("When you run out of lives, the game is over.", True, BLACK)

        # blit the text to the screen.
        screen.blit(my_text, [screen_width / 2 - 50, screen_height / 2])
        screen.blit(intro_text, [screen_width / 2 - 70, screen_height / 2 - 25])
        screen.blit(instruct_text, [50, 50])
        screen.blit(instruct_text3, [50, 100])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second



intro_screen()

for i in range(100):
    # This represents a block
    good_block = Block("good_apple.png")

    # Set a random location for the block
    good_block.rect.x = random.randrange(screen_width - good_block.rect.width)
    good_block.rect.y = random.randrange(-screen_height * 10, 0)

    # Add the block to the list of objects
    good_block_list.add(good_block)
    all_sprites_group.add(good_block)

for i in range(5):
    # This represents a block
    bad_block = Block("bomb.png")

    # Set a random location for the block
    bad_block.rect.x = random.randrange(screen_width)
    bad_block.rect.y = random.randrange(-screen_height * 10, 5)

    # Add the block to the list of objects
    bad_block_list.add(bad_block)
    all_sprites_group.add(bad_block)


# Loop until the user clicks the close button.
done = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()


lives = 5
score = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    all_sprites_group.update()
    pos = pygame.mouse.get_pos()
    player.rect.centerx = pos[0]

    if score >= 20 * level:
        level += 1
        lives += 1
        print(level)
        for i in range(20):
            # This represents a block
            good_block = Block("good_apple.png")

            # Set a random location for the block
            good_block.rect.x = random.randrange(screen_width - good_block.rect.width)
            good_block.rect.y = random.randrange(-screen_height * 10, 0)
            good_block.speed = level * 2

            # Add the block to the list of objects
            good_block_list.add(good_block)
            all_sprites_group.add(good_block)

        for i in range(3):
            # This represents a block
            bad_block = Block("bomb.png")

            # Set a random location for the block
            bad_block.rect.x = random.randrange(screen_width)
            bad_block.rect.y = random.randrange(-screen_height * 10, 5)
            bad_block.speed = level * 2

            # Add the block to the list of objects
            bad_block_list.add(bad_block)
            all_sprites_group.add(bad_block)



     # paints screen
    screen.blit(background_image, [0, 0])

    blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)

    for good_block in blocks_hit_list:
        apple_sound.play()
        score += 1
        print(score)


    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)

    for bad_block in bad_blocks_hit_list:
        bomb_sound.play()
        lives += -1
        print(lives)


    all_sprites_list.draw(screen)

    my_text = my_font.render("Score: " + str(score), True, BLACK)
    screen.blit(my_text, [50, 50])
    my_text = my_font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(my_text, [50, 100])
    my_text = my_font.render("Level " + str(level), True, BLACK)
    screen.blit(my_text, [50, 150])


    if lives <= 0:
        my_text = my_font.render("GAME OVER", True, BLACK)
        screen.blit(my_text, [320, 100])
        my_text = my_font.render("You made it to level: " + str(level), True, BLACK)
        screen.blit(my_text, [320, 150])
        for block in good_block_list:
            block.kill()
        for block in bad_block_list:
            block.kill()




    # --- Drawing code should go here

    all_sprites_group.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()