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

score = 0
decider = 0
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load("player.png")
        
        
        
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.health = 1
                
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        
        self.x = 0
        self.y = 0
        self.image = pygame.Surface([width, height])
        self.image.fill(color) 
        self.rect = self.image.get_rect()
        self.health = 1
        self.speedx = -1
        self.speedy = 0
        self.width = 0
        self.height = 0
        self.x += self.speedx
        self.y += self.speedy
        if self.x > 700:
            self.x = -self.size  
            
    def update(self):
        self.rect.x += self.speedx
        
    
        
                
        
 
# Initialize Pygame
pygame.init()

death_sound = pygame.mixer.Sound("oof.wav")
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
my_font =pygame.font.SysFont("Times New Roman", 30, True, False)
pygame.mixer.music.load('wiimusic.wav')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
cool_list = pygame.sprite.Group()

for i in range(6):
    width = random.randrange(20, 100)
    height = random.randrange(20, 100)

    wall = Wall(RED, width ,height)
    
    wall.rect.x = random.randrange(700, 1400)
    wall.rect.y = random.randrange(0, 500 - height)

   
    wall.speedx = -random.randrange(4,10)
    
    all_sprites_list.add(wall)
    cool_list.add(wall)

    
# This is a list of every sprite. 
# All blocks and the player block as well.


 
# Create a RED player block
player = Block()
all_sprites_list.add(player)



#wall_list.add(enemy)

'''
wall_rects = [

[400, 300, 400, 100],
[100, 100, 600, 200],
[400, 200, 50, 80],
[90, 600, 40, 40],
]

for wall_rect in wall_rects:
    new_wall = Wall(RED, 15 ,30)
    new_wall.rect.x = wall_rect[0]
    new_wall.rect.y = wall_rect[1]
    wall_list.add(new_wall)
    all_sprites_list.add(new_wall)
'''
def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
            screen.fill(RED)
            text = my_font.render("WELCOME TO ESCAPE FROM THE CASINO!", True, WHITE)
            screen.blit(text, [90, 50])
            text = my_font.render("CLICK HERE (click me!!) to continue!!!", True, WHITE)
            screen.blit(text, [90, 200])
            pygame.display.flip()
            
def gameover_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
            screen.fill(BLACK)
            text = my_font.render("You've been captured!!", True, WHITE)
            screen.blit(text, [250, 50])
            text = my_font.render("YOU LOSE", True, WHITE)
            screen.blit(text, [250, 200])
            pygame.display.flip()        

            
intro_screen()
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.constants.USEREVENT:
    
            pygame.mixer.music.load("wiimusic.wav")
            pygame.mixer.music.play()        
    # Clear the screen
    screen.fill(WHITE)
    
     
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
    all_sprites_list.update()

    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
 
    # See if the player block has collided with anything.
    
 
    # Check the list of collisions.
    cool_hit_list = pygame.sprite.spritecollide(player, cool_list, False)
    for wall in cool_hit_list:
        player.health -= 1
        death_sound.play()
        gameover_screen()

        
    if player.health <= 0:
        done = True
        
    
    
    for wall in cool_list:
        if wall.rect.right <= 0:
            wall.rect.right = random.randrange(700,1000)
            wall.rect.y = random.randrange(0,500)
            score += 1
            decider = random.randrange(0,4)
            
            if decider == 2:
                width = random.randrange(20, 100)
                height = random.randrange(20, 100)
                
                wall = Wall(RED, width ,height)
                    
                wall.rect.x = random.randrange(700, 1400)
                wall.rect.y = random.randrange(0, 500 - height)
                
                   
                wall.speedx = -random.randrange(4,10)
                    
                all_sprites_list.add(wall)
                cool_list.add(wall)
                
        
            
            
            
    

    
    my_text = my_font.render("Score = " + str(score), True, BLACK)
    screen.blit(my_text, [0,0])   
    # Draw all the spites
    all_sprites_list.draw(screen)
    #wall_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()