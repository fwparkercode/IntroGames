'''
Ada Collins Final Lab
Kevin's Famous Chili Maze
'''

import pygame

# -- Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Screen dimensions
screen_width = 800
screen_height = 600

# Text

x_offset = 200
# Call this function so the Pygame library can initialize itself
pygame.init()


# Image resources
background_image1 = pygame.image.load("untitled104.jpg")
background_image2 = pygame.image.load("Light-Blue-Square.jpg")
kevin = pygame.image.load("1ytrev.png")
dwight = pygame.image.load("dwightjpg.png")
angela = pygame.image.load("maxresdefault.png")
pam = pygame.image.load("Unknown-1.png")

# Sound resources
background_music = pygame.mixer.Sound("The Office.ogg")
background_music.set_volume(1)
background_music.play(-1)

awesome_sound = pygame.mixer.Sound("Awesome.ogg")
kidding_sound = pygame.mixer.Sound("Kidding.ogg")


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = kevin
        self.chili_bowls = 3
        self.level = 1


        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        enemy_hit_list = pygame.sprite.spritecollide(self, self.enemy, False)
        for enemy in enemy_hit_list:
            self.rect.x = 10
            self.rect.y = 10
            self.chili_bowls -= 1
            kidding_sound.play(0)


        if (pygame.sprite.collide_rect(self, self.pamela)):
            self.rect.x = 10
            self.rect.y = 10
            self.level += 1
            self.chili_bowls = 3
            self.dwight.change_x *= 1.5
            self.angela.change_x *= 1.5
            self.change_x *= 1.5
            awesome_sound.play(0)
        
        if self.chili_bowls == 0:
            end_screen()
            done = True



class Dwight(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = dwight
        self.rect = self.image.get_rect()
        self.rect.y = 320
        self.rect.x = 20
        self.change_x = 2

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right >= 380:
            self.change_x *= -1
        if self.rect.left <= 0:
            self.change_x *= -1



class Angela(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = angela
        self.rect = self.image.get_rect()
        self.rect.y = 320
        self.rect.x = 500
        self.change_x = 2

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right >= screen_width:
            self.change_x *= -1
        if self.rect.left <= 380:
            self.rect.left = 380
            self.change_x *= -1

class Pam(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pam
        self.rect = self.image.get_rect()
        self.rect.y = 150
        self.rect.x = 600


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x




# Create an 800x600 sized screen
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Test')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
enemy_sprite_list = pygame.sprite.Group()
pamela_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 590, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(790, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 300, 150, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(275, 0, 10, 200)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(275, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(375, 200, 10, 250)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(245, 450, 250, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(550, 300, 250, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(550, 125, 10, 175)
wall_list.add(wall)
all_sprite_list.add(wall)

# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
all_sprite_list.add(player)

enemy1 = Dwight(50, 50)
all_sprite_list.add(enemy1)
enemy_sprite_list.add(enemy1)
player.dwight = enemy1

enemy2 = Angela(50, 50)
all_sprite_list.add(enemy2)
enemy_sprite_list.add(enemy2)
player.angela = enemy2

pamela = Pam(50, 50)
all_sprite_list.add(pamela)
pamela_sprite_list.add(pamela)
player.pamela = pamela

player.enemy = enemy_sprite_list

my_font = pygame.font.SysFont('Iowan Old Style', 20, True, False)

clock = pygame.time.Clock()

def intro_screen():
    done = False
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        screen.fill(WHITE)

        my_text = my_font.render("Kevin's Famous Chili Maze:", True, BLACK)
        screen.blit(my_text, [0, 0])
        my_text = my_font.render("Get to Pam without hitting Dwight or Angela!", True, BLACK)
        screen.blit(my_text, [0, 50])
        my_text = my_font.render("Click to start!", True, BLACK)
        screen.blit(my_text, [0, 100])

        pygame.display.flip()

        clock.tick(60)


intro_screen()

def end_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        screen.fill(WHITE)

        my_text = my_font.render("You lost!", True, BLACK)
        screen.blit(my_text, [0, 0])
        my_text = my_font.render("Thank you for playing!", True, BLACK)
        screen.blit(my_text, [0, 50])

        pygame.display.flip()

        clock.tick(60)





done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    all_sprite_list.update()

    screen.blit(background_image2, [0, 0])

    all_sprite_list.draw(screen)

    my_text = my_font.render("Bowls of Chili: " + str(player.chili_bowls), True, BLACK)
    screen.blit(my_text, [50, 50])

    my_text = my_font.render("Level: " + str(player.level), True, BLACK)
    screen.blit(my_text, [590, 50])


    pygame.display.flip()

    clock.tick(60)

pygame.quit()