"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame
import random
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (121, 206, 252)
 
 
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        
        self.image = pygame.image.load("fish.png")
        self.rect = self.image.get_rect()
        
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        
        self.lives = 3
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
        
           
 
            

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
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
 
        if self.rect.right < 0:
            self.rect.left = screen_width
            
        if self.rect.bottom > self.bottom_boundary or self.rect.top < self.top_boundary:
            self.change_y *= -1


# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# Create the player object
player = Player(0, 300)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
block_list = pygame.sprite.Group() 
 
clock = pygame.time.Clock()
done = False
for i in range(5):
    # This represents a block
    block = Block(RED, 20, 15)
    block.image = pygame.image.load("shark.png")
    block.rect = block.image.get_rect()        
    # Set a random location for the block
    block.rect.x = random.randrange(300, screen_width + 300)
    block.rect.y = random.randrange(screen_height)
 
    block.change_x = random.randrange(-5, 0)
    block.change_y = random.randrange(-2, 3)
    block.left_boundary = 0
    block.top_boundary = 0
    block.right_boundary = screen_width
    block.bottom_boundary = screen_height
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

win = pygame.mixer.Sound("win.wav")
death = pygame.mixer.Sound("death.wav")
shark = pygame.mixer.Sound("shark.wav")
background = pygame.mixer.Sound("background.wav")
water = pygame.mixer.Sound("water.wav")
level = 1
my_font = pygame.font.SysFont('Indie Flower', 25, True, False)

def intro_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False
        screen.fill(BLUE)
        text = my_font.render("PLAY SHARKS AND MINOS!", True, WHITE)
        text2 = my_font.render("USE THE ARROW KEYS TO AVOID THE SHARKS", True, WHITE)
        text3 = my_font.render("GOAL: TO COMPLETE THROUGH LEVEL 10!", True, WHITE)
        text4 = my_font.render("YOU HAVE 3 LIVES, GOOD LUCK!", True, WHITE)
        text5 = my_font.render("CLICK THE SPACE BAR TO BEGIN", True, WHITE)
        screen.blit(text, [270, 200])
        screen.blit(text2, [180, 240])
        screen.blit(text3, [200, 280])
        screen.blit(text4, [240, 320])
        screen.blit(text5, [240, 360])
        pygame.display.flip()
        clock.tick(60)
def dead_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return True
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = False
                    return False
                if event.key == pygame.K_RETURN:
                    intro_screen()
                    done = False
                    return False
        screen.fill(BLUE)
        text = my_font.render("GAME OVER", True, WHITE)
        text2 = my_font.render("CLICK THE SPACE BAR TO PLAY AGAIN", True, WHITE)
        text3 = my_font.render("CLICK RETURN FOR THE HOME SCREEN", True, WHITE)
        screen.blit(text, [340, 220])
        screen.blit(text2, [220, 260])
        screen.blit(text3, [220, 300])
        pygame.display.flip()
        clock.tick(60)
def win_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return True
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = False
                    return False
                if event.key == pygame.K_RETURN:
                    intro_screen()
                    done = False
                    return False
    
        screen.fill(BLUE)
        text = my_font.render("YOU WON!", True, WHITE)
        text2 = my_font.render("CLICK THE SPACE BAR TO PLAY AGAIN", True, WHITE)
        text3 = my_font.render("CLICK RETURN FOR THE HOME SCREEN", True, WHITE)
        screen.blit(text, [360, 220])
        screen.blit(text2, [220, 260])
        screen.blit(text3, [220, 300])
        pygame.display.flip()
        clock.tick(60)
   
intro_screen()


#_______________________________________#    
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-5, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(5, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -5)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 5)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(5, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-5, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 5)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -5)
        
 
    # --- Game logic
     
    # This calls update on all the sprites
    all_sprites_list.update()
    
    if player.rect.right > 800:
        water.play()
        player.rect.midleft = (0, 300)
        level += 1
        if level == 11:
            win.play()
            level = 1
            player.lives = 3
            done = win_screen()
            player.change_y = 0
            player.change_x = 0           
        for block in block_list:
            # Set a random location for the block
            block.rect.x = random.randrange(300, screen_width + 300)
            block.rect.y = random.randrange(screen_height - block.rect.height)
         
            block.change_x = random.randrange(-5, 0)
            block.change_y = random.randrange(-2, 3)
            block.left_boundary = 0
            block.top_boundary = 0
            block.right_boundary = screen_width
            block.bottom_boundary = screen_height
            
            print(my_text)
            print(my_lives)   
         
        for i in range(2):
            # This represents a block
            block = Block(RED, 20, 15)
            block.image = pygame.image.load("shark.png")
            block.rect = block.image.get_rect()                
            
            # Set a random location for the block
            block.rect.x = random.randrange(300, screen_width + 300)
            block.rect.y = random.randrange(screen_height- block.rect.height)
         
            block.change_x = random.randrange(-5, 0)
            block.change_y = random.randrange(-2, 3)
            block.left_boundary = 0
            block.top_boundary = 0
            block.right_boundary = screen_width
            block.bottom_boundary = screen_height 
         
                # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)              
        
        
    for block in block_list:
        if pygame.sprite.collide_rect(block, player):
            shark.play()
            player.rect.midleft = (0, 300)
            player.lives -= 1
            print(my_lives)
            if player.lives == 0:
                death.play()
                player.lives = 3
                level = 1
                done = dead_screen()
                player.change_y = 0
                player.change_x = 0                   
            for block in block_list:
                # Set a random location for the block
                block.rect.x = random.randrange(300, screen_width + 300)
                block.rect.y = random.randrange(screen_height)
             
                block.change_x = random.randrange(-5, 0)
                block.change_y = random.randrange(-2, 3)
                block.left_boundary = 0
                block.top_boundary = 0
                block.right_boundary = screen_width
                block.bottom_boundary = screen_height
                
        elif player.rect.top < 0:
            player.rect.top = 0
        elif player.rect.bottom > 600:
            player.rect.bottom = 600
            
    
    background_image = pygame.image.load("sea.png")
 
    # -- Draw everything
    # Clear screen
    screen.fill(BLUE)  
    screen.blit(background_image, [0,0])
    
       
    # Draw sprites
  
    my_text = my_font.render("Level: " + str(level), True, BLACK)
    my_lives = my_font.render("Lives: " + str(player.lives), True, BLACK)    
    screen.blit(my_text, [20,20])
    all_sprites_list.draw(screen)    
    screen.blit(my_lives,[100,20])
    # Flip screen
    pygame.display.flip()
            
 
    # Pause
    clock.tick(60)
 
pygame.quit()