import pygame
import random
import math
# import doggo_fam
 
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
DANK_BLUE = (0, 75, 127)

level = 1
level_number = 50
tick = 0
level_speed = 1
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.init()

# Sounds
background_music = pygame.mixer.Sound("background.wav")
slap = pygame.mixer.Sound("slap.wav")

# Make the lists
wall_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

# Make the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

 
# player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        # HWAT
        self.walls = None
        self.accel = 0.5
        self.jumping = False
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        self.change_y += self.accel
        # Move left/right
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        
        
        for block in block_hit_list:
            if self.change_x >= 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        # Move Up/Down
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.change_y = 0
                # figure out if you're on the ground so it knows when to make you jump
                self.jumping = False
                break
            else:
                self.rect.top = block.rect.bottom
                self.change_y = 0
        # make it so you don't accidentally fall through the bottom of the screen
        if self.rect.bottom > SCREEN_HEIGHT - 10:
            self.rect.bottom = SCREEN_HEIGHT - 30
       # make it so you can't go off the right of the screen
        if self.rect.x >= SCREEN_WIDTH - 15:
            self.rect.x = SCREEN_WIDTH -15
        
                
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
         
            
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height, speed):
        super().__init__()
        
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        
        self.speed = speed
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
                
# randomly make a level      
class Level():
    def __init__(self):
        for i in range(level_number): # This is a variable so the amount of wall can increase
            level_wall = Wall(random.randrange(SCREEN_WIDTH + 10, 2800), random.randrange(0, SCREEN_HEIGHT - 10), random.randrange(10, 100), random.randrange(10, 100), level_speed) # I have a level_speed variable here in case I wanted to make it faster for later versions. But when I did, I met some really confusing glitches.
            wall_list.add(level_wall)
            all_sprite_list.add(level_wall)
        player.walls = wall_list
            

# Create a player
player = Player(100, SCREEN_HEIGHT - 50)
player.add(all_sprite_list)

# Create the bottom wall
bottom_wall = Wall(-10, SCREEN_HEIGHT - 10, SCREEN_WIDTH + 10, 10, 0)
wall_list.add(bottom_wall)
all_sprite_list.add(bottom_wall)

# make the first level trigger
if level == 1:
    Level()

# this becomes the level counter at the top of the screen
levelfont = pygame.font.SysFont('Calibri', 25, True, False)

done = False

clock = pygame.time.Clock()

def game_over(): # Game over screen code VVV
    done = False
    my_font1 = pygame.font.SysFont("Calibri", 50, True, False)
    my_font2 = pygame.font.SysFont("Calibri", 40, True, True)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        text1 = my_font1.render("YOU DIED", True, BLUE)
        text2 = my_font2.render("You were on level " + str(level), True, WHITE)
        screen.blit(text1, [SCREEN_WIDTH / 2 - 110, 50])
        screen.blit(text2, [SCREEN_WIDTH / 2 - 170, 150])
        pygame.display.flip()
        clock.tick(60)
# intro screen code VVV
def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 50, True, False)
    my_font2 = pygame.font.SysFont("Calibri", 30, True, True)
    my_font3 = pygame.font.SysFont("Calibri", 25, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        text = my_font.render("Welcome to Block Jump!", True, BLUE)
        text2 = my_font2.render("Use the arrow keys to move", True, WHITE)
        text3 = my_font3.render("If you go off the left of the screen, you die.", True, BLUE)
        screen.blit(text3, [180, 400])
        screen.blit(text2, [220, 200])
        screen.blit(text, [150, 50])
        pygame.display.flip()
        clock.tick(60)


background_music.play(-1)


# Start the intro screen loop before the main loop
intro_screen()



# --------Main Program Loop ----------
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            done = True
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    if not player.jumping:           
                        player.change_y = -16 
                        player.jumping = True  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.change_x = 0
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.change_x = 0     
        if player.rect.x < 0:
            background_music.stop()
            slap.play()
            game_over()
            done = True
            
               
    tick += 1      
    
    leveltext = levelfont.render("Level " + str(level),True,WHITE)    

        
    if len(wall_list) == 1:
        level += 1
        level_number += 40
        Level()
        
            
    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
 
    screen.blit(leveltext, [5, 5])
                
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit() 