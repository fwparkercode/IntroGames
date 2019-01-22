"""
The objective of this game is to fill a give percentage of the screen by holding down the mouse key. When they mouse
key is down, the player is active and grows. With the mouse key is lifted, the rectangle is inactive and doesnt move.
If the active boxes collide with an enemy box, the player will die and then game will end. If the enemy box hits an
inactive box, that enemy will bounce off of it and the game will continue. The player will level up when they have
filled the given percentage of the screen. This will lead them to another level in which they have to fill more of the
screen with faster and more abundant enemy boxes in the way.

Ava Ori
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (100, 100, 255)
HOT_PINK = (255, 0, 255)
CYAN = (0, 255, 255)
Yellow = (255, 255, 0)
LIGHT_BLUE = (204, 252, 255)
LIGHT_PURPLE = (200, 196, 250)
MINT = (176, 255, 219)
BABY_PINK = (255, 224, 234)

pygame.init()  # Starts Pygame

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

#sounds
pop = pygame.mixer.Sound("Pop.wav")

ding = pygame.mixer.Sound("ding.wav")

background = pygame.mixer.Sound("background.wav")

#groups
enemy_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
active_block_group = pygame.sprite.Group()
stopped_block_group = pygame.sprite.Group()
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#title
pygame.display.set_caption("Filler Game")

#variables

level = 1
rect_area = 0
percentage = round(((rect_area / 350000) * 100))




class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        #the constructer askes for 3 things
        #called my parent class
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1

        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1


# PLAYER

class Player(Block):
    def update(self):
        #this gets the mouse pos and creates a list out of it
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Enemy(pygame.sprite.Sprite):
    #this is the enemy class
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        self.change_x = 0
        self.change_y = 0

        self.stopped_block_group = None


    def update(self):
    # this makes the enemies bounce off the stopped blocks
        self.rect.x += self.change_x

        hit_list = pygame.sprite.spritecollide(self, self.stopped_block_group, False)
        for hit in hit_list:
            if self.change_x > 0:
                self.rect.right = hit.rect.left
                self.change_x *= -1
            else:
                self.rect.left = hit.rect.right
                self.change_x *= -1

        self.rect.y += self.change_y

        hit_list1 = pygame.sprite.spritecollide(self, self.stopped_block_group, False)
        for hit in hit_list1:
            if self.change_y > 0:
                self.rect.bottom = hit.rect.top
                self.change_y *= -1
            else:
                self.rect.top = hit.rect.bottom
                self.change_y *= -1

        hit_list2 = pygame.sprite.spritecollide(self, self.stopped_block_group, False)
        for hit in hit_list2:
            if self.change_y < 0:
                self.rect.bottom = hit.rect.top
                self.change_y *= -1
            else:
                self.rect.top = hit.rect.bottom
                self.change_y *= -1

        hit_list3 = pygame.sprite.spritecollide(self, self.stopped_block_group, False)
        for hit in hit_list3:
            if self.change_x < 0:
                self.rect.right = hit.rect.left
                self.change_x *= -1
            else:
                self.rect.left = hit.rect.right
                self.change_x *= -1

        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1

        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1




# CREATING ENEMY

for i in range(level * 10):
    # This represents a block
    enemy = Enemy(BLACK, 10, 10)

    # Set a random location for the block
    enemy.rect.x = random.randrange(screen_width)
    enemy.rect.y = random.randrange(screen_height)

    enemy.change_x = random.randrange(-3, 4)
    enemy.change_y = random.randrange(-3, 4)
    enemy.left_boundary = 0
    enemy.top_boundary = 0
    enemy.right_boundary = screen_width
    enemy.bottom_boundary = screen_height

    # Add the block to the list of objects
    block_list.add(enemy)
    all_sprites_list.add(enemy)
    enemy_group.add(enemy)
    enemy.stopped_block_group = stopped_block_group

# this is the block that the player creates and it grows
class ActiveBlock(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(color)
        self.active = True
        self.size = 1
        self.rect = self.image.get_rect()
#this is how the block grows
    def update(self):

        if self.active:

            x = self.rect.centerx
            y = self.rect.centery
            if self.active:
                self.size += 1
            self.image = pygame.Surface([self.size, self.size])
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#this is the intro screen
def cut_screen():
    done = False
    frame = 300
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                done = True
        screen.fill(LIGHT_PURPLE)
        my_text = my_font.render("FILLER GAME", True, BLACK)
        my_text2 = my_font.render("Try to fill " + str(level * 10) + "% of the screen ", True, BLACK)
        my_text3 = my_font.render("while avoiding the black boxes!", True, BLACK)
        my_text4 = my_font.render("Press and hold to grow.", True, BLACK)
        my_text5 = my_font.render("Click anywhere to play...", True, BLACK)
        screen.blit(my_text, [250, 100])
        screen.blit(my_text2, [170, 130])
        screen.blit(my_text3, [150, 160])
        screen.blit(my_text4, [190, 190])
        screen.blit(my_text5, [170, 270])

        pygame.display.flip()
        clock.tick(60)


cut_screen()

# this is the level up screen
def cut_screen2():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(LIGHT_PURPLE)
        my_text = my_font.render("YOU WIN", True, BLACK)
        my_text2 = my_font.render("Try to fill " + str(level * 10) + "% of the screen ", True, BLACK)
        my_text3 = my_font.render("while avoiding the black boxes!", True, BLACK)
        my_text4 = my_font.render("Press and hold to grow.", True, BLACK)
        my_text5 = my_font.render("Click anywhere to start next level...", True, BLACK)
        screen.blit(my_text, [250, 100])
        screen.blit(my_text2, [170, 130])
        screen.blit(my_text3, [150, 160])
        screen.blit(my_text4, [190, 190])
        screen.blit(my_text5, [170, 270])

        pygame.display.flip()
        clock.tick(60)

# this is the YOU LOST screen
def cut_screen3():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
           #if event.type == pygame.MOUSEBUTTONUP:
                 #done = True
        screen.fill(LIGHT_PURPLE)
        my_text = my_font.render("YOU LOST.", True, BLACK)
        screen.blit(my_text, [250, 100])

        pygame.display.flip()
        clock.tick(60)

#more variables
size_y = 10
size_x = 10
size_x_speed = 3
size_y_speed = 3
_level = level


# -------- Main Program Loop -----------
background.play(-1)
background.set_volume(0.8)
while not done:
    x, y = (pygame.mouse.get_pos())
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("DOWN")
            _level = level
            #when you press the button down, you create a growing box
            block = ActiveBlock((random.randrange(70, 256),random.randrange(70, 256),random.randrange(70, 256)) , 1, 1)
            ding.play()
            ding.set_volume(5.2)
            block.active = True
            block.rect.centerx, block.rect.centery = event.pos
            all_sprites_list.add(block)
            active_block_group.add(block)

        if event.type == pygame.MOUSEBUTTONUP:
            #when you lift the mouse the box stops growing. this gets added to a different group
            for block in active_block_group:
                block.active = False
                if block.active == False:
                    stopped_block_group.add(block)
            # this adds the size of the block to rect_area which goes to the percentage
            print("UP")
            if _level == level:
                rect_area += round(block.size ** 2)


    # --- Screen-clearing code goes here
    percentage = round(((rect_area / 350000) * 100))


    # this it what happens when you level up

    if percentage >= (level * 10):
        rect_area = 0
        size = 0
        level += 1
        all_sprites_list.empty()
        enemy_group.empty()
        active_block_group.empty()
        stopped_block_group.empty()
        block_list.empty()

        for i in range(level * 10):
            enemy = Enemy(BLACK, 10, 10)
            enemy.rect.x = random.randrange(screen_width)
            enemy.rect.y = random.randrange(screen_height)
            enemy.change_x = random.randrange(-3, 4)
            enemy.change_y = random.randrange(-3, 4)
            enemy.left_boundary = 0
            enemy.top_boundary = 0
            enemy.right_boundary = screen_width
            enemy.bottom_boundary = screen_height
            block_list.add(enemy)
            all_sprites_list.add(enemy)
            enemy_group.add(enemy)
            enemy.stopped_block_group = stopped_block_group
        cut_screen2()

    all_sprites_list.update()


    #this is how you lose
    for enemy in block_list:
        hit_list = pygame.sprite.spritecollide(enemy, active_block_group, False)
        for block in hit_list:
            if block.active == True:
                block.kill()
                pop.play()
                cut_screen3()
                done = True

    # this keeps the blocks from growing on top of eachother or growing out side the screen
    for block in active_block_group:
        if block.rect.x <= 0 or block.rect.right >= 700:
            block.active = False
            stopped_block_group.add(block)

    for block in active_block_group:
        if block.rect.y <= 0 or block.rect.bottom >= 500:
            block.active = False
            stopped_block_group.add(block)

    for block in active_block_group:
        hit_list_two = pygame.sprite.spritecollide(block, stopped_block_group, False)
        for hit in hit_list_two:
            block.active = False
            stopped_block_group.add(block)



    screen.fill(WHITE)
    all_sprites_list.draw(screen)

    # --- Drawing code should go here

    # THIS DRAWS THE PERCENT THE PLAYER HAS FILLED:

    my_font = pygame.font.SysFont("Calibri", 20, True, False)
    my_text = my_font.render("Percentage Filled : " + str(round(((rect_area / 350000) * 100))) + "%", True, BLACK)
    screen.blit(my_text, [440, 10])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()