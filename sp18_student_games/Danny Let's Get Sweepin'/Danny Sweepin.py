import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ROYAL = (95, 39, 216)
level = 0 

'''
#i tried adding a background song but my computer would not allow me
background_sound = pygame.sound.load()

'''
class Player(pygame.sprite.Sprite): 
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor        
        super().__init__()
        
         # Set height, width
        '''
        self.image = pygame.Surface([15, 15])

        self.pygame.image.load("broom.png").convert()
        '''
         
        self.image = pygame.image.load("broom.png")
        
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
        self.rect.y += self.change_y
        if self.rect.x <= 0:
            self.rect.x = 0
            bump_sound.play()
        if self.rect.x >= 685:
            self.rect.x = 685
            bump_sound.play()
        if self.rect.y <= 0:
            self.rect.y = 0
            bump_sound.play()
        if self.rect.y >= 485:
            self.rect.y = 485
            bump_sound.play()
 
class Block(pygame.sprite.Sprite):   
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """    
    def __init__(self, color, width, height):
        
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
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

good_block_sound = pygame.mixer.Sound("good_block.wav")
bad_block_sound = pygame.mixer.Sound("bad_block.wav")
bump_sound = pygame.mixer.Sound("bump.wav")

# Set the height and width of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    block = Block(GREEN, 20, 15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block.image = pygame.image.load("dirt.png") 
    block.image.set_colorkey(WHITE)    
    good_block_list.add(block)
    all_sprites_list.add(block)
    
for i in range(50):
    block = Block(RED, 20, 15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block.image = pygame.image.load("water.png")
    block.image.set_colorkey(WHITE)
    bad_block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Player(20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
time = 3600
level = 1


# intro screen
def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 50, True, False)
    my_font2 = pygame.font.SysFont("Calibri", 25, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(ROYAL)
        text = my_font.render("Let's get sweepin'", True, WHITE)
        screen.blit(text, [screen_width/2 - text.get_width()/2, 210])
        text = my_font2.render("Click to Begin", True, WHITE)
        screen.blit(text, [screen_width/2 - text.get_width()/2, 260])
        pygame.display.flip()
        clock.tick(60)
        
def over_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 50, True, False)
    my_font2 = pygame.font.SysFont("Calibri", 25, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(ROYAL)
        text = my_font.render("Game Over!", True, WHITE)
        screen.blit(text, [screen_width/2 - text.get_width()/2, 210])           
        pygame.display.flip()
        clock.tick(60) 
        
def win_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 50, True, False)
    my_font2 = pygame.font.SysFont("Calibri", 25, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(ROYAL)
        text = my_font.render("You won!", True, WHITE)
        screen.blit(text, [screen_width/2 - text.get_width()/2, 210])           
        pygame.display.flip()
        clock.tick(60) 
    


# Start the intro screen loop before the main loop
intro_screen()

font = pygame.font.SysFont("Calibri", 30)
# -------- Main Program Loop -----------




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
                
  
                
    all_sprites_list.update()
    
    time -= 1 
    
    
    good_block_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_block_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
    
 
    # Clear the screen
    screen.fill(WHITE)
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    for good_block in good_block_hit_list:
        good_block_sound.play(1)
        score += 1
        
    for bad_block in bad_block_hit_list:
        bad_block_sound.play(0)
        score -=1
        
        '''
    if score >= 35:
        level += 1 
        ''' 
        
    if score == 35:
        level +=1
        score = 0

        for block in bad_block_list:
            block.kill()
     
        for i in range(50):
            block = Block(GREEN, 20, 15)
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_height)
            block.image = pygame.image.load("dirt.png") 
            block.image.set_colorkey(WHITE)    
            good_block_list.add(block)
            all_sprites_list.add(block)
    
        for i in range(50):
            block = Block(RED, 20, 15)
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_height)
            block.image = pygame.image.load("water.png")
            block.image.set_colorkey(WHITE)
            bad_block_list.add(block)
            all_sprites_list.add(block) 
        time = 3600 - level*540
                    
                    
    
        
    if time <= 0:
        over_screen()
        
    if level == 5:
        win_screen()
        
    
        
        
        
    text = font.render("Score: " + str(score), True, ROYAL)
    screen.blit(text,[0, 0])
    
    text2 = font.render("Time: " + str(time//60), True, ROYAL)
    screen.blit(text2,[616, 0])  
    
    text3 = font.render("Level: " + str(level), True, ROYAL)
    screen.blit(text3,[300, 0])    
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()