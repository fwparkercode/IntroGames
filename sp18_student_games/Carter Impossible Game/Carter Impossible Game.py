

# Basics
import pygame
import random
score = 0
fails = 0
coin_number = 4
level = 1
intro_ship = 0

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (0, 102, 204)
GREEN = (128, 255, 0)
level = 1
frame = 0


# Define Player Class
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.image.load("ship (1).png")
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 200
 
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
        
        if self.rect.x > 673:
            self.rect.x = 673
           
        if self.rect.x < 0:
            self.rect.x = 0
        
            
        if self.rect.y > 376:
            self.rect.y = 376
          
        if self.rect.y < 0:
            self.rect.y = 0        
          
            
        
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
                

# Define Enmey Class                
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface([20, 20])
        #self.image.fill(RED)
        self.image = pygame.image.load("ship (2).png")
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 3
    def update(self):
        self.rect.y += 2.5
        if self.rect.top > screen_height:
            self.rect.bottom = 22
            self.rect.x = self.rect.x
        self.rect.x += 0
        if self.rect.right > screen_width:
            self.rect.right = self.rect.x
            self.speedx *= -1
        if self.rect.left < 0:
            self.rect.left = self.rect.x
            self.speedx *= -1

# Define Block Class 
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
        
        
# Define Goal Class
class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.image.load("Goal_Image.png")
        self.rect = self.image.get_rect()
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x    

# Define Wall Class        
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height,):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("right_wall_tile.png")
        
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
# Define Fonts        
pygame.init()
my_font = pygame.font.SysFont("Calibri", 40, True, False)

background_music = pygame.mixer.Sound("Pirate1_Theme1.ogg")
background_music.set_volume(1) # float from 0 to 1
background_music.play(-1)

 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

wall_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
goal_list = pygame.sprite.Group()   


# Creating Level 1
if level == 1:
    # Initialize Pygame
 
    
    # Screen Walls 
    
    wall = Wall(0, 250, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    wall = Wall(0, 0, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    wall = Wall(600, 250, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    wall = Wall(600, 0, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    # Spawn Walls 
    
    
    # Goal
    
    goal = Goal(620,185,100,50)
    goal_list.add(goal)
    all_sprites_list.add(goal)
    
    
    
    # Enemys
    
    enemy = Enemy()
    enemy.rect.x = 150 - enemy.rect.width
    enemy.rect.y = 10 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 220 - enemy.rect.width
    enemy.rect.y = 10 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 290 - enemy.rect.width
    enemy.rect.y = 10 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 360 - enemy.rect.width
    enemy.rect.y = 10 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 430 - enemy.rect.width
    enemy.rect.y = 10 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 500 - enemy.rect.width
    enemy.rect.y = 10 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 570 - enemy.rect.width
    enemy.rect.y = 10 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    # Create the player paddle object
    player = Player(50, 50)
    player.walls = wall_list
     
    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    good_block_list = pygame.sprite.Group()
    bad_block_list = pygame.sprite.Group()
    
     
    
    # Coins
    for i in range(coin_number):
        # This represents a block
        block = Block(GREEN, 20, 15)
        block.image = pygame.image.load("coin.png")
     
        # Set a random location for the block
        block.rect.x = random.randrange(110,580)
        block.rect.y = random.randrange(10,screen_height - 25)
            
        
     
        # Add the block to the list of objects
        good_block_list.add(block)
        all_sprites_list.add(block)
        
        
    
        
    
    # Create Player
    player = Player(20, 15)
    player.walls = wall_list
    all_sprites_list.add(player)
     
    # Loop until the user clicks the close button or level is completed
    done = False
    
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    score = 0
    fails = 0
    
    # Defining sounds
    goodhit_sound = pygame.mixer.Sound("goodsound.ogg")
    goodhit_sound.set_volume(.1) # float from 0 to 1
    fail_sound = pygame.mixer.Sound("fail_sound.wav")
    fail_sound.set_volume(.1) # float from 0 to 1

    background_image = pygame.image.load("Water_Background.png")
     

# Creating Level 2   
def level_2():
    # Initialize Pygame
 
    
    # Screen Walls 
    
    wall = Wall(0, 250, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    wall = Wall(0, 0, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    wall = Wall(600, 250, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    wall = Wall(600, 0, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    # Spawn Walls 
    
    
    # Goal
    
    goal = Goal(620,185,100,50)
    goal_list.add(goal)
    all_sprites_list.add(goal)
    
    
    
    # Enemys
    
    # Row One
    
    enemy = Enemy()
    enemy.rect.x = 150 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 220 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 290 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 360 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 430 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 500 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 570 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    # Row Two
    
    enemy = Enemy()
    enemy.rect.x = 125 - enemy.rect.width
    enemy.rect.y = -200 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)    
    
    enemy = Enemy()
    enemy.rect.x = 185 - enemy.rect.width
    enemy.rect.y = -200 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 255 - enemy.rect.width
    enemy.rect.y = -200 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)     
    
    enemy = Enemy()
    enemy.rect.x = 325 - enemy.rect.width
    enemy.rect.y = -200 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy) 
    
    enemy = Enemy()
    enemy.rect.x = 395 - enemy.rect.width
    enemy.rect.y = -200 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 465 - enemy.rect.width
    enemy.rect.y = -200 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 535 - enemy.rect.width
    enemy.rect.y = -200 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 600 - enemy.rect.width
    enemy.rect.y = -200 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)    
    
    
    
    
    # Create the player
    player = Player(50, 50)
    player.walls = wall_list
     

    
     

    # Creates coins
    for i in range(coin_number):
        # This represents a block
        block = Block(GREEN, 20, 15)
        block.image = pygame.image.load("coin.png")
        block.rect = block.image.get_rect()
     
        # Set a random location for the block
        block.rect.x = random.randrange(110,580)
        block.rect.y = random.randrange(10,screen_height - 25)
            
        
     
        # Add the block to the list of objects
        good_block_list.add(block)
        all_sprites_list.add(block)
        
    
     
    # Create a RED player block
    player = Player(20, 15)
    player.walls = wall_list
    
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    score = 0
    fails = 0
    
    # Creates sounds
    goodhit_sound = pygame.mixer.Sound("goodsound.ogg")
    goodhit_sound.set_volume(.1) # float from 0 to 1
    fail_sound = pygame.mixer.Sound("fail_sound.wav")
    fail_sound.set_volume(.1) # float from 0 to 1

    background_image = pygame.image.load("Water_Background.png")

# Creating Level 3    
def level_3():
    # Initialize Pygame
 
    
    # Screen Walls 
    
    wall = Wall(0, 0, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    wall = Wall(0, 250, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    wall = Wall(600, 250, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    wall = Wall(600, 0, 100, 200)
    wall_list.add(wall)
    all_sprites_list.add(wall)
    
    # Spawn Walls 
    
    
    # Goal
    
    goal = Goal(620,185,100,50)
    goal_list.add(goal)
    all_sprites_list.add(goal)
    
    
    
    # Enemys
    
    # Row One
    enemy = Enemy()
    enemy.rect.x = 125 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)    
    
    enemy = Enemy()
    enemy.rect.x = 185 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 255 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)     
    
    enemy = Enemy()
    enemy.rect.x = 325 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy) 
    
    enemy = Enemy()
    enemy.rect.x = 395 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 465 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 535 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 600 - enemy.rect.width
    enemy.rect.y = 0 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)    
    
    
    # Row Two
    
    enemy = Enemy()
    enemy.rect.x = 150 - enemy.rect.width
    enemy.rect.y = -133.333333333 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 220 - enemy.rect.width
    enemy.rect.y = -133.333333333 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 290 - enemy.rect.width
    enemy.rect.y = -133.333333333 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 360 - enemy.rect.width
    enemy.rect.y = -133.333333333 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 430 - enemy.rect.width
    enemy.rect.y = -133.333333333 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 500 - enemy.rect.width
    enemy.rect.y = -133.333333333 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 570 - enemy.rect.width
    enemy.rect.y = -133.333333333 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)    
    
    #Row three
    
    enemy = Enemy()
    enemy.rect.x = 150 - enemy.rect.width
    enemy.rect.y = -266.6666666666 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 220 - enemy.rect.width
    enemy.rect.y = -266.6666666666 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 290 - enemy.rect.width
    enemy.rect.y = -266.6666666666 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 360 - enemy.rect.width
    enemy.rect.y = -266.6666666666 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 430 - enemy.rect.width
    enemy.rect.y = -266.6666666666 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 500 - enemy.rect.width
    enemy.rect.y = -266.6666666666 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    
    enemy = Enemy()
    enemy.rect.x = 570 - enemy.rect.width
    enemy.rect.y = -266.6666666666 - enemy.rect.width
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)    
    
    
    
    
    
    
    # Create the player
    player = Player(50, 50)
    player.walls = wall_list

    # Creates coins
    for i in range(coin_number):
        # This represents a block
        block = Block(GREEN, 20, 15)
        block.image = pygame.image.load("coin.png")
        block.rect = block.image.get_rect()
     
        # Set a random location for the block
        block.rect.x = random.randrange(110,580)
        block.rect.y = random.randrange(10,screen_height - 25)
            
        
     
        # Add the block to the list of objects
        good_block_list.add(block)
        all_sprites_list.add(block)
        
    
     
    # Create a RED player block
    player = Player(20, 15)
    player.walls = wall_list
    
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    score = 0
    fails = 0
    
    # creates sounds
    goodhit_sound = pygame.mixer.Sound("goodsound.ogg")
    goodhit_sound.set_volume(.1) # float from 0 to 1
    fail_sound = pygame.mixer.Sound("fail_sound.wav")
    fail_sound.set_volume(.1) # float from 0 to 1
 
    background_image = pygame.image.load("Water_Background.png")    
    

# creates intro screen   
def intro_screen():
    done = False
    main_font = pygame.font.SysFont("Calibri", 50, True, False)
    second_font = pygame.font.SysFont("Calibri", 30, True, False)
     
    while not done:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(WHITE)
        screen.blit(background_image, [0, 0])
        text = main_font.render("Welcome To Pirates", True, BLACK)
        screen.blit(text, [150, 10])
        
        text = second_font.render("Collect Coins", True, BLACK)
        screen.blit(text, [80, 150])        
        pygame.display.flip()
        clock.tick(60)
        
        text = second_font.render("Move Using the Arrow Keys", True, BLACK)
        screen.blit(text, [350, 150])        
        pygame.display.flip()
        clock.tick(60)
        
        text = second_font.render("Press the Space Bar to Start", True, BLACK)
        screen.blit(text, [340, 300])        
        pygame.display.flip()
        clock.tick(60)   
        
        text = second_font.render("Reach the Safe Zone", True, BLACK)
        screen.blit(text, [40, 300])        
        pygame.display.flip()
        clock.tick(60)

# creates end screen       
def end_screen():
    done = False
    main_font = pygame.font.SysFont("Calibri", 50, True, False)
    third_font = pygame.font.SysFont("Calibri", 40, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(WHITE)
        screen.blit(background_image, [0, 0])
        text = main_font.render("You Won!!!!!", True, BLACK)
        screen.blit(text, [235, 10])
        
        text = third_font.render("You are the superior Pirate", True, BLACK)
        screen.blit(text, [150, 150])        
        pygame.display.flip()
        clock.tick(60)
        
     
        

        
# runs intro screen
intro_screen()
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
    frame += 1
    
    if frame > 300:
        screen.fill(WHITE)
    else:
        screen.fill(WHITE)
    # Clear the screen
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
   
   
    
 
    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
    hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
    
    for enemy in hit_list:
        player.rect.x = 50
        player.rect.y = 200
        fails += 1
        fail_sound.play()
        
    if score == coin_number:
    
        goal_list_hit_list = pygame.sprite.spritecollide(player, goal_list, True)
    
        for i in goal_list_hit_list:
            enemy_list.empty()
            all_sprites_list.empty()
            good_block_list.empty()         
            all_sprites_list.add(player)       
            level += 1
            coin_number *= 2
            score *= 0
            player.rect.x = 50
            player.rect.y = 200
            if level == 2:
                level_2()       
            if level == 3:
                level_3()     
            if level == 4:
                end_screen()
            
        else:
            pygame.sprite.spritecollide(player, goal_list, False)

    
            
            
        

       
 
    # Check the list of collisions.
    for block in good_blocks_hit_list:
        score += 1
        goodhit_sound.play()
 
    # Draw all the spites
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    
    my_text = my_font.render("coins: " + str(score) + "/" + str(coin_number), True, BLACK)
    screen.blit(my_text, [40,40])  
    
    my_text = my_font.render("Fails: " + str(fails), True, BLACK)
    screen.blit(my_text, [540,40])    
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()