import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
pygame.init()

bonus = False

background_music = pygame.mixer.Sound("backgroundmusic.wav")
background_music.set_volume(1.0)
background_music.play(-1)

screen_width = 700
screen_height = 500

shooting_sound = pygame.mixer.Sound("laser.wav")
powerup_sound = pygame.mixer.Sound("powerup_sound.wav")

size = (screen_width, screen_height) 
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
level = 1
done = False
 

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.health = 5
        self.triple = False
        self.powerup = 200
        
 
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if random.randrange(2) == 0:
            self.image = pygame.image.load("enemy2.png")
        else:
            self.image = pygame.image.load("enemy1.png")
        self.rect = self.image.get_rect()
        self.speedx = random.randrange(-6, 7)
        self.speedy = 2
        self.width = random.randrange(10, 200)
        self.center = random.randrange(100, 600)
        self.freq = random.randrange(5, 100)
    def update(self):
        self.rect.y += self.speedy
        self.rect.y += 1
        self.rect.x = self.center + math.sin(self.rect.y/self.freq) * self.width
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
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.speedy = -8
        self.speedx = 1
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        


class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("powerup.png")
        self.rect = self.image.get_rect()
        self.speedx = random.randrange(-6, 7)
        self.speedy = 2
    def update(self):
        self.rect.y += self.speedy
        self.rect.y += 1  
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


player = Player()
player.rect.bottom = screen_height # lock player to the bottom of screen
all_sprites_list = pygame.sprite.Group() # created a bucket for all sprites
all_sprites_list.add(player)


enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
powerup_list = pygame.sprite.Group()

# Enemy placement
for i in range(4):
    enemy = Enemy()
    enemy.rect.x = random.randrange(0, screen_width - enemy.rect.width)
    enemy.rect.y = random.randrange(-screen_height - enemy.rect.height, 0)
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)


#Stars
snow_list = []
for i in range(500):
    starx = random.randrange(700)
    stary = random.randrange(750)
    speed = random.random()
    snow_list.append([starx, stary, speed])


# Intro Screen 
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
        for i in range(len(snow_list)):
            snow_list[i][1] += snow_list[i][2]
            if snow_list[i][1] > 650:
                snow_list[i][1] = -4
            pygame.draw.ellipse(screen, WHITE, [snow_list[i][0], snow_list[i][1], 1, 1])
            
        text = my_font.render("Hello Welcome to Galaga!", True, WHITE)
        text2 = my_font.render("Use the space bar to shoot the enemies. Press to play!", True, WHITE)
        text15 = my_font.render("Try and grab lightning bolts for powerups!", True, WHITE)
        screen.blit(text, [200, 200])
        screen.blit(text2, [50, 300])
        screen.blit(text15, [90, 350])
        pygame.display.flip()
        clock.tick(60)
        
intro_screen()

# Game Over Screen
def game_over():
    done = False
    my_font2 = pygame.font.SysFont("Calibri", 30, True, False)
    my_font11 = pygame.font.SysFont("Calibri", 30, True, False)
    my_font12 = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(RED)
        text3 = my_font2.render("GAME OVER", True, BLACK)
        text16 = my_font2.render("YOU LOST ALL YOUR LIVES", True, BLACK)
        text11 = my_font11.render("final score =", True, BLACK)
        text12 = my_font12.render(str(score), True, BLACK)
        screen.blit(text3, [275, 200])
        screen.blit(text11, [220, 250])
        screen.blit(text12, [380, 250])
        screen.blit(text16, [200, 150])
        pygame.display.flip()
        clock.tick(60)

def bonus_screen():
    done = False
    bullet_list.empty()
    all_sprites_list.empty()
    all_sprites_list.add(player)    
    countdown = 200
    my_font6 = pygame.font.SysFont("Calibri", 30, True, False)
    my_font7 = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)
        for i in range(len(snow_list)):
            snow_list[i][1] += snow_list[i][2]
            if snow_list[i][1] > 650:
                snow_list[i][1] = -4
            pygame.draw.ellipse(screen, WHITE, [snow_list[i][0], snow_list[i][1], 1, 1])
        countdown -= 1
        if countdown <= 0:
            done = True
        text6 = my_font6.render("Bonus Round!!!", True, WHITE)
        text7 = my_font7.render("You have 5 seconds to collect as many points as possible!", True, WHITE)
        screen.blit(text7, [5, 270])
        screen.blit(text6, [275, 200])
        pygame.display.flip()
        clock.tick(60)
        
                

#You win Screen
def win_screen():
    done = False
    bonus = False
    bullet_list.empty()
    all_sprites_list.empty()
    my_font8 = pygame.font.SysFont("Calibri", 30, True, False)
    my_font9 = pygame.font.SysFont("Calibri", 30, True, False)
    my_font10 = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)
        for i in range(len(snow_list)):
            snow_list[i][1] += snow_list[i][2]
            if snow_list[i][1] > 650:
                snow_list[i][1] = -4
            pygame.draw.ellipse(screen, WHITE, [snow_list[i][0], snow_list[i][1], 1, 1])        
        text8 = my_font8.render("Thanks for playing! You won!", True, RED)
        text9 = my_font9.render("Your final score =", True, WHITE)
        text10 = my_font10.render(str(score), True, RED)
        screen.blit(text8, [180, 200])
        screen.blit(text9, [200, 250])
        screen.blit(text10, [425, 250])
        pygame.display.flip()
        clock.tick(60)



# Level Screens
def level_screen():
    done = False
    bonus = False
    countdown = 200
    bullet_list.empty()
    player.triple = False
    all_sprites_list.empty()
    all_sprites_list.add(player)
    my_font5 = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)
        countdown -= 1
        if countdown < 0:
            done = True
        for i in range(len(snow_list)):
            snow_list[i][1] += snow_list[i][2]
            if snow_list[i][1] > 650:
                snow_list[i][1] = -4
            pygame.draw.ellipse(screen, WHITE, [snow_list[i][0], snow_list[i][1], 1, 1])
        text4 = my_font5.render("level", True, WHITE)
        text5 = my_font5.render(str(level + 1), True, WHITE)
        screen.blit(text4, [300, 200])
        screen.blit(text5, [325, 225])
        pygame.display.flip()
        clock.tick(60)


            


my_font3 = pygame.font.SysFont("Calibri", 30, True, False)
score = 0 

health_image = pygame.image.load("littleplayer.png")
countdown2 = 300

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet()
                bullet.rect.centerx = player.rect.centerx
                bullet.rect.centery = player.rect.centery
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                if player.triple == True:
                    bullet = Bullet()
                    bullet.speedx = 1
                    bullet.rect.centerx = player.rect.centerx
                    bullet.rect.centery = player.rect.centery
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                    bullet = Bullet()
                    bullet.speedx = -1
                    bullet.rect.centerx = player.rect.centerx
                    bullet.rect.centery = player.rect.centery
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                    bullet = Bullet()
                    bullet.speedx = 2
                    bullet.rect.centerx = player.rect.centerx
                    bullet.rect.centery = player.rect.centery
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)                                        
                    
        
    
    x, y = pygame.mouse.get_pos()
    player.rect.centerx = x
    # player.rect.centery = y #lock to bottom so stop updating
    
    enemy_list.update()
    bullet_list.update()
    powerup_list.update()
    
    
    # Power Up
    p0werup_list = pygame.sprite.spritecollide(player, powerup_list, True)
    for powerup in p0werup_list:
        if random.randrange(2) == 0:
            player.triple = True
        else:
            player.health += 1       

        powerup_sound.play()
        
    
    # When enemy hits player
    hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
    
    if not bonus:
        for enemy in hit_list:
            enemy.rect.y = -enemy.rect.height
            player.health -= 1
            score -= 300
            print(score)
            if player.health <= 0:
                game_over()
                done = True
    
    
    # When bullet hits enemy     
    for bullet in bullet_list:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        for enemy in hit_list:
            score += 200
            shooting_sound.play()
            bullet.kill()
            print(score)
    
    
    # If you kill all enemies    
    if len(enemy_list) == 0:
        if level == 7:
            bonus = True
            bonus_screen()
            level += 1
        else:
            level_screen()
            level += 1
            player.triple = False
        
        # Powerup   
        if not bonus:
            if level >= 4:
                powerup = Powerup()
                all_sprites_list.add(powerup)
                powerup_list.add(powerup)
                
            # Amount of enemies per level            
            for i in range(level + 6):
                enemy = Enemy()
                enemy.speedy = level * 2 - 2
                enemy.rect.x = random.randrange(0, screen_width - enemy.rect.width)
                enemy.rect.y = random.randrange(-screen_height - enemy.rect.height, 0)
                all_sprites_list.add(enemy)
                enemy_list.add(enemy)
                if level >= 5:
                    enemy.speedy = level + 2
        else:
            countdown2 = 300
            for i in range(140):
                enemy = Enemy()
                enemy.speedy = random.randrange(4, 6)
                enemy.rect.x = random.randrange(0, screen_width - enemy.rect.width)
                enemy.rect.y = random.randrange(-screen_height - enemy.rect.height, 0)
                all_sprites_list.add(enemy)
                enemy_list.add(enemy)
                
                
            
    countdown2 -= 1
    print(countdown2)
    if countdown2 < 0 and bonus:
        bonus = False
        win_screen()
            
     
    screen.fill(BLACK)
    
    # Drawing little players
    for i in range(player.health):
        screen.blit(health_image, [20 * i, 30]) 
        
    
    #Star background
    for i in range(len(snow_list)):
        snow_list[i][1] += snow_list[i][2]
        if snow_list[i][1] > 650:
            snow_list[i][1] = -4
        pygame.draw.ellipse(screen, WHITE, [snow_list[i][0], snow_list[i][1], 1, 1])
    
    all_sprites_list.draw(screen)
    
    # Score draw
    my_text = my_font3.render("PLYR1= " + str(score), True, WHITE)
    screen.blit(my_text, [0,0])    
 
    
    pygame.display.flip()
 
    
    clock.tick(60)
 

pygame.quit()
