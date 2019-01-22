"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Player_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([15, 60])
        self.image.fill(BLACK)        
        self.rect = self.image.get_rect()
        
        self.rect.x = 660
        self.rect.y = 175
       
        self.change_x = 0
        self.change_y = 0   
        
    def changespeed(self, x, y):
       
        self.change_x += x
        self.change_y += y
         
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
                    
        if self.rect.y < 0:
            self.rect.y = 0
            
        if self.rect.y > 340:
            self.rect.y = 340
            
            
                
class Player_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([15, 60])
        self.image.fill(BLACK)        
        self.rect = self.image.get_rect()
        
        self.rect.x = 25
        self.rect.y = 175
       
        self.change_x = 0
        self.change_y = 0   
        
    def changespeed(self, x, y):
       
        self.change_x += x
        self.change_y += y
         
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
                    
        if self.rect.y < 0:
            self.rect.y = 0
            
        if self.rect.y > 340:
            self.rect.y = 340
            
            
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([12, 12])
        self.image.fill(BLACK)        
        self.rect = self.image.get_rect()
        
        self.rect.x = 350
        self.rect.y = 200
        
        self.change_x = random.randrange(1, 5)
        self.change_y = random.randrange(1, 5)
        
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
            
    def update(self):
        self.rect.x = self.rect.x + self.change_x
        self.rect.y = self.rect.y + self.change_y        
        
        if self.rect.x <= 0:
            self.rect.x = 0
            
        if self.rect.x >= 670:
            self.rect.x = 670
                           
        if self.rect.y <= 0:
            self.rect.y = 0
                   
        if self.rect.y >= 385:
            self.rect.y = 385   
            
       
        
pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

 
pygame.display.set_caption("Ryan's Game")

all_sprites_list = pygame.sprite.Group()


player_1 = Player_1()
all_sprites_list.add(player_1)

player_2 = Player_2()
all_sprites_list.add(player_2)

ball = Ball()
all_sprites_list.add(ball)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
 
my_font = pygame.font.SysFont('Times New Roman', 30, True, False)


score = 0
 
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(0, 3)
                         
                               
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(0, -3) 
                
######################################################

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_A:
                player_2.changespeed(0, -3)
            elif event.key == pygame.K_Z:
                player_2.changespeed(0, 3)
                                         
                                               
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_A:
                player_2.changespeed(0, 3)
            elif event.key == pygame.K_Z:
                player_2.changespeed(0, -3)         
            
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    # pygame.draw.rect(screen, BLACK, [25, 175, 15, 60], 0)
    # pygame.draw.rect(screen, BLACK, [660, 200, 15, 60], 0)
    
    pygame.draw.line(screen, BLACK, [350, 700], [350, 0], 3)
    
 
    my_text = my_font.render("Score: " + str(score), True, BLACK)
    screen.blit(my_text, [50, 0])   
    
    my_text = my_font.render("Score: " + str(score), True, BLACK)
    screen.blit(my_text, [550, 0])    
    
    all_sprites_list.update()
    all_sprites_list.draw(screen)    

    # --- Go ahead and update the sceen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()