"""
Octavio Lopez

My first game
"""

import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (40, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Space Wars")
 
# Loop until the user clicks the close button.
done = False
score = 0
level = 1
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.health = 3
        self.rect = self.image.get_rect()
        self.triple = False
        self.powerup = 200                        
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 3
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > screen_height:
            self.rect.bottom = 0
          
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("asteroid.png")
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
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.speedy = -8
        self.speedx = 0
        self.powerup = 200
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
class Enemybullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speedy = 8
        self.speedx = 0
        self.powerup = 200
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
               

# Creates the user sprite            
player = Player()

# Groups
all_sprites_list = pygame.sprite.Group() # create a bucket for all sprites
all_sprites_list.add(player)
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
power_list = pygame.sprite.Group()
asteroid_list = pygame.sprite.Group()
enemybullet_list = pygame.sprite.Group()

# Variable that helps determine the conclusion of the game
screen_choice = 0

# Formation of the Enemies
heighte = 4
widthe = 12

horizontal_spacing = 50
vertical_spacing = -40

for h in range(widthe):
    for g in range(heighte):
        enemy = Enemy()
        enemy.rect.x = h * horizontal_spacing + 100 
        enemy.rect.y = g * vertical_spacing
        all_sprites_list.add(enemy)
        enemy_list.add(enemy)

# Font for keeping track of the score, level, lives
my_font = pygame.font.SysFont('americantypewrite', 18, False, False)

# Star list for intro screen
star_list = []

for i in range(150): 
    x = random.randrange(700)
    y = random.randrange(500)
    speed = random.random() * 2 + 0.5
    star_list.append([x, y, speed])

# Intro Screen Function
def intro_screen():
    done = False
    my_font_intro = pygame.font.SysFont("americantypewrite", 70, True, False)
    my_font_intro2 = pygame.font.SysFont("americantypewrite", 30, True, False)
    my_font_intro3 = pygame.font.SysFont("americantypewrite", 25, True, False)
    my_font_intro4 = pygame.font.SysFont("americantypewrite", 60, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        
        for i in range(len(star_list)):
            star_list[i][1] += star_list[i][2]
            if star_list[i][1] > 500:
                star_list[i][1] = -5
            pygame.draw.ellipse(screen, WHITE, [star_list[i][0], star_list[i][1], 3, 3])         
        
        text_title = my_font_intro.render("Welcome to Space Wars!", True, GREEN)
        text_instructions = my_font_intro2.render("Kill the enemies before they kill you.", True, GREEN)
        text_controls = my_font_intro3.render("Use the mousepad to move and click the mousepad to shoot.", True, GREEN)
        text_start = my_font_intro4.render("Click the mousepad to start.", True, GREEN)
        screen.blit(text_title, [15, 30])
        screen.blit(text_instructions, [120, 130])
        screen.blit(text_controls, [80, 200])
        screen.blit(text_start, [15, 290])
                
               
        
        pygame.display.flip()
        clock.tick(60)


# Activates the background music
background_sound = pygame.mixer.Sound("background.wav")
background_sound.set_volume(1)
background_sound.play(-1)

# Intro screen loop before the main loop
intro_screen()

# Background image
bgd_image = pygame.image.load("background.png")

# Noises for shooting and collisions
explosion_sound = pygame.mixer.Sound("explosion.wav")
laser_sound = pygame.mixer.Sound("lasershot.wav")
enemy_laser_sound = pygame.mixer.Sound("enemylaser.wav")


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Clicking the mousebutton to shoot
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.centerx = player.rect.centerx
            bullet.rect.centery = player.rect.centery
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            laser_sound.play()
        
        # Triple bullets for when the user catches the bullet box
        if player.triple == True and event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.centerx = player.rect.centerx
            bullet.rect.centery = player.rect.centery
            bullet.speedx = 2
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            bullet = Bullet()
            bullet.rect.centerx = player.rect.centerx
            bullet.rect.centery = player.rect.centery
            bullet.speedx = -2
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            laser_sound.play()
         
    
    # This rids the user's arrow only for when they are actually playing the game
    pygame.mouse.set_visible(False)
    
    # --- Game logic should go here
    
    # The user sprite follow the user's movement on the mousepad
    x, y = pygame.mouse.get_pos()
    player.rect.centerx = x
    player.rect.centery = y
    
    # Updates lists
    enemy_list.update()
    bullet_list.update()
    power_list.update()
    asteroid_list.update()
    enemybullet_list.update()
    
    # For when an enemy bullet collides with the user
    for enemybullet in enemybullet_list:
        if pygame.sprite.collide_rect(player, enemybullet):
            enemybullet_list.remove(enemybullet)
            all_sprites_list.remove(enemybullet)
            player.health -= 1
            explosion_sound.play() 
    
    # This creates bullets for the enemy
    for enemy in enemy_list:
        if random.randrange(500) == 0:
            enemybullet = Enemybullet()
            enemybullet.rect.centerx = enemy.rect.centerx
            enemybullet.rect.centery = enemy.rect.centery
            all_sprites_list.add(enemybullet)
            enemybullet_list.add(enemybullet)
            enemy_laser_sound.play()    
    
    # Lists for collisions
    hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
    asteroid_hit_list = pygame.sprite.spritecollide(player, asteroid_list, False)
    
    
    # When an enemy collides with the user
    for enemy in hit_list:
        enemy_list.remove(enemy)
        all_sprites_list.remove(enemy)        
        player.health -= 1
        explosion_sound.play()
    
    # When an asteroid collides with the user
    for asteroid in asteroid_hit_list:
        asteroid_list.remove(asteroid)
        all_sprites_list.remove(asteroid)        
        player.health -= 1 
        explosion_sound.play()
    
    # This ends the game if the user has no health left
    if player.health <= 0:
        done = True
        screen_choice += 1
        
    # Determines if bullets collide with an enemy or asteriod 
    for bullet in bullet_list:
        # List for collision
        bullet_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        asteroid_bullet_hit_list = pygame.sprite.spritecollide(bullet, asteroid_list, True)
        
        # For each enemy or asteroid the bullet collides with, remove the bullet and add to the score
        for enemy in bullet_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            explosion_sound.play()
        for asteroid in asteroid_bullet_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            explosion_sound.play()
        
    # List for collision between the user and the power up box (bullet box)
    power_hit_list = pygame.sprite.spritecollide(player, power_list, False)
    
    # Creates new levels if there are no enemies
    if len(enemy_list) == 0:
        level += 1
        # New enemies that move faster for each new level
        for h in range(widthe):
            for g in range(heighte):
                enemy = Enemy()
                enemy.speedy = level * 2
                enemy.rect.x = h * horizontal_spacing + 100
                enemy.rect.y = g * vertical_spacing
                all_sprites_list.add(enemy)
                enemy_list.add(enemy)
        # Bullet box (power up) falls down for the user to collide with for triple bullets
        if level == 2:
            power_bullet = Enemy()
            power_bullet.image = pygame.image.load("bullets.png")
            power_bullet.rect.x = 20
            power_bullet.rect.y = -10
            all_sprites_list.add(power_bullet)
            power_list.add(power_bullet)
        # Asteroids that fall down the screen randomly    
        if level == 3:
            for i in range(15):
                asteroid = Asteroid()
                asteroid.rect.x = random.randrange(0, screen_width - asteroid.rect.width)
                asteroid.rect.y = random.randrange(-screen_height - asteroid.rect.height, 0)
                all_sprites_list.add(asteroid)
                asteroid_list.add(asteroid)   
            
    # Removes the bullet box (power up) sprite if the user collides with it and the user gets triple bullets          
    for power_bullet in power_hit_list:
        power_list.remove(power_bullet)
        all_sprites_list.remove(power_bullet)        
        player.triple = True
                
    # Ends the game if the user gets to the fourth level
    if level == 4:
        done = True
        screen_choice += 2       
            
        
    # For the background image
    screen.fill(WHITE)
    screen.blit(bgd_image, [0,0])
    
    
    # Creates text in the upper left hand corner of the screen for level, score, and heatlh
    my_text_level = my_font.render("Level: " + str(level), True, WHITE)            
    my_text_score = my_font.render("Score: " + str(score), True, WHITE)
    my_text_health = my_font.render("Lives: " + str(player.health), True, WHITE)            
    screen.blit(my_text_level, [10, 10])
    screen.blit(my_text_score, [10, 30])
    screen.blit(my_text_health, [10, 50])
             
    # Puts the sprites on the screen
    all_sprites_list.draw(screen)
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 

# Makes the mouse visible for the user to exit the game
pygame.mouse.set_visible(True)


# Background stars for the exit screen
star_list_lose = []

for i in range(150): 
    x_lose = random.randrange(700)
    y_lose = random.randrange(500)
    speed_lose = random.random() * 2 + 0.5
    star_list_lose.append([x_lose, y_lose, speed_lose])

# Exit screen if the user loses
def lose_screen():
    done = False
    my_font_lose = pygame.font.SysFont("americantypewrite", 100, True, False)
    my_font_lose2 = pygame.font.SysFont("americantypewrite", 60, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        
        for i in range(len(star_list_lose)):
            star_list_lose[i][1] += star_list_lose[i][2]
            if star_list_lose[i][1] > 500:
                star_list_lose[i][1] = -5
            pygame.draw.ellipse(screen, WHITE, [star_list_lose[i][0], star_list_lose[i][1], 3, 3])        
        
        text_lose = my_font_lose.render("You Lose!", True, RED)
        text_lose2 = my_font_lose2.render("Click the mousepad to exit.", True, RED)
        screen.blit(text_lose, [150, 50])
        screen.blit(text_lose2, [15, 250])       
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# Exit screen if the user wins
def win_screen():
    done = False
    my_font_win = pygame.font.SysFont("americantypewrite", 100, True, False)
    my_font_win2 = pygame.font.SysFont("americantypewrite", 60, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        
        for i in range(len(star_list_lose)):
            star_list_lose[i][1] += star_list_lose[i][2]
            if star_list_lose[i][1] > 500:
                star_list_lose[i][1] = -5
            pygame.draw.ellipse(screen, WHITE, [star_list_lose[i][0], star_list_lose[i][1], 3, 3])         
        
        text_win = my_font_win.render("You Win!", True, YELLOW)
        text_win2 = my_font_win2.render("Click the mousepad to exit.", True, YELLOW)
        screen.blit(text_win, [150, 50])
        screen.blit(text_win2, [15, 250])
                       
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


# If the user loses
if screen_choice == 1:
    lose_screen()
# If the user wins
if screen_choice == 2:
    win_screen()
# If the user loses
if screen_choice == 3:
    lose_screen()
    
pygame.quit()