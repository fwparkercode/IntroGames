"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc

 Noah Keim 2018
"""

import pygame
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

wall_num = 0
level = 1


# Player Function, Jump makes the player jump,
# changespeed changes the x speed of the player and update adds position,
# checks for collisions and keeps the sprite on the screen.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Sprite.png")
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = 100
        self.rect.y = screen_height - 40
        self.accely = .2
        self.jumps = 2


    def jump(self):
        if self.jumps > 0:
            self.change_y = -5



    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x




    def update(self):
        """ Find a new position for the player"""
        self.change_y += self.accely
        self.rect.y += self.change_y

        hit_list = pygame.sprite.spritecollide(self, self.wall_list, False)
        for wall in hit_list:
            if self.change_y  > 0:
                self.rect.bottom = wall.rect.top
                self.change_y = 0
                self.jumps = 2
            else:
                self.rect.top = wall.rect.bottom
                self.change_y = 0



        self.rect.x += self.change_x

        hit_list = pygame.sprite.spritecollide(self, self.wall_list, False)
        for wall in hit_list:
            if self.change_x > 0:
                self.rect.right = wall.rect.left

            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = wall.rect.right



        if self.rect.right > screen_width:
            self.rect.right = screen_width
            for wall in wall_list:
                wall.kill()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_height - 20:
            self.rect.bottom = screen_height - 20
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.y >= screen_height - 40:
            self.jumps = 2




# Wall Class, Update checks for collisions and moves the walls across the screen

class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(MAGENTA)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.wall_count = 0
    def update(self):
        self.rect.x -= 1
        if pygame.sprite.collide_rect(self, one_player):
            one_player.rect.right = self.rect.left

        if pygame.sprite.collide_rect(self, side_wall):
            self.kill()
# Border class, a thin line on the side of the screen that
# checks for collisions and kills walls when they hit it.

class Border(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 0















pygame.init() #starts pygame
background = pygame.image.load("Background.jpg")

background_sound = pygame.mixer.Sound("Night Lights.wav")
background_sound.play(1000)


# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Final Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
one_player = Player()
side_wall = Border(1, screen_height)
side_wall.rect.x = 0




all_sprites_list.add(one_player)
all_sprites_list.add(side_wall)


# creates all the walls
for i in range(23 + (8 * level)):
    wall_num += 1
    wall = Wall(random.randrange(10, 80), random.randrange(10, 80))
    wall.rect.x = random.randrange(40, screen_width)
    wall.rect.y = random.randrange(20, screen_height - 40)
    all_sprites_list.add(wall)
    wall_list.add(wall)

one_player.wall_list = wall_list

# Cut screen function, when called shows a cut
# screen with the text being the variables
def cut_screen(text1, text2, text3):
    done = False # local variable done
    my_font = pygame.font.SysFont("Calibri", 50, True, False)
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
        screen.fill(BLACK)
        my_text1 = my_font.render(text1, True, WHITE)
        my_text2 = my_font.render(text2, True, WHITE)
        my_text3 = my_font.render(text3, True, WHITE)
        screen.blit(my_text1, [110, 200])
        screen.blit(my_text2, [130, 250])
        screen.blit(my_text3, [110, 300])

        pygame.display.flip()

        clock.tick(60)


cut_screen("Welcome to City Runner", "A game by Noah Keim", "Press Return to continue")







# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                one_player.changespeed(-5, 0)

            elif event.key == pygame.K_RIGHT:
                one_player.changespeed(5, 0)
            elif event.key == pygame.K_SPACE:
                one_player.jump()
                one_player.jumps -= 1


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                one_player.changespeed(5, 0)
            elif event.key == pygame.K_RIGHT:
                one_player.changespeed(-5, 0)

    # Checks if the player has lost
    if one_player.rect.left == 0:
        cut_screen("Game Over", "Press Return to play again", "")
        level = 1

        for wall in wall_list:
            wall.kill()
        for i in range(23 + (8 * level)): # Restarts the game
            wall_num += 1
            wall = Wall(random.randrange(10, 70), random.randrange(10, 70))
            wall.rect.x = random.randrange(60, screen_width)
            wall.rect.y = random.randrange(20, screen_height - 40)
            all_sprites_list.add(wall)
            wall_list.add(wall)
        one_player.rect.x = 100
        one_player.rect.y = screen_height - 40
        one_player.change_x = 0
        one_player.change_y = 0

    # checks if the player has won the game
    if level == 6:
        cut_screen("You won!!!!!", "Thanks for playing", "Press Return to Exit")

    # checks if the player has completed the level
    wall_num = 0
    for wall in wall_list:
        wall_num += 1
    if wall_num == 0:
        level += 1
        cut_screen("Next level", "Good Luck", "Press Return to continue")
        for i in range(23 + (8 * level)):
            wall_num += 1
            wall = Wall(random.randrange(10, 70), random.randrange(10, 70))
            wall.rect.x = random.randrange(60, screen_width)
            wall.rect.y = random.randrange(20, screen_height - 40)
            all_sprites_list.add(wall)
            wall_list.add(wall)
        one_player.rect.x = 100
        one_player.rect.y = screen_height - 40
        one_player.change_x = 0
        one_player.change_y = 0








    # --- Game logic should go here
    all_sprites_list.update()

 
    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    screen.blit(background, [0, 0])


    pygame.draw.rect(screen, GRAY, [0, screen_height - 20, screen_width, 20])
    for x in range(10, screen_width, 40):
        pygame.draw.rect(screen, YELLOW, [x, screen_height - 10, 20, 3])


    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
