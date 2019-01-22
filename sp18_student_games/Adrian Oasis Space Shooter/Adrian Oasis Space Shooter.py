"""
Created by Adrian Bustamante
"""
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 142, 54)
# Lists
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
enemy_bullet_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
# Variables
level = 1
screen_width = 700
screen_height = 500
health = 5
done = False
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("stars.png")                   
# --- Classes
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("badship2.png")
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0
    
        
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x +=self.speedx
        if self.rect.top > screen_height:
            self.rect.bottom = 0
            self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.x += self.speedx
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.speedx *= -1
        if self.rect.left < 0:
            self.rect.left = 0 
            self.speedx *= -1
            
        
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self, x, y):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("ship1.png")
        self.health = 5
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
        self.change_y += 200
    
 
    def update(self):
        """ Update the player's position. """
        
        self.rect.x += self.change_x
        self.rect.y += self.change_y
     
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - 60:
            self.rect.x = screen_width - 60
        if self.rect.y < 0:
            self.rect.y = 0 
           
        if self.rect.y > screen_height - 60:
            self.rect.y = screen_height - 60   
                   
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("laser.png")
       
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 20
        
class EnemyBullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("bad_laser.png")
        #self.image = pygame.Surface([4, 10])
        #self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.centerx = 0
        self.speedy = -10

                   
 
    def update(self):
        """ Move the bullet. """
        self.rect.y += self.speedy


#player.rect.bottom = screen_height # lock player to bottom of screen
all_sprites_list = pygame.sprite.Group() # creates a bucket for all sprites 

block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
# --- Create the window
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen = pygame.display.set_mode([screen_width, screen_height])

 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# Enemies spawn
for a in range(8):
    for b in range(3):
        block = Block(BLUE)
        block.rect.x = a * 80 + 30 
        block.rect.y = b * 75
        all_sprites_list.add(block)
        bad_block_list.add(block)

 
# Creation player block
player = Player(300,0)
player.rect.bottom = screen_height
#all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
clock = pygame.time.Clock()

# outro- screen
def outro_screen():
    done =  False 
    my_font = pygame.font.SysFont("Calibri", 100, True, False)
    my_font2 = pygame.font.SysFont("Calibri", 30, True, False)
    my_font3 = pygame.font.SysFont("Calibri", 70, True, False)
    my_font4 = pygame.font.SysFont("Calibri", 55, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
        screen.fill(BLACK)
        text = my_font.render("You a loser!", True, RED)
        screen.blit(text, [110, 130])
        
        text = my_font4.render("Press green triangle to try again!", True, GREEN)
        screen.blit(text, [0, 30])
        text = my_font4.render("Press green triangle to try again!", True, GREEN)
        screen.blit(text, [0, 430])        
        
        text = my_font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, [170, 200])
        pygame.display.flip()
        clock.tick(60)    

# music
background_music2 = pygame.mixer.Sound("Jingle.wav")
background_music2.set_volume(1.5)
background_music2.play()

        
# intro_screen 
def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 100, True, False)
    my_font2 = pygame.font.SysFont("Calibri", 30, True, False)
    my_font3 = pygame.font.SysFont("Calibri", 70, True, False)
    my_font4 = pygame.font.SysFont("Calibri", 50, True, False)
    
    

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                done = True
        screen.fill(BLACK)
        text = my_font.render("Welcome to Oasis", True, RED)
        screen.blit(text, [5, 0])
  
        text = my_font2.render("There has been a War going on Earth for 22 years.", True, WHITE)
        screen.blit(text, [50, 90])
        
        text = my_font2.render("You are in the middle of a battle when you see a ship.", True, WHITE)
        screen.blit(text, [40, 130])
        
        text = my_font2.render("You get the ship and escape Earth before it explodes.", True, WHITE)
        screen.blit(text, [40, 170])
        
        
        text = my_font2.render("You are cruising in your ship when suddenly...", True, WHITE)
        screen.blit(text, [80, 210])        
        
        text = my_font3.render("Press any key to Begin!", True, WHITE)
        screen.blit(text, [30, 280])
        
        text = my_font4.render("Spacebar = shoot", True, WHITE)
        screen.blit(text, [20, 350])
        
        text = my_font4.render("Use Arrow keys to move", True, WHITE)
        screen.blit(text, [20,410])        
        
        pygame.display.flip()
        clock.tick(60)    
 
# Used to manage how fast the screen updates

intro_screen()
#background_image = pygame.image.load("space")
my_font = pygame.font.SysFont('Calibri', 45, True, False) 

#background_image = pygame.image.load("strike.bmp")
#player.rect.y = 370
score = 0
background_music2 = pygame.mixer.Sound("Mars.wav")
background_music2.set_volume(0.3)
background_music2.play(-1)
laser_sound = pygame.mixer.Sound("laser_shooting.wav")
laser_sound.set_volume(0.1)

#hit_music = pygame.mixer.Sound("Hit.mp3")
hit_music = pygame.mixer.Sound("hit.wav")
hit_music.set_volume(27)
damage_music = pygame.mixer.Sound("damage.wav")



# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:   
                bullet = Bullet()
                bullet.rect.centerx = player.rect.centerx
                bullet.rect.centery = player.rect.centery
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                laser_sound.play()
            elif event.key == pygame.K_LEFT:
                player.changespeed(-6, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(6, 0)
                            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(6, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-6, 0)
                 
   
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
    
    # Calculate mechanics for each bullet
    for enemybullet in enemy_bullet_list:
        player_hit_list = pygame.sprite.spritecollide(enemy_bullet, player_list, True)
        for player in player_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            hit_music.play()
            health -= 1
            print(score)        
    for enemybullet in enemy_bullet_list:
        if pygame.sprite.collide_rect(player, enemybullet):
            enemy_bullet_list.remove(enemybullet)
            all_sprites_list.remove(enemybullet)
            hit_music.play()
            player.health -= 1
            
    for enemy in bad_block_list:
        if random.randrange(420) == 0:
            enemy_bullet = EnemyBullet()
            all_sprites_list.add(enemy_bullet)
            enemy_bullet_list.add(enemy_bullet)
            enemy_bullet.rect.center = enemy.rect.center   
            enemy_bullet.speedy = 6 + enemy.speedy
            
    
    for bullet in bullet_list:
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, bad_block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            
            
        # Levels
    if len(bad_block_list) == 0:
        level += 1 
             
        if level > 1:
            for a in range(8):
                for b in range(3):
                    block = Block(BLUE)
                    block.rect.x = a * 80 + 30 
                    block.rect.y = b * 75
                    all_sprites_list.add(block)
                    bad_block_list.add(block)
                    block.speedy = level + 3
                    enemybullet.rect.y = level + 3
                
                      
                    for enemy in bad_block_list:
                        if random.randrange(420) == 0:
                            enemy_bullet = EnemyBullet()
                            all_sprites_list.add(enemy_bullet)
                            enemy_bullet_list.add(enemy_bullet)
                            enemy_bullet.rect.center = enemy.rect.center   
                            enemy_bullet.speedy = 6 + enemy.speedy
                            
           
                     
            
                              
            
            
        
        
        # new enemies that move faster and are cooler
        
        
    
    all_sprites_list.draw(screen)
    
    # --- Draw a frame
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
    player_hit_list = pygame.sprite.spritecollide(block, player_list, True)
    #enemy_bullet_list = pygame.sprite.spritecollide(block, player_list, True)
    
    
    for block in bad_blocks_hit_list:
        player.health -= 1
        damage_music = pygame.mixer.Sound("damage.wav")
        damage_music.set_volume(0.5)
        damage_music.play()        
        print(score)
        
        
        
    
        
    # Check the list of collisions.
 
    # Health
    if player.health <= 0:   
        done = True
        background_music2 = pygame.mixer.Sound("out.wav")
        background_music2.set_volume(1.5)
        background_music2.play()
        
        outro_screen()     
        
        
    # Draw all the spites
    screen.blit(background_image, [0,0])
    my_text = my_font.render("Score: " + str(score), True, WHITE)
    screen.blit(my_text, [10,10]) 
    my_text = my_font.render("Health:" + str(player.health), True, WHITE)
    screen.blit(my_text, [10,50]) 
    my_text = my_font.render("Level:" + str(level), True, WHITE)
    screen.blit(my_text, [10,90])     
    
    all_sprites_list.draw(screen)
    all_sprites_list.draw(screen)
    all_sprites_list.draw(screen)
    all_sprites_list.draw(screen)
    
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
#outro_screen()
pygame.quit()
