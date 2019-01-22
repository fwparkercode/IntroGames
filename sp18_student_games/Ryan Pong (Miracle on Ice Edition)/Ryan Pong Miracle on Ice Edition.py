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
BLUE = (66, 78, 244)
frame = 0

score_1 = 0
score_2 = 0

class Player_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([15, 60])
        self.image.fill(BLACK)
        self.image = pygame.image.load("original.png")
        self.rect = self.image.get_rect()

        self.rect.x = 635
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

        if self.rect.y > 325:
            self.rect.y = 325



class Player_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([15, 60])
        self.image.fill(BLACK)
        self.image = pygame.image.load("Flag_of_the_Soviet_Union.png")
        self.rect = self.image.get_rect()

        self.rect.x = 38
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

        if self.rect.y > 325:
            self.rect.y = 325


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([12, 12])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        self.countdown = 100

        self.rect.x = 350
        self.rect.y = 200

        # self.change_x = random.randrange(3, 4)
        # self.change_y = random.randrange(3, 4)

        self.change_x = random.choice([3, -3])
        print(self.change_x)
        self.change_y = random.choice([3, -3])
        print(self.change_y)



    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.countdown -= 1

        if self.countdown < 0:

            self.rect.x = self.rect.x + self.change_x
            self.rect.y = self.rect.y + self.change_y


            if self.rect.y <= 0:
                self.change_y *= -1


            if self.rect.y >= 385:
                self.change_y *= -1




pygame.init()

collision_sound = pygame.mixer.Sound("bad_block.wav")
background_image = pygame.image.load("hockey.png")
background_sound = pygame.mixer.Sound("awesomeness.wav")
background_sound.play(-1)
background_sound.set_volume(.6)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])


pygame.display.set_caption("Ryan's Game")

all_sprites_list = pygame.sprite.Group()
ball_list = pygame.sprite.Group()


player_1 = Player_1()
all_sprites_list.add(player_1)


player_2 = Player_2()
all_sprites_list.add(player_2)

ball = Ball()
all_sprites_list.add(ball)
ball_list.add(ball)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


my_font = pygame.font.SysFont('Times New Roman', 30, True, False)



def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Times New Roman", 40, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLUE)
        text = my_font.render("Pong", True, WHITE)
        screen.blit(text, [320, 120])
        text_2 = my_font.render("Miracle on Ice Edition", True, WHITE)
        screen.blit(text_2, [200, 200])
        pygame.display.flip()
        clock.tick(60)


intro_screen()


def end_screen(winner):
    done = False
    my_font = pygame.font.SysFont("Times New Roman", 40, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(WHITE)
        text = my_font.render(winner, True, BLACK)
        screen.blit(text, [260, 150])
        pygame.display.flip()
        clock.tick(60)


done = False

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1.changespeed(0, -3)
            elif event.key == pygame.K_a:
                player_2.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(0, 3)
            elif event.key == pygame.K_z:
                player_2.changespeed(0, 3)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1.changespeed(0, 3)
            elif event.key == pygame.K_a:
                player_2.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player_1.changespeed(0, -3)
            elif event.key == pygame.K_z:
                player_2.changespeed(0, -3)




    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    screen.blit(background_image, [0, 0])

    frame += 1
    print(frame//2100)

    if frame % 2000 == 0:
        ball = Ball()
        ball.image = pygame.Surface([12, 12])
        ball.image.fill(BLACK)
        ball.rect = ball.image.get_rect()
        ball.rect.x = 350
        ball.rect.y = 200
        ball.change_x = random.choice([3, -3])
        print(ball.change_x)
        ball.change_y = random.choice([3, -3])
        print(ball.change_y)
        all_sprites_list.add(ball)
        ball_list.add(ball)




    for ball in ball_list:
        if ball.rect.x <= 0:
            ball.kill()
            ball = Ball()
            all_sprites_list.add(ball)
            ball_list.add(ball)
            score_1 += 1


        if ball.rect.x >= 690:
            ball.kill()
            ball = Ball()
            all_sprites_list.add(ball)
            ball_list.add(ball)
            score_2 += 1

    if score_1 == 20:
        end_screen("USA wins!")
        done = True
        break
    if score_2 == 20:
        end_screen("Soviets win")
        done = True
        break



    ball_hit_list = pygame.sprite.spritecollide(player_1, ball_list, False)

    for ball in ball_hit_list:
        ball.rect.right = player_1.rect.left
        ball.change_x *= -1
        collision_sound.play(0)

    ball_hit_list = pygame.sprite.spritecollide(player_2, ball_list, False)

    for ball in ball_hit_list:
        ball.rect.left = player_2.rect.right
        ball.change_x *= -1
        collision_sound.play(0)



    # --- Drawing code should go here
    # pygame.draw.rect(screen, BLACK, [25, 175, 15, 60], 0)
    # pygame.draw.rect(screen, BLACK, [660, 200, 15, 60], 0)


    # pygame.draw.line(screen, BLACK, [345, 700], [350, 0], 3)


    my_text = my_font.render("Score: " + str(score_2), True, BLACK)
    screen.blit(my_text, [50, 0])

    my_text = my_font.render("Score: " + str(score_1), True, BLACK)
    screen.blit(my_text, [550, 0])

    all_sprites_list.update()
    all_sprites_list.draw(screen)

    # --- Go ahead and update the sceen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()