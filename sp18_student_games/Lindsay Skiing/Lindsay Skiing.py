import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)     # defining colors

first_screen = pygame.image.load("IntroScreen.jpg")
main_screen = pygame.image.load("snow.png")
end_game = pygame.image.load("gameover.jpg") # screen images go here
lives = 5
level = 1
background_y = 1
frame = 0       # game variables here

pygame.init()

screen_width = 700
screen_height = 525
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)      # setting up the screen
pygame.display.set_caption('Final Project')

background_music = pygame.mixer.Sound("backgroundmusic.wav")
background_music.set_volume(0.5)
background_music.play(-1)       # all sound here
bump_sound = pygame.mixer.Sound("bump.wav")

my_font = pygame.font.SysFont('Times New Roman', 25, True, False) # setting my font

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("skierleft.png")
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.changespeedx = 0
    def update(self):
        self.change_x = 0
        self.change_y = 0
        self.rect.left += self.changespeedx
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 700:
            self.rect.right = 700
        if player.changespeedx > 0:
            player.image = pygame.image.load("skierright.png")  
        if player.changespeedx < 0:
            player.image = pygame.image.load("skierleft.png")
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y          # player created here –– this is the first class

class Skier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("otherskierleft.png")
        self.rect = self.image.get_rect()
        self.changespeedx = random.randrange(-4, 5)
    def update(self):
        self.rect.left += self.changespeedx
        self.rect.top -= level
        if self.rect.left <= 0:
            self.rect.left = 0
            self.changespeedx *= -1
            self.image = pygame.image.load("otherskierright.png")
        if self.rect.left >= 670:
            self.rect.left = 670
            self.changespeedx *= -1
            self.image = pygame.image.load("otherskierleft.png")
        if self.rect.top <= -30:
            self.rect.top = 525     # first 'obstacle' class

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tree.png")
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.top -= level
        if self.rect.top <= -50:
            self.rect.top = 525        # another obstacle

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rock.png")
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.top -= level
        if self.rect.top <= -30:
            self.rect.top = 525      # our third and final obstacle!!
            
all_sprites_list = pygame.sprite.Group()
bad_sprites_list = pygame.sprite.Group() # groups created here

for i in range(2):       # creates 2 of each 'obstacle' sprite at the beginning of the game
    tree = Tree()
    tree.rect.left = random.randrange(670)
    tree.rect.top = random.randrange(525)    
    all_sprites_list.add(tree)
    bad_sprites_list.add(tree)     
    rock = Rock()
    rock.rect.left = random.randrange(670)
    rock.rect.top = random.randrange(525)
    all_sprites_list.add(rock)  
    bad_sprites_list.add(rock)
    other_skier = Skier()
    other_skier.rect.left = random.randrange(670)
    other_skier.rect.top = random.randrange(525)
    all_sprites_list.add(other_skier)
    bad_sprites_list.add(other_skier)

def level_up(level):             # the level-up function creates additional obstacle sprites
    for i in range(3):
        tree = Tree()
        tree.rect.left = random.randrange(670)
        tree.rect.top = random.randrange(525, 1050)    
        all_sprites_list.add(tree)
        bad_sprites_list.add(tree)
    
    for i in range (2):
        rock = Rock()
        rock.rect.left = random.randrange(670)
        rock.rect.top = random.randrange(525, 1050)
        all_sprites_list.add(rock)  
        bad_sprites_list.add(rock)
    
    for i in range(4):
        other_skier = Skier()
        other_skier.rect.left = random.randrange(670)
        other_skier.rect.top = random.randrange(525, 1050)
        all_sprites_list.add(other_skier)
        bad_sprites_list.add(other_skier)
        
player = Player(350, 235)
all_sprites_list.add(player)    # creates the player last 

def intro_screen():     # intro screen function
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True                  
            screen.blit(first_screen,[0, 0])
            my_text = my_font.render("Welcome to Ski Adventure! Press the space bar to begin.", True, BLACK)
            screen.blit(my_text,[25, 440])
            pygame.display.flip()
            clock.tick(60)
            
def game_over():        # game over screen function
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)
        screen.blit(end_game,[0, -75])        
        my_text1 = my_font.render("Game over.", True, WHITE)       
        my_text2 = my_font.render("You reached level " + str(level) + ".", True, WHITE)
        screen.blit(my_text1,[280, 440])
        screen.blit(my_text2,[235, 475])
        pygame.display.flip()
        clock.tick(60)        

pygame.display.set_caption("Final Project")

done = False

clock = pygame.time.Clock()
intro_screen()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeedx -= 1
            elif event.key == pygame.K_RIGHT:
                player.changespeedx += 1

    all_sprites_list.update()
    
    screen.fill(WHITE)

    background_y -= level
    if background_y < -main_screen.get_height():
        background_y = 0
        x = 0

    for x in range(0, screen_width, main_screen.get_width()):
        for y in range(-500, screen_height, main_screen.get_height()):
            screen.blit(main_screen, [x, y + background_y])

    all_sprites_list.draw(screen)

    my_text1 = my_font.render("Level: " + str(level), True, BLACK)
    my_text2 = my_font.render("Lives remaining: " + str(lives), True, BLACK)
    screen.blit(my_text1,[5, 490])
    screen.blit(my_text2,[490, 490]) 
    
    hit_list = pygame.sprite.spritecollide(player, bad_sprites_list, True)   
    for sprite in hit_list:
        bump_sound.play(0)
        lives -= 1
        if lives <= 0:
            game_over()
            done = True
    
    if frame % 600 == 0 and frame > 0:
        level += 1
        level_up(level)
        
    frame += 1
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# add a bump sound?