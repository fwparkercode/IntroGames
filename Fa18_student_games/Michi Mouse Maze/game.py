"""
Use sprites to collect blocks.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/j

Explanation video: http://youtu.be/4W2AqUetBi4
MICHI PARSA
"""
import pygame
import random
score = 0
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
PINK = (255,51,125)
YELLOW = (241, 196, 15)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
ORANGE = (214, 155, 27)
TURQUOISE =(26, 214, 167)
BROWN = (76, 38, 3)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.image.load("images.png")
        click_sound = pygame.mixer.Sound("Digital Bananas.ogg")
        click_sound.play()



        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.wall_list, False)
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
        block_hit_list = pygame.sprite.spritecollide(self, self.wall_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
good_block_list = pygame.sprite.Group()


# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(250):
    # This represents a block
    block = Block(YELLOW, 10, 7)


    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)


    class Block(pygame.sprite.Sprite):
        """
        This class represents the ball.
        It derives from the "Sprite" class in Pygame.
        """

        def __init__(self, color, width, height):
            """ Constructor. Pass in the color of the block,
            and its size. """

            # Call the parent class (Sprite) constructor
            super().__init__()

            # Create an image of the block, and fill it with a color.
            # This could also be an image loaded from the disk.
            self.image = pygame.Surface([width, height])
            self.image.fill(color)

            # Fetch the rectangle object that has the dimensions of the image
            # image.
            # Update the position of this object by setting the values
            # of rect.x and rect.y
            self.rect = self.image.get_rect()


    # Initialize Pygame
    pygame.init()

    # Set the height and width of the screen
    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])

    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    block_list = pygame.sprite.Group()
    good_block_list = pygame.sprite.Group()
    bad_block_list = pygame.sprite.Group()

    # This is a list of every sprite.
    # All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()

    for i in range(250):
        # This represents a block
        block = Block(YELLOW, 10, 7)
        block_2 = Block(TURQUOISE, 10, 7)

        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(screen_height)

        block_2.rect.x = random.randrange(screen_width)
        block_2.rect.y = random.randrange(screen_height)
        # Add the block to the list of objects
        good_block_list.add(block)
        all_sprites_list.add(block)

        bad_block_list.add(block_2)
        all_sprites_list.add(block_2)

    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)

wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(10, 200,10, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(54, 117,186,10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(243, 120,10, 186)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(254,301,76, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(331, 300,10,67 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(388, 66,10,167 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(413, 232,76,10 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(490,255,10,87 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(509,338,87,10 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(115,57,10,87 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(192,56,87,10 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(496,47,10,100 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(528,146,10,87 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(382,307,4,14 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(602,26,10,123 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(634,163,10,87 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(30,203,95,10 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(114,237,10,34 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(187,361,10,87 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(24,331,10,87 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(130,374,10,87 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(284,250,10,87 )
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(518,171,87,10 )
wall_list.add(wall)
all_sprites_list.add(wall)


# Create a player block
player = Player(50, 50)
all_sprites_list.add(player)
player.wall_list = wall_list

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_font = pygame.font.SysFont("calibri", 30, True, False) #part of text

score = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

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
    # updating
    all_sprites_list.update()

    # Clear the screen
    screen.fill(WHITE)
    print(pygame.mouse.get_pos())
    # Get the current mouse position. This returns the position
    # as a list of two numbers.

    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_block_hit_list = pygame.sprite.spritecollide(player,bad_block_list,True)

    ###############################


    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)

    for block in bad_block_hit_list:
        score-= 1
        print(score)
   # Draw all the spites
    all_sprites_list.draw(screen)

    # text
    my_text = my_font.render("Score: " + str(score),True, YELLOW)

    screen.blit(my_text, [20, 20])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
