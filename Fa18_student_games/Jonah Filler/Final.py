"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0) # (Red, green, blue)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (120,120,120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
pygame.init()

total_area = 0
percent = 0
level = 1
lives_list = []
background_music = pygame.mixer.Sound('baclground.wav')
pop = pygame.mixer.Sound('pop.wav')

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

bad_block_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Size
        self.size = 0
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.growing = True

    # Grow method
    def grow(self):
        my_pos = self.rect.center
        self.size += 1
        self.image = pygame.Surface([self.size, self.size])
        self.rect = self.image.get_rect()
        self.rect.center = my_pos
        self.far_x = self.rect.center[0] + self.size * .5
        self.near_x = self.rect.center[0] - self.size *.5
        self.far_y = self.rect.center[1] + self.size * .5
        self.near_y = self.rect.center[1] - self.size *.5
    def update(self):
        if self.growing == True:
            self.grow()
            if self.far_x == screen_width:
                self.growing = False
            if self.far_y == screen_height:
                self.growing = False
            if self.near_x == 0:
                self.growing = False
            if self.near_y == 0:
                self.growing = False
        if self.growing == True:
            hit_list = pygame.sprite.spritecollide(self, bad_block_group, False)
            for hit in hit_list:
                self.kill()
                pop.play()
                pop.set_volume(20)
                lives_list.append(1)
                print(lives_list)
            hit_list_2 = pygame.sprite.spritecollide(self, block_group, False)
            if len(hit_list_2) > 1:
                self.growing = False





class Bad_Blocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - 5)
        self.rect.y = random.randrange(0, screen_height - 5)
        self.speed_x = random.randrange(-3, 3)
        self.speed_y = random.randrange(-3, 3)
        if self.speed_x == 0:
            self.speed_x = random.randrange(-3, 3)
        if self.speed_y == 0:
            self.speed_y = random.randrange(-3, 3)
        bad_block_group.add(self)
        all_sprites_group.add(self)
    def update(self):
        self.rect.x += self.speed_x
        hit_list = pygame.sprite.spritecollide(self, block_group, False)
        for hit in hit_list:
            if self.speed_x > 0:
                self.rect.right = hit.rect.left
                self.speed_x *= -1
            else:
                self.rect.left = hit.rect.right
                self.speed_x *= -1

        self.rect.y += self.speed_y
        hit_list = pygame.sprite.spritecollide(self, block_group, False)
        for hit in hit_list:
            if self.speed_y > 0:
                self.rect.bottom = hit.rect.top
                self.speed_y *= -1
            else:
                self.rect.top = hit.rect.bottom
                self.speed_y *= -1

        if self.rect.x <= 0:
            self.speed_x = -self.speed_x
        if self.rect.y <= 0:
            self.speed_y = -self.speed_y
        if self.rect.x >= screen_width:
            self.speed_x = -self.speed_x
        if self.rect.y >= screen_height:
            self.speed_y = -self.speed_y




for i in range (level * 5 + 10):
    bad_blocks = Bad_Blocks()
    bad_blocks.update()




pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def intro_screen():
    done = False
    frame = 0
    my_font = pygame.font.SysFont('Helvetica', 40, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(BLACK)
        my_text = my_font.render('Click to start.', True, WHITE)
        my_text_2 = my_font.render('Welcome to Filler!', True, WHITE)
        my_text_3 = my_font.render('The goal is to fill as much of', True, WHITE)
        my_text_7 = my_font.render('the screen as you can.', True, WHITE)
        my_text_4 = my_font.render('But don\'t get hit while growing.', True, WHITE)
        my_text_5 = my_font.render('You get 3 lives.', True, WHITE)
        my_text_6 = my_font.render('To start off, fill 10 %.', True, WHITE)
        screen.blit(my_text, [230, 440 - 10])
        screen.blit(my_text_2, [180, 80 - 10])
        screen.blit(my_text_3, [100, 140 - 10])
        screen.blit(my_text_7, [150,200 - 10])
        screen.blit(my_text_4, [60, 260 - 10])
        screen.blit(my_text_5, [210, 320 - 10])
        screen.blit(my_text_6, [150, 380 - 10])

        pygame.display.flip()
        clock.tick(60)

def cut_screen():
    done = False
    my_font = pygame.font.SysFont("Helvetica", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        my_text = my_font.render('You are on level ' + str(level) + '.', True, WHITE)
        my_text_2 = my_font.render('You need to fill ' + str(level * 5 + 5) + '% of the screen', True, WHITE)
        screen.blit(my_text, [240, 230])
        screen.blit(my_text_2, [125, 300])

        pygame.display.flip()
        clock.tick(60)

def end_screen():
    done = False
    my_font = pygame.font.SysFont("Helvetica", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        my_text = my_font.render("YOU LOST.", True, WHITE)
        screen.blit(my_text, [280, 100])

        pygame.display.flip()
        clock.tick(60)


intro_screen()

growing = False


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_block = Player()
            new_block.rect.center = event.pos
            all_sprites_group.add(new_block)
            block_group.add(new_block)

        if event.type == pygame.MOUSEBUTTONUP:
            for block in block_group:
                block.growing = False
            print(percent)
    total_area = 0
    for block in block_group:
        total_area += block.size ** 2
    percent = round(total_area/350000 * 100, 2)
    all_sprites_group.update()

    background_music.play()
    background_music.set_volume(.1)

    if percent >= (level * 5) + 5:
        total_area = 0
        level += 1
        all_sprites_group.empty()
        bad_block_group.empty()
        block_group.empty()
        cut_screen()
        lives_list = []
        for i in range(level * 10):
            bad_blocks = Bad_Blocks()
            bad_blocks.update()

    if len(lives_list) == 3:
        end_screen()
        done = True



    # --- Game logic should go here


    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    all_sprites_group.draw(screen)

    my_font = pygame.font.SysFont("Helvetica", 20, True, False)
    my_text = my_font.render(str(percent) + "%", True, RED)
    screen.blit(my_text, [630,10])

    my_font = pygame.font.SysFont("Helvetica", 20, True, False)
    my_text = my_font.render('Lives lost:' + str(len(lives_list)), True, RED)
    screen.blit(my_text, [0,10])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
