import pygame
import random
pygame.init()
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode([700,600])
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 151, 48)
lives = 3
level = 2
done = False
clock = pygame.time.Clock()

# CHECKLIST
# noises
class Brick(pygame.sprite.Sprite):
    image = None

    def __init__(self, x, y, image):
        super().__init__()


        self.image = pygame.image.load(image)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)

class Ball(pygame.sprite.Sprite):
    image = None
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 4
        self.change_y = 4
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.top < 0:
            self.rect.top = 0
            self.change_y *= -1
        if self.rect.right > 700:
            self.rect.right = 700
            self.change_x *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.change_x *= -1



class Player(pygame.sprite.Sprite):
    image = None
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([75, 10])
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right > 700:
            self.rect.right = 700
        if self.rect.left < 0:
            self.rect.left = 0

player = Player(50, 50)
player.rect.bottom = 600
player.rect.centerx = 350
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)



paddle_x = 650
paddle_y = 550
paddle_width = 60
paddle_height = 20
paddle_color = [20,180,180]
paddle_speed = 10

myfont = pygame.font.SysFont("Calibri", 22)
score = 0

brick_list = pygame.sprite.Group()
brick1 = Brick(0, 0, "sloth.png")

for x in range(0, screen_width, brick1.rect.width):
    for y in range(50, 1* brick1.rect.height, brick1.rect.height):
        brick = Brick(x, y, "sloth.png")
        brick_list.add(brick)
        all_sprites_list.add(brick)


ball = Ball(50, 450)
all_sprites_list.add(ball)

#game loop
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
        text = my_font.render("Welcome to Brick Breaker: Zoo Escape", True, ORANGE)
        screen.blit(text, [140, 300])
        pygame.display.flip()
        clock.tick(60)

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
        text = my_font.render("Game Over", True, ORANGE)
        screen.blit(text, [290, 300])
        pygame.display.flip()
        clock.tick(60)
def win_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        text = my_font.render("You WIN!!!", True, ORANGE)
        screen.blit(text, [290, 300])
        pygame.display.flip()
        clock.tick(60)


intro_screen()

my_font = pygame.font.SysFont("Calibri", 30, True, False)


background_music = pygame.mixer.Sound("happy.wav")
background_music.set_volume(0.9)
background_music.play(0)
collide_sound = pygame.mixer.Sound("collide.wav")

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-6, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(6, 0)


        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(6, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-6, 0)
          #if len(player) == 27:


    all_sprites_list.update()
    if ball.rect.top > 600:
        lives -= 1
        ball.rect.x = 50
        ball.rect.y = 450
        #reset the ball position
    if lives == -1:
        gameover_screen()
    if score == 27:
        win_screen()
        # take to new level

    #make the screen completely white
    screen.fill(BLACK)



    hit_list =  pygame.sprite.spritecollide(ball, brick_list, True)

    for hit in hit_list:
        score = score + 1
        ball.change_y *= -1
    if pygame.sprite.collide_rect(ball, player):
        ball.rect.bottom = player.rect.top
        ball.change_y *= -1
    if len(brick_list) == 0:
        level += 1
        for x in range(0, screen_width, brick1.rect.width):
            for y in range(50, 1 * brick1.rect.height, brick1.rect.height):
                brick = Brick(x, y, "narwhal.png")
                brick_list.add(brick)
                all_sprites_list.add(brick)
                brick.change_x = 5
                brick.change_y = 5




    #draw everything on the screen
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    score_label = my_font.render("score: " + str(score), 1, pygame.color.THECOLORS['white'])
    screen.blit(score_label, (5, 10))
    all_sprites_list.draw(screen)
    text = my_font.render("lives: " + str(lives), True, WHITE)
    screen.blit(text, [130, 10])


    pygame.display.flip()
    clock.tick(60)
    #update the entire display

pygame.quit()