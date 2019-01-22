"""
CREATED BY OWEN BOWERS
ONLY 1 LEVEL!
"""

import pygame
from spritesheet_functions import SpriteSheet
import constants
import za
from za import Za
from player import Player
import platforms
from platforms import MovingPlatform

#import enemy
#from enemy import EnemyD
BLACK = ( 0,0,0)
WHITE = (255,255,255)
pygame.init()
#background_music = pygame.mixer.Sound("ispy3.wav")
import pygame
import constants
import laser
import sys
score = 0
pos = (576, 720, 70, 70)
laser_list = []
enemy_list = []
bad_laser_list = []
pizza_list = []
laser_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
bad_laser_list = pygame.sprite.Group()
pizza_list = pygame.sprite.Group()
class EnemyD(pygame.sprite.Sprite):
    level = None
    def __init__(self):
        super().__init__()
        self.laser_list = None
        self.image = pygame.image.load("communism_doggo.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 800
        self.change_x = 0
    def update(self):
        laser_hit_list = pygame.sprite.spritecollide(self, laser_list, True)
        for laser in laser_hit_list:
                self.kill()
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """
  
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.stops = True
        sprite_sheet = SpriteSheet("p1_walk.png")
        # Load all the right facing images into a list
        for i in range(9):
            image = sprite_sheet.get_image(i * 64, 704, 64, 64)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(i * 64, 704, 64, 64)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)            
    
     
        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.lives = 3 

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        laser_hit_list = pygame.sprite.spritecollide(self, bad_laser_list, True)
        for laser in laser_hit_list:
                self.lives -= 1 
        pizza_hit_list = pygame.sprite.spritecollide(self, pizza_list, True)
        for pizza in pizza_hit_list:
                self.lives += 1
                pizza.kill()
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R" and self.stops == False:
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L" and self.stops == False:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        elif self.direction == "R" and self.stops == True:
            self.image = self.walking_frames_r[0]
        else:
            self.image = self.walking_frames_l[0]        

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"
        self.stops = False
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"
        self.stops = False
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.stops = True
    #def fire(self):
class Laser(pygame.sprite.Sprite):
    
    def __init__(self,direction):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.move = 0
       
        
        sprite_sheet = SpriteSheet("lasers.png")
        image = sprite_sheet.get_image( 275, 60, 20, 20)
        if direction == "L":
            image = pygame.transform.flip(image, True, False)
        
 
        # Set the image the player starts with
        self.image = image
    
        # Set a referance to the image rect.
        
        self.rect = self.image.get_rect()        
        self.rect.x = 0
        if direction == "R":
            self.move = 5
        else:
            self.move = -5
        sprite_sheet = SpriteSheet("p1_walk.png")
    def update(self):
        self.rect.x += self.move
        if self.rect.x >= 1000 or self.rect.x <= -1000:
            self.kill()
class Bad_Laser(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.move = 0
       
        
        sprite_sheet = SpriteSheet("lasers.png")
        image = sprite_sheet.get_image( 275, 0, 20, 20)
        
        image = pygame.transform.flip(image, True, False)
                    
      
 
        # Set the image the player starts with
        self.image = image
    
        # Set a referance to the image rect.
        
        self.rect = self.image.get_rect()        
        self.rect.x = 0
        self.move = -3
    def update(self):
        self.rect.x += self.move
        if self.rect.x >= 850 or self.rect.x <= -50:
            self.kill()
        
           
 
class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    
    
    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        for laser in bad_laser_list:
            laser.rect.x += shift_x
        for pizza in pizza_list:
            pizza.rect.x += shift_x        
            

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)
         
        self.background = pygame.image.load("back.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
        pos = (576, 720, 70, 70)
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 500, 500,"plat"],
                  [platforms.GRASS_MIDDLE, 568, 500,"plat"],
                  [platforms.GRASS_RIGHT, 636, 500,"plat"],
                  [platforms.GRASS_LEFT, 800, 400,"plat"],
                  [platforms.GRASS_MIDDLE, 868, 400,"plat"],
                  [platforms.GRASS_RIGHT, 936, 400,"plat"],
                  [platforms.GRASS_LEFT, 1000, 500,"plat"],
                  [platforms.GRASS_MIDDLE, 1068, 500,"plat"],
                  [platforms.GRASS_RIGHT, 1136, 500,"plat"],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280,"plat"],
                  [platforms.STONE_PLATFORM_MIDDLE, 1191, 280,"plat"],
                  [za.pizzapos, 1191,240, "pizza"],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280,"plat"],
                  [za.pizzapos, 100,400, "pizza"],
                  [platforms.STONE_PLATFORM_LEFT, 1500, 550,"plat"],
                  [platforms.STONE_PLATFORM_MIDDLE, 1570, 550,"plat"],
                  [za.pizzapos, 1571,400, "pizza"],
                  [platforms.STONE_PLATFORM_RIGHT, 1640, 550,"plat"],
                  [platforms.GRASS_LEFT,1800, 400,"plat"],
                  [platforms.GRASS_MIDDLE, 1870, 400,"plat"],
                  [platforms.GRASS_RIGHT, 1940, 400,"plat"],
                  [platforms.GRASS_LEFT, 2000, 500,"plat"],
                  [platforms.GRASS_MIDDLE, 2070, 500,"plat"],
                  [platforms.GRASS_RIGHT, 2140, 500,"plat"],
                  [platforms.STONE_PLATFORM_LEFT, 2120, 280,"plat"],
                  [platforms.STONE_PLATFORM_MIDDLE, 2190, 280,"plat"],
                  [platforms.STONE_PLATFORM_RIGHT, 2260, 280,"plat"] ,                 
                  [pos, 1870 ,300, "enemy"],
                  [pos, 2070 ,400, "enemy"],
                  [pos, 2190 ,180, "enemy"],
                  [pos, 868 ,300, "enemy"],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            if platform[3] == "plat":
                block = platforms.Platform(platform[0])
                block.rect.x = platform[1]
                block.rect.y = platform[2]
                block.player = self.player
                self.platform_list.add(block)
            elif platform[3] == "pizza":
                block = za.Za()
                block.rect.x = platform[1]
                block.rect.y = platform[2]
                block.player = self.player
                pizza_list.add(block) 
            else:
                block = EnemyD()
                block.rect.x = platform[1]
                block.rect.y = platform[2]
                block.player = self.player
                self.platform_list.add(block)
                enemy_list.add(block)
                print(enemy_list)
                #block.laser_list = levels.laser_list

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """
        
        # Call the parent constructor
        Level.__init__(self, player)
        
        self.background = pygame.image.load("background_01.jpg").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000
     
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)     
      
def start():
    # STARTUP SCREEN
    font = pygame.font.SysFont('Calibri', 40, True, False)
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lil Boat - The Game")
    donez = False
    clock = pygame.time.Clock()
    
    while not donez:
        screen.fill(BLACK)
        text = font.render("Use WASD to move and spacebar to shoot", True, WHITE)
        text2 = font.render("Press space to begin", True, WHITE)
        screen.blit(text,[100,200])
        screen.blit(text2,[230,300])
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                donez = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    donez = True
       
    
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip() 
            clock.tick(60)
def die():
    # STARTUP SCREEN
    font = pygame.font.SysFont('Calibri', 40, True, False)
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lil Boat - The Game")
    donez = False
    clock = pygame.time.Clock()
    
    while not donez:
        screen.fill(BLACK)
        text = font.render("You died", True, WHITE)
        text2 = font.render("Press space to quit", True, WHITE)
        screen.blit(text,[100,200])
        screen.blit(text2,[230,300])
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                donez = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    donez = True
                    
       
    
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip() 
            clock.tick(60)     
        
def main():
    """ Main Program """
    score = 0
    
    ht = pygame.image.load("heart.png")
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Lil Boat - The Game")

    # Create the player
    player = Player()
    
    #pizza = Za(400,400)
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()

    player.level = current_level
    music = pygame.mixer.Sound("ispy.ogg")
    pew = pygame.mixer.Sound("phasers3.wav")
    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    #active_sprite_list.add(pizza)
    #Loop until the user clicks the close button.
    donez = False
    lcn = 0
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    music.play(0)
    # -------- Main Program Loop -----------
    while not donez:
        #enemy_list = level_list[0].enemy_list
        print(enemy_list)        
        lives = player.lives
        if lives <= 0:
            donez = True
            
        for event in pygame.event.get(): # User did something
            
            if event.type == pygame.QUIT: # If user clicked close
                donez = True
            
                # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_w:
                    player.jump()
                if event.key == pygame.K_SPACE:
            
                    laser = Laser(player.direction)
                    laser.rect.x = player.rect.x + 30
                    laser.rect.y = player.rect.y + 30
                    active_sprite_list.add(laser)
                    pew.play(0)
                    laser_list.add(laser) 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()
        for laser in laser_list:
            laser_hit_list = pygame.sprite.spritecollide(laser, enemy_list, True)
            for enemy in laser_hit_list:
                laser_list.remove(laser)
                score += 50
                #allsprite?
        lcn +=1
        if lcn == 15 or lcn == 30:
            for enemy in enemy_list:
                blas = Bad_Laser()
                blas.rect.x = enemy.rect.x +35
                blas.rect.y = enemy.rect.y + 60
                print("checking..")
                bad_laser_list.add(blas)
                     
        if lcn == 90:
            lcn = 0
        
        #print("checking..")
        # Update the player.
        active_sprite_list.update()
        laser_list.update()
        bad_laser_list.update()
        pizza_list.update()
        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        laser_list.draw(screen)
        bad_laser_list.draw(screen)
        pizza_list.draw(screen)
        if lives >= 1:
            screen.blit(ht,[5,5])
            
        if lives >= 2:
            screen.blit(ht,[45,5])
        if lives >= 3:
            screen.blit(ht,[85,5])        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.display.quit()
    pygame.quit()
    #sys.exit()
    
start()
main()
  

