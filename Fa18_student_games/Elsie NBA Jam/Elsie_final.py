# Levels??!!
# backround music. Lower the sound


"""
pygame base template
Intro computer programming

Elsie Rattner 2018
"""


import pygame
import random


# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
FILL = (98, 103, 209)

pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# games name
pygame.display.set_caption("Cavaliers escape")

score = 0

# key variables
keyx = 0
keyy = 0

# speed variables
speedx = 200
speedy = 200

# position variables
coordx = 323
coordy = 370

timer = 61

# sound recourse
backround_music = pygame.mixer.Sound("Backround.wav")

# play music
backround_music.set_volume(0.5)
backround_music.play(-1)

# loading images
court_image = pygame.image.load("court.jpg")
ball = pygame.image.load("basketball.png")
lebron = pygame.image.load("lebron.png")
simmons = pygame.image.load("Love.png")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


class Net(pygame.sprite.Sprite):
    # Invisible net block for collision

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = 65
        self.rect.y = 240


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # enemy characteristics
        self.x = 0
        self.y = 0
        self.size = 100
        self.image = lebron
        self.speedx = random.choice([-3, -2, -1, 1, 2, 3])
        self.speedy = 1
        self.canguard = 0
        if random.randrange(2) == 0:
            self.image = lebron
        else:
            self.image = simmons
        self.rect = self.image.get_rect()

    def update(self):
        # enemy motion
        self.canguard += 1

        self.rect.x += self.speedx
        if self.rect.right > screen_width/2 - 50 and self.rect.left < screen_width/2 + 50 and self.rect.bottom > screen_height/2 - 50 and self.rect.top < screen_height/2 +50 :
            self.speedx *= -1
            self.rect.x += self.speedx
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.speedx *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx *= -1

        self.rect.y += self.speedy
        if self.rect.right > screen_width/2 - 50 and self.rect.left < screen_width/2 + 50 and self.rect.bottom > screen_height/2 - 50 and self.rect.top < screen_height/2 +50 :
            self.speedy *= -1
            self.rect.y += self.speedy
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.speedy *= -1
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy *= -1


class Player(pygame.sprite.Sprite):
    # player class
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image = ball
        self.rect = self.image.get_rect()
        # vectors
        self.change_x = 0
        self.change_y = 0
        self.rect.center = (screen_width / 2, screen_height / 2)

    def changespeed(self, x, y):
        # change speed of the players wih keys.
        self.change_x += x
        self.change_y += y

    def update(self):
        # new position for a player
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 700 - self.rect.width:
            self.rect.x = 700 - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 500 - self.rect.height:
            self.rect.y = 500 - self.rect.height


# create groups
netgroup = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# create player
player = Player()
all_sprites_group.add(player)
net1 = Net()
net2 = Net()
net2.rect.right = screen_width - net1.rect.x

# dump into groups
netgroup.add(net1)
netgroup.add(net2)
all_sprites_group.update()


# create enemy
for i in range(3):
    enemy = Enemy()
    enemy.rect.x = random.randrange(0, screen_width - enemy.rect.width)
    enemy.rect.bottom = random.randrange(0, screen_width)
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)


def cut_screen():
    # start screen and levels
    frame = 0
    done = False  # Local variable done
    my_font = pygame.font.SysFont("Calibri", 27, True, False)
    while not done:
        frame += 1
        # ----- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        # text on start screen.
        screen.fill(FILL)
        my_text = my_font.render("Welcome to the Cavaliers escape", True, WHITE)
        my_text2 = my_font.render("move the ball with arrow keys into either basket to score ", True, WHITE)
        my_text3 = my_font.render("avoid all players! game gets harder as you go", True, WHITE)
        my_text4 = my_font.render("To win, score at least 10 points before time runs out", True, WHITE)
        my_text5 = my_font.render("Click to continue! good luck", True, WHITE)
        screen.blit(my_text, [190, 100])
        screen.blit(my_text2, [100, 130])
        screen.blit(my_text3, [140, 155])
        screen.blit(my_text4, [110, 185])
        screen.blit(my_text5, [225, 210])
        pygame.display.flip()
        clock.tick(60)


cut_screen()

# -------- Main Program Loop -----------
while not done:
    # ----- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Key movements to control the ball.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:

                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                 player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                 player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                 player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                 player.changespeed(0, -3)

    # font for score
    font = pygame.font.SysFont('Calibri', 75, True, False)
    text = font.render("My text", True, BLACK)

    font1 = pygame.font.SysFont('Calibri', 40, True, False)
    text1 = font.render("My text1", True, BLACK)
    
    # timer
    timer -= 1/60
    
    # ----- Game logic should go here
    all_sprites_group.update()
    if timer <= 0:
            frame = 0
            done = False
            my_font = pygame.font.SysFont("Calibri", 27, True, False)
            while not done:
                # ----- Main event loop
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        done = True

                # text on start screen.
                screen.fill(FILL)
                if score >= 10:
                    my_text = my_font.render("Yay! you won", True, WHITE)
                else:
                    my_text = my_font.render("Boooo, you didn't win.", True, WHITE)
                screen.blit(my_text, [190, 100])

                pygame.display.flip()
                clock.tick(60)

    # ------ collisions
    # player colliding with sprites
    net_hit_list = pygame.sprite.spritecollide(player, netgroup, False,)
    for net in net_hit_list:
        score += 1
        my_sound = pygame.mixer.Sound("swish.wav")
        my_sound.play()
        player.rect.center = (screen_width / 2, screen_height / 2)
        # create enemy
        for i in range(1):
            enemy = Enemy()
            enemy.rect.x = random.choice([0, 5])
            enemy.rect.bottom = random.randrange(0, screen_width)
            all_sprites_group.add(enemy)
            enemy_group.add(enemy)
    # player colliding with enemies
    enemy_hit_list = pygame.sprite.spritecollide(player, enemy_group, False,)
    for enemy in enemy_hit_list:
        if enemy.canguard > 60:
            score -= 1
        enemy.canguard = 0
        player.rect.center = (screen_width / 2, screen_height / 2)
        my_sound1 = pygame.mixer.Sound("hitsound.wav")
        my_sound1.play()


    # ----- Screen-clearing code goes here
    screen.fill(BLACK)
    screen.blit(court_image, [0, 0])

    # ----- Drawing code should go here
    all_sprites_group.draw(screen)

    # draw and print timer
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [0, 450])

    # draw and print time
    text1 = font1.render("Time: " + str(int(timer)), True, BLACK)
    screen.blit(text1, [0, 430])



    # actual movement of keys
    keyx += speedx
    if keyx < 0:
        keyx = 0
    keyy += speedy
    if keyy < 0:
        keyy = 0

    # ----- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # ----- Limit to 60 frames per second
    clock.tick(60)


# Close the window and quit.
pygame.quit()
