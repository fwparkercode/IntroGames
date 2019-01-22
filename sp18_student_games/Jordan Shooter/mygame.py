"""
Use sprites to collect blocks.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random


# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0, 128, 0)

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height, speed=3, direction=random.choice([-1, 1])):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.speed = speed
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height
        self.direction = direction

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
speed_x = 0
speed_y = 0


# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
#gas_list = pygame.sprite.Group()


# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

#Sound
background_sound = pygame.mixer.Sound("space.ogg")
background_sound.set_volume(0.6)
background_sound.play(-1)

for i in range(25):
    # This represents a block
    block = Block(WHITE, 20, 15, speed=random.randrange(1, 4))
    block.image = pygame.image.load("asteroid.png").convert()
    block.image.set_colorkey(WHITE)
    block.rect = block.image.get_rect()
    block.rect.x = random.randrange (screen_width)
    block.rect.y = random.randrange (screen_height)    
    
    for i in range(5):
        # This represents a block
        gas = Block(RED, 15, 20)
        gas.image = pygame.image.load("images.jpg").convert()
        gas.rect = gas.image.get_rect()
        gas.rect.x = random.randrange (screen_width)
        gas.rect.y = random.randrange (screen_height)       

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)
player.image = pygame.image.load("rocket.png").convert()


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0
background_image = pygame.image.load("space.png")


def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # return True
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False
        screen.fill(BLACK)
        text = my_font.render("Welcome to Outer Space", True, WHITE)
        text2 = my_font.render("Press Enter to Start", True, WHITE)
        screen.blit(text, [200, 230])
        screen.blit(text2, [224, 270])
        pygame.display.flip()
        clock.tick(60)


# Start the intro screen loop before the main loop
intro_screen()

lives = 3

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                speed_x = 1
            if event.key == pygame.K_LEFT: 
                speed_x = -1
            if event.key == pygame.K_UP: 
                speed_y = -1
            if event.key == pygame.K_DOWN: 
                speed_y = 1
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT: 
                speed_x = 0
            if event.key == pygame.K_LEFT: 
                speed_x = 0 
            if event.key == pygame.K_UP: 
                speed_y = 0 
            if event.key == pygame.K_DOWN: 
                speed_y = 0       
            
    # Clear the screen
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    # Get the current mouse position. This returns the position
    # as a list of two numbers.

    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x += speed_x * player.speed
    player.rect.y += speed_y * player.speed
    if player.rect.x >= screen_width - player.width:
        player.rect.x = screen_width - player.width
    if player.rect.x <= 0:
        player.rect.x = 0
    if player.rect.y >= screen_height - player.height:
        player.rect.y = screen_height - player.height
    if player.rect.y <= 0:
        player.rect.y = 0

    sprite_list = block_list.sprites()
    for i in range(len(sprite_list)):
        bad_block = sprite_list[i]
        bad_block.rect.x += bad_block.direction * bad_block.speed
        if bad_block.rect.x >= screen_width - bad_block.width:
            bad_block.rect.x = screen_width - bad_block.width
            bad_block.direction *= -1
        if bad_block.rect.x <= 0:
            bad_block.rect.x = 0
            bad_block.direction *= -1

    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    #gas_hit_list = pygame.sprite.spritecollide(player, gas_list, True)
    

    # Check the list of collisions.
    for block in blocks_hit_list:
        # score += 1
        #
        # print(score)
        lives -= 1
    
    #for gas in gas_hit_list:
        #lives += 1
    
    if lives <= 0:
        done = True
        

    # Draw all the spites
    all_sprites_list.draw(screen)
    
    my_font_2 = pygame.font.SysFont("Calibri", 20, True, False)
    my_text = my_font_2.render(("Lives:" +str(lives)), True, WHITE)
    
    screen.blit(my_text, [0, 0])
    
    if lives <= 0:
        my_font_3 = pygame.font.SysFont("Calibri", 150, True, False)
        my_text_2 = my_font_3.render("YOU LOSE", True, RED)
        screen.blit(my_text_2, [59, 200])           
    if lives >= 10:
            my_font_4 = pygame.font.SysFont("Calibri", 150, True, False)
            my_text_3 = my_font_4.render("YOU WIN", True, GREEN)
            screen.blit(my_text_2, [59, 200])         
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)
    

pygame.quit()