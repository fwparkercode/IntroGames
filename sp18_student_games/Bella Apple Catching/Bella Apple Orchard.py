# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

# Set the height and width of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("FINAL")
all_sprites_list = pygame.sprite.Group()


#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Global Variables
score = 0
level = 1
lives = 5



#Classes
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("download.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 700 - self.rect.width:
            self.rect.x = 700 - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 400 - self.rect.height:
            self.rect.y = 400 - self.rect.height
            
    

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface([30, 30])
        #self.image.fill(RED)
        self.image = pygame.image.load("download copy.png")
        self.rect = self.image.get_rect()
        self.speedx = random.randrange(-6, 7)
        self.speedy = 3
    def update(self):
        self.rect.y += self.speedy
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
            
class Bad_Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface([30, 30])
        #self.image.fill(RED)
        self.image = pygame.image.load("images-2.png")
        self.rect = self.image.get_rect()
        self.speedx = random.randrange(-6, 7)
        self.speedy = 3
    def update(self):
        self.rect.y += self.speedy
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
    
    
class Power_Up(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("download copy 3.png")
        self.rect = self.image.get_rect()
        self.speedx = random.randrange(-6, 7)
        self.speedy = 3
    def update(self):
        self.rect.y += self.speedy
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
            
power_up_list = pygame.sprite.Group()
for i in range(1):
    power_up = Power_Up()
    power_up.rect.x = random.randrange(0, screen_width - power_up.rect.width)
    power_up.rect.y = random.randrange(-screen_height - power_up.rect.height,0)
    power_up_list.add(power_up)
    all_sprites_list.add(power_up)    
    
bad_apple_list = pygame.sprite.Group()
for i in range(2):
    bad_apple = Bad_Apple()
    bad_apple.rect.x = random.randrange(0, screen_width - bad_apple.rect.width)
    bad_apple.rect.y = random.randrange(-screen_height - bad_apple.rect.height,0)
    bad_apple_list.add(bad_apple)
    all_sprites_list.add(bad_apple)
    
    
player = Player(300,300)
all_sprites_list.add(player)

apple_list = pygame.sprite.Group()
for i in range(10):
    apple = Apple()
    apple.rect.x = random.randrange(0, screen_width - apple.rect.width)
    apple.rect.y = random.randrange(-screen_height - apple.rect.height, 0)    
    apple_list.add(apple)
    all_sprites_list.add(apple)
 
 
    
# Image resources
background_image = pygame.image.load("orchard2.jpg")
background_music = pygame.mixer.Sound("01 Cotton-Eyed Joe.wav")
background_music.set_volume(4)
background_music.set_volume(1)
background_music.play()
my_sound = pygame.mixer.Sound("powerup.wav")
my_sound.set_volume(100)
bad_apple_music = pygame.mixer.Sound("rock_breaking.wav")




score = 0
key_x = 0
key_y = 0
speed_x = 0
speed_y= 0

# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 25, True, False)
text = font.render("My text",True,BLACK)



def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        text = my_font.render("WELCOME TO APPLE CATCH!", True, WHITE)
        text2 = my_font.render("Catch the good apples and avoid the worm ones!", True, WHITE)
        text3 = my_font.render("Use the arrow keys to control the basket.", True, WHITE)
        text4 = my_font.render("Press the mouse button to begin!", True, WHITE)
        screen.blit(text4,[120, 310])
        screen.blit(text, [140, 250])
        screen.blit(text2,[40, 270])
        screen.blit(text3,[85, 290])
        pygame.display.flip()
        clock.tick(60)
        
        
def outro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        text = my_font.render("YOU DIED!", True, WHITE)
        text2 = my_font.render("THANKS FOR PLAYING.", True, WHITE)
        screen.blit(text, [270, 250])
        screen.blit(text2,[200, 270])
        pygame.display.flip()
        clock.tick(60)


# Start the intro screen loop before the main loop
intro_screen()


 


# Game loop
while not done:
 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.changespeed(-15, 0)
                    elif event.key == pygame.K_RIGHT:
                        player.changespeed(15, 0)
                    elif event.key == pygame.K_UP:
                        player.changespeed(0, -15)
                    elif event.key == pygame.K_DOWN:
                        player.changespeed(0, 15)
         
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.changespeed(15, 0)
                    elif event.key == pygame.K_RIGHT:
                        player.changespeed(-15, 0)
                    elif event.key == pygame.K_UP:
                        player.changespeed(0, 15)
                    elif event.key == pygame.K_DOWN:
                        player.changespeed(0, -15)        
        
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
    #x, y= pygame.mouse.get_pos()
    
    hit_list = pygame.sprite.spritecollide(player, apple_list, True)
    for apple in hit_list:
        score += 1
        print(score)
        
        
    hit_list = pygame.sprite.spritecollide(player, bad_apple_list, True)
    for bad_apple in hit_list:
        lives -= 1
        print(lives)
        bad_apple_music.play()
        
    hit_list = pygame.sprite.spritecollide(player, power_up_list, True)
    for power_up in hit_list:
        lives += 1
        print(lives)
        my_sound.play()
                 
    
    if len(apple_list) == 0:
        level += 1
        for i in range(level * 10):
            apple = Apple()
            apple.speedy = level * 2
            apple.rect.x = random.randrange(0, screen_width - apple.rect.width)
            apple.rect.y = random.randrange(-screen_height - apple.rect.height, 0)    
            apple_list.add(apple)
            all_sprites_list.add(apple)   
            
        for i in range(level * 2):
            bad_apple = Bad_Apple()
            bad_apple.speedy = level * 2
            bad_apple.rect.x = random.randrange(0, screen_width - bad_apple.rect.width)
            bad_apple.rect.y = random.randrange(-screen_height - bad_apple.rect.height, 0)    
            bad_apple_list.add(bad_apple)
            all_sprites_list.add(bad_apple) 
            
        for i in range(level * 2):
            power_up = Power_Up()
            power_up.speedy = level * 1
            power_up.rect.x = random.randrange(0, screen_width - power_up.rect.width)
            power_up.rect.y = random.randrange(-screen_height - power_up.rect.height, 0)    
            power_up_list.add(power_up)
            all_sprites_list.add(power_up)             
            
    if (lives) == 0:
        done = True
        outro_screen()
    
      
    all_sprites_list.update()
    # Clear the screen and set the screen background
    screen.fill(BLACK)
    
    # Blit images here (blit background first!)
    screen.blit(background_image, [0, 0])
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [0, 0])    
    text = font.render("Level:" + str(level), True, BLACK)
    screen.blit(text, [0, 25])
    text = font.render("Lives:" + str(lives), True, BLACK)
    screen.blit(text, [0, 50])    
    
    all_sprites_list.draw(screen)
    
    # Render the score text
    # Increasing score up to 1000... let's add this
    # Put the image of the text on the screen at 250x250
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
     
 
# Be IDLE friendly
pygame.quit()