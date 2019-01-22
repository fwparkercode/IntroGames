difficulty = 0
game_over_text = 0
while difficulty == 0:
    level = input("Easy or Hard? ")
    if level.lower() == "easy":
        difficulty = 1
    elif level.lower() == "hard":
        difficulty = 2
    elif level.lower() == "rally the hands of history":
        print("1010001010111100100101100000001011110110101001011110001001000010111101011000110110010010100110111001101000110001111011111001011000100110001000000100001000011111101011011001011101010001100101101101111110110100011101100001111000000101001000000000000000001001111011000010011000111001111101011101011101001101100111110101000110110111110101111011101000110000001001")
        game_over_text += 1
    else:
        print("What'd you say? Ju*st type easy or hard. *st type 72616C6C79207468652068616E6473206F6620686973746F7279DA")

import pygame
import random
pygame.init()
# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (200, 255, 100)
LIGHT_G = (0, 100, 0)
GOOD_G = (0, 150, 0)
RED = (255, 0, 0)
HEART_RED = (255, 100, 100)
BLUE = (0, 0, 255)
GRAY = (220, 200, 200)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
COLOR = (random.randrange(256), random.randrange(256), random.randrange(256))
# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# Variables
x = 300
y = 300
water_item = 0
fire_item = 0
light_item = 0
ice_item = 0
sword_item = 0
bow_item = 0
better_bow_item = 0
pac_kill = 0
mega_kill = 0
sonic_kill = 0
luigi_kill = 0
ganon_kill = 0
frame = 0
water_frame = 0
ice_frame = 0
light_frame = 0
fire_frame = 0
music_frame = 0
zelda_frame = 0
sword_stop = 0
bow_stop = 0
better_bow_stop = 0
arrow_stop = 1
arrow_face = 2
rupee_BL = 0
rupee_BR = 0
rupee_TL = 0
rupee_TR = 0
rupee_CL = 0
rupee_CM = 0
rupee_CR = 0
secret_level = 0

item_spawn = random.randrange(10, 20)

# Riddles
word_list = []
riddle_BL = 0
riddle_BR = 0
riddle_TL = 0
riddle_TR = 0
riddle_CL = 0
riddle_CM = 0
riddle_CR = 0

demise = 0

riddle_start = 0
riddle_start_frame = 0

# Objects

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("LinkNormal.png")


        self.rect = self.image.get_rect()
        self.rect.x = x # player movement prep
        self.rect.y = y

        self.change_x = 0 # player movement
        self.change_y = 0
        self.map_x = 1 # map
        self.map_y = 0
        self.health = 3
        self.rupee = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""

        self.change_x += x  # player speed
        self.change_y += y


    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if player.rect.x <= 0: # map boundaries VVV
            if self.map_x == 0:
                player.rect.x = 5
            else:
                self.map_x -= 1
                player.rect.x = screen_width - 5
        if player.rect.x >= screen_width:
            if self.map_x == 3:
                player.rect.x = screen_width - 5
            else:
                self.map_x += 1
                player.rect.x = 5
        if player.rect.y <= 0:
            if self.map_y == 3:
                player.rect.y = 5
            else:
                self.map_y += 1
                player.rect.y = screen_height - 5
        if player.rect.y >= screen_height:
            if self.map_y == 0:
                player.rect.y = screen_height - 5
            else:
                self.map_y -= 1
                player.rect.y = 5 # map boundaries ^^^

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
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
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Lightning(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Light.png")
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height / 2

class Ice(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Ice.png")
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height / 2

class Fire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Fire.png")
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height / 2


class Water(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Water.png")
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height / 2


class Sword(pygame.sprite.Sprite):

    def __init__(self):
        super(Sword, self).__init__()
        self.images = []
        self.images.append(pygame.image.load("SwordRight.png"))
        self.images.append(pygame.image.load("SwordLeft.png"))
        self.images.append(pygame.image.load("SwordDLeft.png"))
        self.images.append(pygame.image.load("SwordDRight.png"))
        self.sword_angle = 0
        self.image = self.images[self.sword_angle]
        self.rect = self.image.get_rect()
        self.counter = 0

    def update(self):
        if self.sword_angle >= len(self.images):
            self.sword_angle = 0
        self.image = self.images[self.sword_angle]

        self.counter += 1

        if self.counter >= 5:
            self.counter = 0
            self.sword_angle += 1

        if self.sword_angle == 0:
            self.rect.x = player.rect.x + 45
            self.rect.y = player.rect.y - 25
            if self.counter == 3:
                self.rect.x = player.rect.x
        if self.sword_angle == 1:
            self.rect.x = player.rect.x - 25
            self.rect.y = player.rect.y - 25
            if self.counter == 3:
                self.rect.y = player.rect.y
        if self.sword_angle == 2:
            self.rect.x = player.rect.x - 20
            self.rect.y = player.rect.y + 35
            if self.counter == 3:
                self.rect.x = player.rect.x
        if self.sword_angle == 3:
            self.rect.x = player.rect.x + 45
            self.rect.y = player.rect.y + 35
            if self.counter == 3:
                self.rect.y = player.rect.y

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if difficulty == 1:
            self.health = 120
        if difficulty == 2:
            self.health = 240

class Pacman(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pacman.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(200, 500)
        self.rect.y = random.randrange(225, 275)
    def update(self):

        self.rect.x = mouse_x
        self.rect.y += random.randrange(-2, 2)
        if self.rect.x <= 0:
            self.rect.x = random.randrange(200, 500)
        if self.rect.x >= screen_width:
            self.rect.x = random.randrange(200, 500)
        if self.rect.y <= 0:
            self.rect.y = random.randrange(225, 275)
        if self.rect.y >= screen_width:
            self.rect.y = random.randrange(225, 275)

class Megaman(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Megaman.gif")
        self.rect = self.image.get_rect()
        self.rect.x = screen_width - 150
        self.rect.y = random.randrange(200, 300)
        self.move = 0
    def update(self):
        if self.move == 0:
            self.rect.y += 5
        else:
            self.rect.y -= 5
        if self.rect.y >= screen_height - 50:
            self.move = 1
        if self.rect.y <= 0:
            self.move = 0
class Sonic(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Sonic.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = random.randrange(175, 275)
    def update(self):
        self.rect.x += 5
        if self.rect.x >= screen_width - 25:
            self.rect.x = 0
            self.rect.y = random.randrange(0, 500)
class Luigi(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Luigi.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, screen_width - 100)
        self.rect.y = random.randrange(100, screen_height - 100)
    def update(self):
        self.rect.x += random.randrange(-5, 5)
        self.rect.y += random.randrange(-5, 5)
        if self.rect.x <= 0:
            self.rect.x = random.randrange(200, 500)
        if self.rect.x >= screen_width:
            self.rect.x = random.randrange(200, 500)
        if self.rect.y <= 0:
            self.rect.y = random.randrange(225, 275)
        if self.rect.y >= screen_width:
            self.rect.y = random.randrange(225, 275)
class Ganon(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Ganon.png")
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 225
        if difficulty == 1:
            self.health = 1000
        if difficulty == 2:
            self.health = 2000
            self.damage = 0
        self.attack_frame = 0
    def update(self):
        if difficulty == 2:
            self.attack_frame += 1
            if self.attack_frame >= 180:
                self.damage = 1
            if self.attack_frame >= 240:
                self.attack_frame = 0



class Bow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if arrow_face == 2:
            self.image = pygame.image.load("BowRight.png")
            self.rect = self.image.get_rect()
    def update(self):
        if arrow_face == 1:
            arrow.rect.x -= 3
        if arrow_face == 2:
            arrow.rect.x += 3
        if arrow_face == 3:
            arrow.rect.y -= 3
        if arrow_face == 4:
            arrow.rect.y += 3
        better_arrow.rect.x += 3
        if arrow.rect.x <= 0:
            arrow.rect.x = bow.rect.x + 15
            arrow.rect.y = bow.rect.y + 10
        if arrow.rect.x >= screen_width:
            arrow.rect.x = bow.rect.x + 15
            arrow.rect.y = bow.rect.y + 10

        if arrow.rect.y <= 0:
            arrow.rect.x = bow.rect.x + 10

            arrow.rect.y = bow.rect.y + 10

        if arrow.rect.y >= screen_height:
            arrow.rect.x = bow.rect.x + 10

            arrow.rect.y = bow.rect.y + 10

        if arrow.rect.x >= screen_width:
            better_arrow.rect.x = bow.rect.x + 15
            better_arrow.rect.y = bow.rect.y + 10


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if arrow_face == 2:
            self.image = pygame.image.load("ArrowRight.png")
            self.rect = self.image.get_rect()
class  Better_Bow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("BetterBow.png")
        self.rect = self.image.get_rect()
    def update(self):
        better_arrow.rect.x += 3
        if better_arrow.rect.x >= screen_width:
            better_arrow.rect.x = better_bow.rect.x + 15
            better_arrow.rect.y = better_bow.rect.y + 10
class Better_Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("BetterArrow.png")
        self.rect = self.image.get_rect()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_number = random.randrange(5)
        if self.image_number == 0:
            self.image = pygame.image.load("RupeeGreen.png")
            self.rect = self.image.get_rect()
        if self.image_number == 1:
            self.image = pygame.image.load("RupeeBlue.png")
            self.rect = self.image.get_rect()
        if self.image_number == 2:
            self.image = pygame.image.load("RupeeOrange.png")
            self.rect = self.image.get_rect()
        if self.image_number == 3:
            self.image = pygame.image.load("RupeeCyan.png")
            self.rect = self.image.get_rect()
        if self.image_number == 4:
            self.image = pygame.image.load("RupeeRed.png")
            self.rect = self.image.get_rect()
class Buffalo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Buffalo.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 650)
        self.rect.y = random.randrange(50, 450)
class Grave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Grave.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 650)
        self.rect.y = random.randrange(50, 450)
class Rocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Rocks.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 650)
        self.rect.y = random.randrange(50, 450)
class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Tree.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 650)
        self.rect.y = random.randrange(50, 450)
class Wheat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Wheat.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 650)
        self.rect.y = random.randrange(50, 450)
class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Box(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
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
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    """This creates all the walls in room 1"""

    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 450, BLUE]
                 ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):
    """This creates all the walls in room 2"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 450, GREEN],
                 [590, 50, 20, 450, GREEN]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):
    """This creates all the walls in room 3"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, MAGENTA],
                 [0, 350, 20, 250, MAGENTA],
                 [780, 0, 20, 250, MAGENTA],
                 [780, 350, 20, 250, MAGENTA],
                 [20, 0, 760, 20, MAGENTA],
                 [20, 580, 760, 20, MAGENTA]]


        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)


# Sounds
sword_slash = pygame.mixer.Sound("Sword.wav")
item_sound = pygame.mixer.Sound("Item.wav")
big_item_sound = pygame.mixer.Sound("BigItem.wav")
zelda_sound = pygame.mixer.Sound("zelda.wav")
riddle_sound = pygame.mixer.Sound("Riddle.wav")
hit_sound = pygame.mixer.Sound("Hit.wav")
light_sound = pygame.mixer.Sound("Light.wav")
wave_sound = pygame.mixer.Sound("Waves.wav")

# Fonts
font = pygame.font.SysFont("Calibri", 10, True, False)
my_font = pygame.font.SysFont("Calibri", 40, True, False)
rupee_font = pygame.font.SysFont("Calibri", 20, True, True)

# Name
pygame.display.set_caption("My Game")

# Class variables
player = Player()

water = Water()
ice = Ice()
lightning = Lightning()
fire = Fire()
sword = Sword()
bow = Bow()
arrow = Arrow()
better_bow = Better_Bow()
better_arrow = Better_Arrow()

enemy = Enemy()

pick = sword

luigi = Luigi()
pacman = Pacman()
megaman = Megaman()
sonic = Sonic()
ganon = Ganon()

buffalo = Buffalo()
grave = Grave()
rocks = Rocks()
tree = Tree()
wheat = Wheat()

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)



# list creation
water_list = pygame.sprite.Group()

fire_list = pygame.sprite.Group()

lightning_list = pygame.sprite.Group()

ice_list = pygame.sprite.Group()

sword_list = pygame.sprite.Group()

bow_list = pygame.sprite.Group()
arrow_list = pygame.sprite.Group()
better_bow_list = pygame.sprite.Group()
better_arrow_list = pygame.sprite.Group()

enemy_list = pygame.sprite.Group()

megaman_list= pygame.sprite.Group()
pacman_list= pygame.sprite.Group()
sonic_list= pygame.sprite.Group()
luigi_list = pygame.sprite.Group()
ganon_list = pygame.sprite.Group()

rupee_list = pygame.sprite.Group()
megaman_rupee = pygame.sprite.Group()
pacman_rupee = pygame.sprite.Group()
sonic_rupee = pygame.sprite.Group()
luigi_rupee = pygame.sprite.Group()
ganon_rupee = pygame.sprite.Group()
plains_BL = pygame.sprite.Group()
plains_BR = pygame.sprite.Group()
plains_TL = pygame.sprite.Group()
plains_TR = pygame.sprite.Group()
cliff_left = pygame.sprite.Group()
cliff_middle = pygame.sprite.Group()
cliff_right = pygame.sprite.Group()

buffalo_list = pygame.sprite.Group()
grave_list = pygame.sprite.Group()

rocks_list = pygame.sprite.Group()

tree_list = pygame.sprite.Group()

wheat_list = pygame.sprite.Group()

# Particles
lightbeam_image = pygame.image.load("Lighbeam.png")
lightbeam = 0

snow_list = []
for i in range(2000):
    speed = random.random() * 5 + 1
    size5 = speed + 23
    x = random.randrange(screen_width)
    y = random.randrange(screen_height)
    snowflake = [x, y, speed, size]
    snow_list.append(snowflake)
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Intro screen
def intro_screen():
    done = False
    frame = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 1200:
            done = True
        screen.fill(RED)
        intro_text = my_font.render("Welcome to Eluryh.", True, WHITE)
        intro_text2 = rupee_font.render("To find the gold, answer with swords, then loot, then trees, then Bill.", True, WHITE)
        intro_text3 = rupee_font.render("To find the silver, answer the bow, then dolphin, then Wilbur.   Find the mouth", True, WHITE)
        intro_text4 = rupee_font.render("Who placed the curse on the Kingdom ruled by Princess Adlez?     of walls.", True, WHITE)

        screen.blit(intro_text, [0, 100])
        screen.blit(intro_text2, [0, 200])
        screen.blit(intro_text3, [0, 300])
        screen.blit(intro_text4, [0, 400])

        pygame.display.flip()
        clock.tick(60)
# game over

def game_over():
    done = False
    frame = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(RED)
        my_text = my_font.render("Game Over", True, WHITE)
        screen.blit(my_text, [100, 100])
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
# Victory
def victory():
    done = False
    frame = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        WINCOLOR = (random.randrange(256), random.randrange(256), random.randrange(256))

        screen.fill(YELLOW)
        my_text = my_font.render("You Win!", True, WINCOLOR)
        if game_over_text >= 1:
            my_text = font.render("'Invariably, you'll find that if the language is any good, your users are going to take it to places where you never thought it would be taken.' - Guido von Rossum", True, BLACK)
        screen.blit(my_text, [0, 0])
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
# inventory
def inventory():
    done = False
    frame = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(RED)
        my_text = my_font.render("Inventory", True, WHITE)
        screen.blit(my_text, [100, 100])
        if light_item >= 1:
            lightning_list.add(lightning)
            lightning_list.draw(screen)
            lightning.rect.x = 0
            lightning.rect.y = 0
        if water_item >= 1:
            water_list.add(water)
            water.rect.x = 0
            water.rect.y = 50
            water_list.draw(screen)
        if ice_item >= 1:
            ice_list.add(ice)
            ice.rect.x = 0
            ice.rect.y = 100
            ice_list.draw(screen)
        if fire_item >= 1:
            fire_list.add(fire)
            fire.rect.x = 0
            fire.rect.y = 130
            fire_list.draw(screen)
        if sword_item >= 1:
            sword_list.add(sword)
            sword.rect.x = 0
            sword.rect.y = screen_height - 50
            sword_list.draw(screen)
        if bow_item >= 1:
            bow_list.add(bow)
            bow.rect.x = 30
            bow.rect.y = screen_height - 50
            bow_list.draw(screen)
        if better_bow_item >= 1:
            better_bow_list.add(better_bow)
            better_bow.rect.x = 50
            better_bow.rect.y = screen_height - 50
            better_bow_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
def control():
    done = False
    frame = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True


        screen.fill(RED)
        controls_text = rupee_font.render("Up, Down, Left, Right to move, Space to use special attacks", True, BLACK)
        controls_text_2 = rupee_font.render("1, 2, 3, 4 to change bow direction, ESC to quit, 8 to play music", True, BLACK)
        controls_text_3 = rupee_font.render("N,L,W,I,F to change outfits, Q for inventory, TAB for intro", True, BLACK)
        controls_text_4 = rupee_font.render("b for bow, s for sword, p for powerful bow", True, BLACK)
        controls_text_5 = rupee_font.render("Type anytime to use the keyboard. Click ENTER or RETURN to delete all", True, BLACK)

        screen.blit(controls_text, [0, 100])
        screen.blit(controls_text_2, [0, 200])
        screen.blit(controls_text_3, [0, 300])
        screen.blit(controls_text_4, [0, 400])
        screen.blit(controls_text_5, [0, 0])


        pygame.display.flip()
        clock.tick(60)


def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()
    main_frame = 0
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])

    # Set the title of the window
    pygame.display.set_caption('Maze Runner')

    # Create the player paddle object
    player = Player()
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done:

        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        # --- Game Logic ---

        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
        if current_room_no == 2:
            main_frame += 1
            if main_frame == 180:
                victory()

        # --- Drawing ---
        screen.fill(BLACK)

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

intro_screen()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
                if bow_item >= 1:
                    arrow_face = 1
                    bow.image = pygame.image.load("BowLeft.png")
                    arrow.image = pygame.image.load("ArrowLeft.png")
                    arrow.rect = arrow.image.get_rect()
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
                if bow_item >= 1:

                    bow.image = pygame.image.load("BowRight.png")
                    arrow.image = pygame.image.load("ArrowRight.png")
                    arrow.rect = arrow.image.get_rect()
                    arrow_face = 2
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
                if bow_item >= 1:

                    arrow_face = 3
                    bow.image = pygame.image.load("BowUp.png")
                    arrow.image = pygame.image.load("ArrowUp.png")
                    arrow.rect = arrow.image.get_rect()
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
                if bow_item >= 1:

                    arrow_face = 4
                    bow.image = pygame.image.load("BowDown.png")
                    arrow.image = pygame.image.load("ArrowDown.png")
                    arrow.rect = arrow.image.get_rect()
            if event.key == pygame.K_3:
                if bow_item >= 1:

                    arrow_face = 1
                    bow.image = pygame.image.load("BowLeft.png")
                    arrow.image = pygame.image.load("ArrowLeft.png")
                    arrow.rect = arrow.image.get_rect()
            if event.key == pygame.K_2:
                if bow_item >= 1:

                    arrow_face = 4
                    bow.image = pygame.image.load("BowDown.png")
                    arrow.image = pygame.image.load("ArrowDown.png")
                    arrow.rect = arrow.image.get_rect()
            if event.key == pygame.K_4:
                if bow_item >= 1:

                    arrow_face = 3
                    bow.image = pygame.image.load("BowUp.png")
                    arrow.image = pygame.image.load("ArrowUp.png")
                    arrow.rect = arrow.image.get_rect()
            if event.key == pygame.K_1:
                if bow_item >= 1:

                    bow.image = pygame.image.load("BowRight.png")
                    arrow.image = pygame.image.load("ArrowRight.png")
                    arrow.rect = arrow.image.get_rect()
                    arrow_face = 2
            elif event.key == pygame.K_l:
                if light_item >= 1:
                    player.image = pygame.image.load("LinkLight.png")
            elif event.key == pygame.K_n:
                player.image = pygame.image.load("LinkNormal.png")
            elif event.key == pygame.K_w:
                if water_item >= 1:
                    player.image = pygame.image.load("LinkWater.png")
            elif event.key == pygame.K_i:
                if ice_item >= 1:
                    player.image = pygame.image.load("LinkIce.png")
            elif event.key == pygame.K_f:
                if fire_item >= 1:
                    player.image = pygame.image.load("LinkFire.png")
            elif event.key == pygame.K_q:
                player.change_x = 0
                player.change_y = 0
                inventory()
            elif event.key == pygame.K_SPACE:
                sword_stop = 1
                bow_stop = 1
                better_bow_stop = 1
            elif event.key == pygame.K_b:
                pick = bow
            elif event.key == pygame.K_s:
                pick = sword
            elif event.key == pygame.K_p:
                pick = better_bow
            elif event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_TAB:
                player.change_x = 0
                player.change_y = 0
                intro_screen()






            # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
            elif event.key == pygame.K_8:
                if zelda_frame == 1:
                    zelda_sound.stop()
                    zelda_frame = 0
            elif event.key == pygame.K_SPACE:
                if pick == sword:
                    sword_stop = 0
                    sword.image = pygame.image.load("SwordRight.png")
                if pick == bow:
                    bow_stop = 0
                if pick == better_bow:
                    better_bow_stop = 0
            elif event.key == pygame.K_9:
                player.change_x = 0
                player.change_y = 0
                control()
            if event.key == pygame.K_q:
                letter = "q"
                word_list.append(letter)

            if event.key == pygame.K_w:
                letter = 'w'

                word_list.append(letter)

            if event.key == pygame.K_e:
                letter = 'e'

                word_list.append(letter)
                if riddle_BL == 1:
                    riddle_BL += 1
                if riddle_BL >= 6:
                    if riddle_TL >= 5:
                        if riddle_BR >= 5:
                            if riddle_TR == 0:
                                riddle_TR += 1
                if riddle_CR == 5:
                    riddle_CR += 1
                if demise == 1:
                    demise += 1
                if demise == 5:
                    demise += 1

            if event.key == pygame.K_r:
                letter = 'r'

                word_list.append(letter)
                if riddle_BL == 2:
                    riddle_BL += 1
                if riddle_BR == 2:
                    riddle_BR += 1
                if riddle_CR >= 8:
                    if riddle_CM == 0:
                        riddle_CM += 1
                if riddle_CR >= 8:
                    if riddle_CM >= 5:
                        if riddle_CL == 0:
                            riddle_CL += 1


            if event.key == pygame.K_t:
                letter = 't'

                word_list.append(letter)
                if riddle_TR == 4:
                    riddle_TR += 1
                if riddle_CR == 4:
                    riddle_CR += 1

            if event.key == pygame.K_y:
                letter = 'y'

                word_list.append(letter)
                if riddle_TR == 2:
                    riddle_TR += 1
                if riddle_CM == 4:
                    riddle_CM += 1

            if event.key == pygame.K_u:
                letter = 'u'

                word_list.append(letter)
                if riddle_CR == 3:
                    riddle_CR += 1

            if event.key == pygame.K_i:
                letter = 'i'

                word_list.append(letter)
                if riddle_BL == 4:
                    riddle_BL += 1
                if riddle_CL == 3:
                    riddle_CL += 1
                if demise == 3:
                    demise += 1

            if event.key == pygame.K_o:
                letter = 'o'

                word_list.append(letter)
                if riddle_BR == 1:
                    riddle_BR += 1
                if riddle_CM == 1:
                    riddle_CM += 1
                if riddle_CL == 1:
                    riddle_CL += 1
                if riddle_CL == 6:
                    riddle_CL += 1


            if event.key == pygame.K_p:
                letter = 'p'

                word_list.append(letter)
                if riddle_TR == 3:
                    riddle_TR += 1
                if bow_item >= 1:
                    if riddle_CR == 0:
                        riddle_CR += 1

            if event.key == pygame.K_a:
                letter = 'a'

                word_list.append(letter)
                if riddle_TL == 2:
                    riddle_TL += 1
                if riddle_TL == 4:
                    riddle_TL += 1
                if riddle_BR == 3:
                    riddle_BR += 1
                if riddle_CR == 1:
                    riddle_CR += 1
                if riddle_CR == 7:
                    riddle_CR += 1
            if event.key == pygame.K_s:
                letter = 's'

                word_list.append(letter)
                if riddle_CL == 5:
                    riddle_CL += 1
                if demise == 4:
                    demise += 1

            if event.key == pygame.K_d:
                letter = 'd'

                word_list.append(letter)
                if demise == 0:
                    demise += 1

            if event.key == pygame.K_f:
                letter = 'f'

                word_list.append(letter)

            if event.key == pygame.K_g:
                letter = 'g'

                word_list.append(letter)
                if riddle_TR == 1:
                    riddle_TR += 1

            if event.key == pygame.K_h:
                letter = 'h'

                word_list.append(letter)

            if event.key == pygame.K_j:
                letter = 'j'

                word_list.append(letter)

            if event.key == pygame.K_k:
                letter = 'k'

                word_list.append(letter)
                if riddle_CM == 3:
                    riddle_CM += 1

            if event.key == pygame.K_l:
                letter = 'l'
                if riddle_BL >= 6:
                    if riddle_TL == 0:
                        riddle_TL += 1
                if riddle_TL == 1:
                    riddle_TL += 1
                if riddle_TL >= 5:
                    if riddle_BL >= 6:
                        if riddle_BR == 0:
                            riddle_BR += 1
                if riddle_CR == 2:
                    riddle_CR += 1

                word_list.append(letter)
                if riddle_BL == 3:
                    riddle_BL += 1

            if event.key == pygame.K_z:
                letter = 'z'

                word_list.append(letter)

            if event.key == pygame.K_x:
                letter = 'x'

                word_list.append(letter)
                if riddle_BR == 4:
                    riddle_BR += 1

            if event.key == pygame.K_c:
                letter = 'c'

                word_list.append(letter)
                if riddle_CM == 2:
                    riddle_CM += 1

            if event.key == pygame.K_v:
                letter = 'v'

                word_list.append(letter)

            if event.key == pygame.K_b:
                letter = 'b'

                word_list.append(letter)
                if riddle_CL == 2:
                    riddle_CL += 1

            if event.key == pygame.K_n:
                letter = 'n'

                word_list.append(letter)
                if riddle_BL == 5:
                    riddle_BL += 1
                if riddle_CR == 6:
                    riddle_CR += 1
                if riddle_CL == 4:
                    riddle_CL += 1
                if riddle_CL == 7:
                    riddle_CL += 1

            if event.key == pygame.K_m:
                letter = 'm'
                word_list.append(letter)
                if sword_item >= 1:
                    if riddle_BL == 0:
                        riddle_BL += 1
                if riddle_TL == 3:
                    riddle_TL += 1
                if demise == 2:
                    demise += 1
            if event.key == pygame.K_SPACE:
                if difficulty == 2:
                    ganon.damage = 0
            if event.key == pygame.K_RETURN:
                word_list.clear()
                if demise <= 6:
                    demise = 0
                if riddle_BL <= 6:
                    riddle_BL = 0
                if riddle_BR <= 5:
                    riddle_BR = 0
                if riddle_CL <= 8:
                    riddle_CL = 0
                if riddle_CM <= 5:
                    riddle_CM = 0
                if riddle_CR <= 3:
                    riddle_CR = 0
                if riddle_TL <= 5:
                    riddle_TL = 0
                if riddle_TR <= 5:
                    riddle_TR = 0
    # time


    frame += 1

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # game over states
    if water_item <= 0:
        if player.map_x == 3:
            if player.map_y == 0:
                water_frame += 1
                if water_frame == 30:
                    player.health -= 1
                if water_frame == 60:
                    player.health -= 1
                if water_frame == 90:
                    player.health -= 1
                if player.health == 0:
                    game_over()
    if ice_item <= 0:
        if player.map_x == 1:
            if player.map_y == 3:
                ice_frame += 1
                if ice_frame == 30:
                    player.health -= 1
                if ice_frame == 60:
                    player.health -= 1
                if ice_frame == 90:
                    player.health -= 1
                if player.health == 0:
                    game_over()
        if player.map_x == 0:
            if player.map_y == 3:
                ice_frame += 1
                if ice_frame == 30:
                    player.health -= 1
                if ice_frame == 60:
                    player.health -= 1
                if ice_frame == 90:
                    player.health -= 1
                if player.health == 0:
                    game_over()
    if light_item == 0:
        if player.map_x == 0:
            if player.map_y == 0:
                light_frame += 1
                if light_frame == 30:
                    player.health -= 1
                if light_frame == 60:
                    player.health -= 1
                if light_frame == 90:
                    player.health -= 1
                if player.health == 0:
                    game_over()
        if player.map_x == 0:
            if player.map_y == 1:
                light_frame += 1
                if light_frame == 30:
                    player.health -= 1
                if light_frame == 60:
                    player.health -= 1
                if light_frame == 90:
                    player.health -= 1
                if player.health == 0:
                    game_over()

    if fire_item <= 0:
        if player.map_x == 3:
            if player.map_y == 3:
                fire_frame += 1
                if fire_frame == 30:
                    player.health -= 1
                if fire_frame == 60:
                    player.health -= 1
                if fire_frame == 90:
                    player.health -= 1
                if player.health == 0:
                    game_over()
                    
        if player.map_x == 3:
            if player.map_y == 2:
                fire_frame += 1
                if fire_frame == 30:
                    player.health -= 1
                if fire_frame == 60:
                    player.health -= 1
                if fire_frame == 90:
                    player.health -= 1
                if player.health == 0:
                    game_over()
        if player.map_x == 2:
            if player.map_y == 3:
                fire_frame += 1
                if fire_frame == 30:
                    player.health -= 1
                if fire_frame == 60:
                    player.health -= 1
                if fire_frame == 90:
                    player.health -= 1
                if player.health == 0:
                    game_over()

    # game over states ^^
    # Music

    if zelda_frame == 0:
        zelda_sound.play()
        zelda_frame = 1

    # Victory
    if ganon.health <= 0:
        victory()

    # --- Screen-clearing code goes here
    screen.fill(WHITE)
    # --- Drawing code should go here

    # Map drawing
    if player.map_x == 0:
        if player.map_y == 0:
            light_sound.play()
            pygame.draw.rect(screen, LIGHT_G, [0, 0, screen_width, screen_height])
    if player.map_x == 0:
        if player.map_y == 1:
            light_sound.play()
            pygame.draw.rect(screen, LIGHT_G, [0, 0, screen_width, screen_height])

    if player.map_x == 0:
        if player.map_y == 2:
            light_sound.stop()
            pygame.draw.rect(screen, GRAY, [0, 0, screen_width, screen_height])
            if len(grave_list) < item_spawn:

                for j in range(item_spawn):
                    grave = Grave()
                    grave_list.add(grave)
            grave_list.draw(screen)
            pygame.draw.rect(screen, LIGHT_G, [0, screen_height - 10, screen_width, 10])
            pygame.draw.rect(screen, CYAN, [0, 0, screen_width, 10])
    if player.map_x == 0:
        if player.map_y == 3:
            pygame.draw.rect(screen, CYAN, [0, 0, screen_width, screen_height])
    if player.map_x == 1:
        if player.map_y == 0:
            light_sound.stop()
            pygame.draw.rect(screen, GREEN, [0, 0, screen_width, screen_height])
            pygame.draw.rect(screen, LIGHT_G, [0, 0, 10, screen_height])

    if player.map_x == 2:
        if player.map_y == 0:
            wave_sound.stop()
            pygame.draw.rect(screen, GREEN, [0, 0, screen_width, screen_height])
            if len(tree_list) < item_spawn:
                for l in range(item_spawn):
                    tree = Tree()
                    tree_list.add(tree)
            tree_list.draw(screen)
            pygame.draw.rect(screen, BLUE, [screen_width - 10, 0, screen_width, screen_height])

    if player.map_x == 3:
        if player.map_y == 0:

            pygame.draw.rect(screen, BLUE, [0, 0, screen_width, screen_height])
    if player.map_x == 1:
        if player.map_y == 1:
            light_sound.stop()
            pygame.draw.rect(screen, GREEN, [0, 0, screen_width, screen_height])
            if len(buffalo_list) < item_spawn:
                for i in range(item_spawn):
                    buffalo = Buffalo()
                    buffalo_list.add(buffalo)
            buffalo_list.draw(screen)
            pygame.draw.rect(screen, LIGHT_G, [0, 0, 10, screen_height])
            pygame.draw.rect(screen, GRAY, [0, 0, screen_width, 10])

    if player.map_x == 2:
        if player.map_y == 1:
            pygame.draw.rect(screen, GREEN, [0, 0, screen_width, screen_height])
            if len(wheat_list) < item_spawn:

                for m in range(item_spawn):
                    wheat = Wheat()
                    wheat_list.add(wheat)
            wheat_list.draw(screen)
            pygame.draw.rect(screen, YELLOW, [screen_width - 10, 0, screen_width, screen_height])
            pygame.draw.rect(screen, GRAY, [0, 0, screen_width, 10])
    if player.map_x == 3:
        if player.map_y == 1:
            wave_sound.stop()
            pygame.draw.rect(screen, YELLOW, [0, 0, screen_width, screen_height])
            pygame.draw.rect(screen, RED, [0, 0, screen_width, 10])
            pygame.draw.rect(screen, BLUE, [0, screen_height - 10, screen_width, 10])
    if player.map_x == 1:
        if player.map_y == 2:
            pygame.draw.rect(screen, GRAY, [0, 0, screen_width, screen_height])
            if len(rocks_list) < item_spawn:

                for k in range(item_spawn):
                    rocks = Rocks()
                    rocks_list.add(rocks)
            rocks_list.draw(screen)
            pygame.draw.rect(screen, CYAN, [0, 0, screen_width, 10])

    if player.map_x == 2:
        if player.map_y == 2:
            pygame.draw.rect(screen, GRAY, [0, 0, screen_width, screen_height])
            pygame.draw.rect(screen, RED, [0, 0, screen_width, 10])
            pygame.draw.rect(screen, RED, [screen_width - 10, 0, screen_width, screen_height])
    if player.map_x == 3:
        if player.map_y == 2:
            pygame.draw.rect(screen, RED, [0, 0, screen_width, screen_height])
    if player.map_x == 1:
        if player.map_y == 3:
            pygame.draw.rect(screen, CYAN, [0, 0, screen_width, screen_height])
    if player.map_x == 2:
        if player.map_y == 3:
            pygame.draw.rect(screen, RED, [0, 0, screen_width, screen_height])
    if player.map_x == 3:
        if player.map_y == 3:
            pygame.draw.rect(screen, RED, [0, 0, screen_width, screen_height])

    # Item drawing
    if player.map_x == 3:
        if player.map_y == 1:
            if light_item <= 0:
                if mega_kill >= 1:
                    lightning_list.add(lightning)
                    lightning_list.draw(screen)
    if player.map_x == 0:
        if player.map_y == 1:
            if water_item <= 0:
                if pac_kill >= 1:
                    water_list.add(water)
                    water_list.draw(screen)
    if player.map_x == 3:
        if player.map_y == 0:
            if ice_item <= 1:
                if sonic_kill >= 1:
                    ice_list.add(ice)
                    ice_list.draw(screen)
    if player.map_x == 0:
        if player.map_y == 3:
            if fire_item <= 1:
                if luigi_kill >= 1:
                    fire_list.add(fire)
                    fire_list.draw(screen)

    # Boss drawing
    if player.map_x == 3:
        if player.map_y == 3:
            if ganon_kill < 1:
                if ganon.health <= 2000 and ganon.health >= 1775:
                    ganon.image = pygame.image.load("Megaman.gif")
                    ganon_list.add(ganon)
                    ganon_list.draw(screen)
                if ganon.health <= 1774 and ganon.health >= 1500:
                    ganon.image = pygame.image.load("Pacman.png")
                    ganon_list.add(ganon)
                    ganon_list.draw(screen)
                if ganon.health <= 1499 and ganon.health >= 1225:
                    ganon.image = pygame.image.load("Sonic.png")
                    ganon_list.add(ganon)
                    ganon_list.draw(screen)
                if ganon.health <= 1224 and ganon.health >= 1000:
                    ganon.image = pygame.image.load("Luigi.png")
                    ganon_list.add(ganon)
                    ganon_list.draw(screen)
                if ganon.health <= 999:
                    ganon.image = pygame.image.load("Ganon.png")
                    ganon_list.add(ganon)
                    ganon_list.draw(screen)

    if player.map_x == 3:
        if player.map_y == 1:
            if mega_kill < 1:
                megaman_list.add(megaman)
                megaman_list.draw(screen)
                megaman.update()
    if player.map_x == 0:
        if player.map_y == 1:
            if pac_kill < 1:
                pacman_list.add(pacman)
                pacman_list.draw(screen)
                pacman.update()
    if player.map_x == 3:
        if player.map_y == 0:
            if sonic_kill < 1:
                sonic_list.add(sonic)
                sonic_list.draw(screen)
                sonic.update()
    if player.map_x == 0:
        if player.map_y == 3:
            if luigi_kill < 1:
                luigi_list.add(luigi)
                luigi_list.draw(screen)
                luigi.update()



    # Rupee drawing

    if player.map_x == 1:
        if player.map_y == 0:
            if sword_item >= 1:
                if riddle_BL == 6:
                    if word_list[5] == 'n':
                         riddle_sound.play()
                         for i in range(15):
                            rupee = Coin()
                            rupee.rect.x = random.randrange(25, 675)
                            rupee.rect.y = random.randrange(25, 475)
                            rupee_list.add(rupee)
                            plains_BL.add(rupee)
                            riddle_BL += 1
                            word_list.clear()
                    else:
                        word_list.clear()
                        riddle_BL = 0

                plains_BL.draw(screen)
    if player.map_x == 2:
        if player.map_y == 0:
            if riddle_BR == 5:
                if word_list[4] == 'x':
                    riddle_sound.play()

                    for i in range(15):
                        rupee = Coin()
                        rupee.rect.x = random.randrange(25, 675)
                        rupee.rect.y = random.randrange(25, 475)
                        rupee_list.add(rupee)
                        plains_BR.add(rupee)
                        riddle_BR += 1
                        word_list.clear()
                else:
                    riddle_BR = 0
                    word_list.clear()
            plains_BR.draw(screen)
    if player.map_x == 2:
        if player.map_y == 1:
            if riddle_TR == 5:
                if word_list[4] == 't':
                    riddle_sound.play()

                    for i in range(15):
                        rupee = Coin()
                        rupee.rect.x = random.randrange(25, 675)
                        rupee.rect.y = random.randrange(25, 475)
                        rupee_list.add(rupee)
                        plains_TR.add(rupee)
                        riddle_TR += 1
                        word_list.clear()
                else:
                    word_list.clear()
                    riddle_TR = 0

            plains_TR.draw(screen)
    if player.map_x == 1:
        if player.map_y == 1:
            if riddle_TL == 5:
                if word_list[4] == 'a':
                    riddle_sound.play()

                    for i in range(15):
                        rupee = Coin()
                        rupee.rect.x = random.randrange(100, 600)
                        rupee.rect.y = random.randrange(25, 475)
                        rupee_list.add(rupee)
                        plains_TL.add(rupee)
                        riddle_TL += 1
                        word_list.clear()
                else:
                    word_list.clear()
                    riddle_TL = 0

            plains_TL.draw(screen)
    if player.map_x == 1:
        if player.map_y == 2:
            if riddle_CM == 5:
                if word_list[4] == 'y':
                    riddle_sound.play()

                    for i in range(15):
                        rupee = Coin()
                        rupee.rect.x = random.randrange(25, 675)
                        rupee.rect.y = random.randrange(25, 475)
                        rupee_list.add(rupee)
                        cliff_middle.add(rupee)
                        riddle_CM += 1
                        word_list.clear()
                else:
                    word_list.clear()
                    riddle_CM = 0

            cliff_middle.draw(screen)

    if player.map_x == 0:
        if player.map_y == 2:
            if riddle_CL == 8:
                if word_list[7] == 'n':
                    riddle_sound.play()

                    for i in range(10):
                        rupee = Coin()
                        rupee.rect.x = random.randrange(25, 675)
                        rupee.rect.y = random.randrange(25, 475)
                        rupee_list.add(rupee)
                        cliff_left.add(rupee)
                        riddle_CL += 1
                        word_list.clear()
                else:
                    word_list.clear()
                    riddle_CL = 0

            cliff_left.draw(screen)
    if player.map_x == 2:
        if player.map_y == 2:
            if bow_item >= 1:
                if riddle_CR == 8:
                    if word_list[7] == 'a':
                        riddle_sound.play()

                        for i in range(15):
                            rupee = Coin()
                            rupee.rect.x = random.randrange(25, 675)
                            rupee.rect.y = random.randrange(25, 475)
                            rupee_list.add(rupee)
                            cliff_right.add(rupee)
                            riddle_CR += 1
                            word_list.clear()
                    else:
                        word_list.clear()
                        riddle_CR = 0

                cliff_right.draw(screen)


    # Sword drawing
    if player.map_x == 1:
        if player.map_y == 0:
            if sword_item == 0:
                sword_list.add(sword)
                sword.rect.x = 100
                sword.rect.y = 100
                sword_list.draw(screen)
    else:
        sword_list.remove(sword)
    if sword_item >= 1:
        if pick == sword:
            sword_list.add(sword)
            sword_list.draw(screen)
        if sword_stop == 0:
            sword.rect.x = player.rect.x + 40
            sword.rect.y = player.rect.y

    # Bow drawing
    if player.map_x == 2:
        if player.map_y == 2:
            if bow_item == 0:
                bow_list.add(bow)
                bow.rect.x = 200
                bow.rect.y = 200
                bow_list.draw(screen)
    if bow_item >= 1:
        if pick == bow:
            bow_list.add(bow)
            bow_list.draw(screen)
            if arrow_face == 1:
                bow.rect.x = player.rect.x - 20
                bow.rect.y = player.rect.y
            if arrow_face == 2:
                bow.rect.x = player.rect.x + 40
                bow.rect.y = player.rect.y
            if arrow_face == 3:
                bow.rect.x = player.rect.x
                bow.rect.y = player.rect.y - 20
            if arrow_face == 4:
                bow.rect.x = player.rect.x
                bow.rect.y = player.rect.y + 40
        if bow_stop == 0:
            if arrow_face == 1:
                arrow.rect.x = player.rect.x - 20
                arrow.rect.y = player.rect.y + 10
            if arrow_face == 2:
                arrow.rect.x = player.rect.x + 40
                arrow.rect.y = player.rect.y + 10
            if arrow_face == 3:
                arrow.rect.x = player.rect.x + 10
                arrow.rect.y = player.rect.y - 20
            if arrow_face == 4:
                arrow.rect.x = player.rect.x + 5
                arrow.rect.y = player.rect.y + 40
            if pick == bow:
                arrow_list.add(arrow)
                arrow_list.draw(screen)
            else:
                arrow_list.remove(arrow)
    if player.rupee >= 100:
        if player.map_x == 0:
            if player.map_y == 2:

                if better_bow_item == 0:
                    better_bow.rect.x = 200
                    better_bow.rect.y = 200
                    better_bow_list.add(better_bow)
                    better_bow_list.draw(screen)
        if better_bow_item >= 1:
            if pick == better_bow:
                better_bow_list.add(better_bow)
                better_bow_list.draw(screen)

                better_bow.rect.x = player.rect.x + 40
                better_bow.rect.y = player.rect.y + 10

            if better_bow_stop == 0:
                better_arrow.rect.x = player.rect.x + 40
                better_arrow.rect.y = player.rect.y + 15
                if pick == better_bow:
                    better_arrow_list.add(arrow)
                    better_arrow_list.draw(screen)


        # Special moves
    if sword_stop == 1:
        if sword_item >= 1:
            if pick == sword:
                sword.update()
                sword_slash.set_volume(.04)
                sword_slash.play()

    if bow_stop == 1:
        if bow_item >= 1:
            if pick == bow:
                arrow_list.add(arrow)
                arrow_list.draw(screen)
                bow.update()
                sword_slash.play()
    if better_bow_stop == 1:
        if better_bow_item >= 1:
            if pick == better_bow:
                better_arrow_list.add(better_arrow)
                better_arrow_list.draw(screen)
                better_bow.update()
                sword_slash.play()






    # player drawing
    all_sprites_list.draw(screen)
    all_sprites_list.update()

        # Item collection
    lightning_hit_list = pygame.sprite.spritecollide(player, lightning_list, True)
    for light in lightning_hit_list:
        light_item += 1
        item_sound.play()

        player.image = pygame.image.load("LinkLight.png")
    ice_hit_list = pygame.sprite.spritecollide(player, ice_list, True)
    for ice in ice_hit_list:
        ice_item += 1
        item_sound.play()
        player.image = pygame.image.load("LinkIce.png")

    water_hit_list = pygame.sprite.spritecollide(player, water_list, True)
    for water in water_hit_list:
        water_item += 1
        item_sound.play()

        player.image = pygame.image.load("LinkWater.png")
    fire_hit_list = pygame.sprite.spritecollide(player, fire_list, True)
    for fire in fire_hit_list:
        fire_item += 1
        item_sound.play()

        player.image = pygame.image.load("LinkFire.png")

    # Sword collection
    if player.map_x == 1:
        if player.map_y == 0:

            sword_hit_list = pygame.sprite.spritecollide(player, sword_list, True)
    for sword in sword_hit_list:
        pick = sword
        if sword_item <= 2:
            big_item_sound.play()

            sword_item += 1
            sword.rect.x = player.rect.x + 40
            sword.rect.y = player.rect.y

    # Sword use

    megaman_kill_list = pygame.sprite.spritecollide(sword, megaman_list, True)
    for kill in megaman_kill_list:
        if megaman.health <= 0:
            mega_kill += 1
        else:
            megaman.health -= 1
    pacman_kill_list = pygame.sprite.spritecollide(sword, pacman_list, True)
    for kill in pacman_kill_list:

        if pacman.health <= 0:
            pac_kill += 1
        else:
            pacman.health -= 1
            pacman.rect.y += random.randrange(-35, 35)

    sonic_kill_list = pygame.sprite.spritecollide(sword, sonic_list, True)
    for kill in sonic_kill_list:

        if sonic.health <= 0:
            sonic_kill += 1
        else:
            sonic.health -= 1
    luigi_kill_list = pygame.sprite.spritecollide(sword, luigi_list, True)
    for kill in luigi_kill_list:
        if luigi.health <= 0:
            luigi_kill += 1
        else:
            luigi.health -= 1
            luigi.rect.y += random.randrange(-75, 75)
    ganon_kill_list = pygame.sprite.spritecollide(sword, ganon_list, True)
    for kill in ganon_kill_list:

        if ganon.health == 0:
            ganon_kill += 1
        else:
            ganon.health -= 1
    # Bow collection

    bow_hit_list = pygame.sprite.spritecollide(player, bow_list, True)
    for bow in bow_hit_list:
        pick = bow
        if bow_item <= 2:
            big_item_sound.play()

            bow_item += 1
            bow.rect.x = player.rect.x + 40
            bow.rect.y = player.rect.y
    better_bow_hit_list = pygame.sprite.spritecollide(player, better_bow_list, True)
    for better_bow in better_bow_hit_list:
        pick = better_bow
        if better_bow_item <= 1:
            better_bow_item += 1
            better_bow.rect.x = player.rect.x + 40
            better_bow.rect.y = player.rect.y
            better_arrow.rect.x = player.rect.x + 40
            better_arrow.rect.y = player.rect.y + 10
    # Bow use
    megaarrow_kill_list = pygame.sprite.spritecollide(arrow, megaman_list, True)
    for kill in megaarrow_kill_list:
        if megaman.health == 0:
            mega_kill += 1
        else:
            megaman.health -= 2
    pacarrow_kill_list = pygame.sprite.spritecollide(arrow, pacman_list, True)
    for kill in pacarrow_kill_list:
        if pacman.health == 0:
            pac_kill += 1
        else:
            pacman.health -= 2
    sonicarrow_kill_list = pygame.sprite.spritecollide(arrow, sonic_list, True)
    for kill in sonicarrow_kill_list:
        if sonic.health <= 0:
            sonic_kill += 1
        else:
            sonic.health -= 2
    luigiarrow_kill_list = pygame.sprite.spritecollide(arrow, luigi_list, True)
    for kill in luigiarrow_kill_list:
        if luigi.health <= 0:
            luigi_kill += 1
        else:
            luigi.health -= 2

    ganonarrow_kill_list = pygame.sprite.spritecollide(arrow, ganon_list, True)
    for kill in ganonarrow_kill_list:
        if ganon.health <= 0:
            ganon_kill += 1
        else:
            ganon.health -= 2

    bettermegaarrow_kill_list = pygame.sprite.spritecollide(better_arrow, megaman_list, True)
    for kill in bettermegaarrow_kill_list:
        if megaman.health <= 0:
            mega_kill += 1
        else:
            megaman.health -= 120
    betterpacarrow_kill_list = pygame.sprite.spritecollide(better_arrow, pacman_list, True)
    for kill in betterpacarrow_kill_list:
        if pacman.health <= 0:
            pac_kill += 1
        else:
            pacman.health -= 120
    bettersonicarrow_kill_list = pygame.sprite.spritecollide(better_arrow, sonic_list, True)
    for kill in bettersonicarrow_kill_list:
        if sonic.health <= 0:
            sonic_kill += 1
        else:
            sonic.health -= 120
    betterluigiarrow_kill_list = pygame.sprite.spritecollide(better_arrow, luigi_list, True)
    for kill in betterluigiarrow_kill_list:
        if luigi.health <= 0:
            luigi_kill += 1
        else:
            luigi.health -= 120
    betterganonarrow_kill_list = pygame.sprite.spritecollide(better_arrow, ganon_list, True)
    for kill in betterganonarrow_kill_list:
        if ganon.health <= 0:
            ganon_kill += 1
        else:
            ganon.health -= 120

    # Victory



    # Rupees
    rupee_kill_list = pygame.sprite.spritecollide(player, rupee_list, True)
    for rupee in rupee_kill_list:
        player.rupee += 1


    pygame.draw.ellipse(screen, GOOD_G, (screen_width - 130, 20, 15, 25))
    pygame.draw.ellipse(screen, BLACK, (screen_width - 130, 20, 15, 25), 3)
    my_text = rupee_font.render("Rupee x" + str(player.rupee), False, GOOD_G)
    screen.blit(my_text, [screen_width - 110 , 20])

    # Hearts
    if player.health == 3:
        pygame.draw.rect(screen, HEART_RED, (screen_width - 50, 0, 10, 10))
        pygame.draw.rect(screen, BLACK, (screen_width - 50, 0, 10, 10), 3)

        pygame.draw.rect(screen, HEART_RED, (screen_width - 30, 0, 10, 10))
        pygame.draw.rect(screen, BLACK, (screen_width - 30, 0, 10, 10), 3)

        pygame.draw.rect(screen, HEART_RED, (screen_width - 10, 0, 10, 10))
        pygame.draw.rect(screen, BLACK, (screen_width - 10, 0, 10, 10), 3)

    if player.health == 2:
        pygame.draw.rect(screen, HEART_RED, (screen_width - 30, 0, 10, 10))
        pygame.draw.rect(screen, BLACK, (screen_width - 30, 0, 10, 10), 3)

        pygame.draw.rect(screen, HEART_RED, (screen_width - 10, 0, 10, 10))
        pygame.draw.rect(screen, BLACK, (screen_width - 10, 0, 10, 10), 3)

    if player.health == 1:
        pygame.draw.rect(screen, HEART_RED, (screen_width - 10, 0, 10, 10))
        pygame.draw.rect(screen, BLACK, (screen_width - 10, 0, 10, 10), 3)

    # Timer
    timer = rupee_font.render("Time: " + str(frame/60), False, BLACK)
    screen.blit(timer, [0, 0])

    # Control alert
    control_text = my_font.render("Press 9 for controls", False, BLACK)
    if frame <= 300:
        screen.blit(control_text, [0, 400])

    # Riddle start

    riddle_start_text = rupee_font.render("Welcome to the Riddles", True, BLACK)

    if riddle_start == 1:
        riddle_start_frame += 1
        if riddle_start_frame <= 300:
            screen.blit(riddle_start_text, [0, 500])

    # Map riddles
    BL_text = rupee_font.render("Arthur pulls the sword while ___ casts the spell.", False, BLACK)
    BR_text = rupee_font.render("I am the ___ I speak for the trees ", False, BLACK)
    TL_text = rupee_font.render("The Loot ___ out of Tilted charges off the flying bus", False, BLACK)
    TR_text = rupee_font.render("The desert country of ___, ruled by Ant and Cleo, recorded by Bill", False, BLACK)
    CL_text = rupee_font.render("Wilbur and Will and Fritz ___, bowler hat and 'Danger' and Kuala", False, BLACK)
    CM_text = rupee_font.render("___ beats the Dolph(in) Drago(n)", False, BLACK)
    CR_text = rupee_font.render("Pit, the bow-wielding angel who was given flight by ____", False, BLACK)

    if demise == 6:
        if word_list[5] == 'e':
            riddle_sound.play()
            word_list.clear()
            demise += 1
            riddle_start = 1
        else:
            word_list.clear()
            demise = 0
    if demise >= 6:
        if sword_item >= 1:
            if player.map_x == 1:
                if player.map_y == 0:
                        screen.blit(BL_text, [100, 100])
            if player.map_x == 1:
                if player.map_y == 1:
                    screen.blit(TL_text, [100, 100])
            if player.map_x == 2:
                if player.map_y == 0:
                    screen.blit(BR_text, [100, 100])
            if player.map_x == 2:
                if player.map_y == 1:
                    screen.blit(TR_text, [100, 100])

        if bow_item >= 1:
            if player.map_x == 2:
                if player.map_y == 2:
                        screen.blit(CR_text, [100, 100])
            if player.map_x == 0:
                if player.map_y == 2:
                    screen.blit(CL_text, [100, 100])
            if player.map_x == 1:
                if player.map_y == 2:
                    screen.blit(CM_text, [100, 100])

    # my_text5 = my_font.render(str(riddle_BL) +str(riddle_BR)+str(riddle_TL)+str(riddle_TR)+str(riddle_CL)+str(riddle_CM)+str(riddle_CR), False, BLACK)
    my_text144 = my_font.render(str(word_list) + str(level), False, BLACK)
    screen.blit(my_text144, [0, 30])

    # Rain
    if player.map_y == 3:
        if player.map_x == 0 or player.map_x == 1:
            for raindrop in snow_list:
                snowflake[1] += snowflake[2]
                pygame.draw.ellipse(screen, WHITE, [raindrop[0], raindrop[1], 10, 10])
                if snowflake[1] > screen_height:
                    snowflake[1] = -5
                    snowflake[0] = random.randrange(screen_width)
                    WHITE = (random.randrange(200, 255), random.randrange(200, 255), random.randrange(200, 255))
    if player.map_x == 0:
        if player.map_y == 0 or player.map_y == 1:
            lightbeam = random.randrange(1, 10)
            if lightbeam == 1:
                for lightbeam in range(5):
                    screen.blit(lightbeam_image, [random.randrange(500), 0])
                    for lightbeam in range(50):
                        pygame.draw.line(screen, GREEN, [random.randrange(0, 700), 0], [random.randrange(0, 700,), 500])

    # Secret level
    if player.map_x == 3:
        if player.map_y == 2:
            if fire_item >= 1:
                secret_level += 5
                pygame.draw.rect(screen, BLACK, (0, 0, secret_level, secret_level))
                if secret_level >= 700:
                    end_text = rupee_font.render("Let your dreams take flight", True, WHITE)
                    screen.blit(end_text, [150, 150])
                if secret_level == 1400:
                    main()



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()




