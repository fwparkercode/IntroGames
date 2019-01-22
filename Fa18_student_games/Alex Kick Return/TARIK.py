# Import a library of functions called 'pygame'
import pygame
import random
import time
# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Define dimensions
screen_width = 600
screen_height = 800
player_height = 51
player_width = 70

size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TARRRIIIKKK")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Global Variables
level = 1
player_speed = 3
score = 0
speed = 1
player_yspeed = 0
player_y = 0
player_xspeed = 0
player_x = 0
jukes = 5
power_up_odds = random.randrange(1, 5)
speed_lines_number = 0
quit = False
# Text resources

my_font = pygame.font.SysFont('Calibri', 30, True, False)

# Classes


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, w, z, stop):
        """ Change the speed of the player"""
        if stop != True:
            self.change_x += w
            self.change_y += z

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.left <= 0:
            self.rect.left = 1
        if self.rect.top <= 0:
            self.rect.top = 1
        if self.rect.bottom >= screen_height - player_height + 10:
            self.rect.bottom = screen_height - player_height + 10
        if len(enemy_list.sprites()) < level + 2:
            enemy = Player(random.randrange(50, screen_width), random.randrange(50, 100))
            enemy.image = pygame.image.load("matthews.png")
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)
        for enemy in enemy_list:
            if len(enemy_list.sprites()) > level + 2:
                enemy.kill()


# image resources
background_image = pygame.image.load("bears_stadium.png")
tarik_cohen = pygame.image.load("TARIK COHEN.png")
football = pygame.image.load("FOOTBALL.png")
lightning = pygame.image.load("lightning-bolt.png")
speed_lines = pygame.image.load("speed.png")

# Sound resources
background_music = pygame.mixer.Sound("Wretched Blade 1.ogg")
touchdown_sound = pygame.mixer.Sound("touchdown.wav")
bump_sound = pygame.mixer.Sound("bump.wav")
tackle_sound = pygame.mixer.Sound("tackle.wav")

# start my background music
background_music.play(-1)


# create Groups
enemy_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
power_up_list = pygame.sprite.Group()

# Create Sprites
juke_powerup = Player(random.randrange(0, screen_width), random.randrange(0, screen_height))
power_up_list.add(juke_powerup)
player = Player((screen_width/2) - 10, screen_height - 73)

# Create Enemies
for i in range(level + 2):
    enemy = Player(random.randrange(50, screen_width), random.randrange(50, 100))
    enemy.image = pygame.image.load("matthews.png")
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)


all_sprites_list.add(player)


# Alter Sprites
player.image = pygame.image.load("TARIK COHEN.png")
player.rect = player.image.get_rect()
juke_powerup.image = pygame.image.load("lightning-bolt.png")


# Functions
def you_scored(level, speed):
    touchdown_sound.play()
    player.rect.x = screen_width / 2
    player.rect.y = screen_height - 73
    level += 1
    if level > 5:
        speed += .5
    elif level > 9:
        speed += .2
    else:
        speed += 0
    for enemy in enemy_list:
        enemy.rect.x = random.randrange(50, screen_width)
        enemy.rect.y = random.randrange(50, 100)
    return level, speed

if not quit:
    def you_got_tackled():
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        tackle_sound.play()
        time.sleep(.1)
        player.rect.x = screen_width / 2
        player.rect.y = screen_height - 73
        level = 1
        speed = 1
        score = 0
        for enemy in enemy_list:
            enemy.rect.x = random.randrange(50, screen_width)
            enemy.rect.y = random.randrange(50, 100)
        return level, speed, score


def cut_screen(text1, text2, text3, text4, text5, text6):
    player.changespeed(0, 0, False)
    done1 = False
    done = False # local variable done
    quit = False
    while not done1:
        state = pygame.key.get_pressed()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done1 = True # Flag that we are done so we exit this loop
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and state[pygame.K_UP] == 0 and state[pygame.K_DOWN] == 0 and state[pygame.K_LEFT] == 0 and state[pygame.K_RIGHT] == 0:
                done1 = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y and state[pygame.K_UP] == 0 and state[pygame.K_DOWN] == 0 and state[pygame.K_LEFT] == 0 and state[pygame.K_RIGHT] == 0:
                    player.changespeed(0, 0, False)
                    done1 = True
                    done = False
                elif event.key == pygame.K_n:
                    pygame.display.quit()
                    pygame.quit()
                    done1 = True
                    done = True
                    quit = True
                # Move with arrow keys
                elif event.key == pygame.K_LEFT:
                    player.changespeed(-player_speed, 0, False)
                    moving = True
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(player_speed, 0, False)
                    moving = True
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -player_speed, False)
                    moving = True
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, player_speed, False)
                    moving = True
                    # Flip with space
                elif event.key == pygame.K_SPACE:
                    player.image = pygame.transform.flip(player.image, True, True)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(player_speed, 0, False)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-player_speed, 0, False)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, player_speed, False)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -player_speed, False)
                elif event.key == pygame.K_SPACE:
                    player.image = pygame.transform.flip(player.image, True, True)


            player.changespeed(0, 0, False)
        if not quit:
            screen.fill(BLACK)
            myfont = pygame.font.SysFont("Britannic Bold", 40)
            nlabel = myfont.render(text1, True, WHITE)
            nlabel_rect = nlabel.get_rect(center=(screen_width / 2, 300))
            instructions = myfont.render(text2, True, WHITE)
            instructions_rect = instructions.get_rect(center=(screen_width / 2, 400))
            instructions_2 = myfont.render(text3, True, WHITE)
            instructions_2_rect = instructions_2.get_rect(center=(screen_width / 2, 440))
            start = myfont.render(text4, True, WHITE)
            start_rect = start.get_rect(center=(screen_width / 2, 500))
            extra1 = myfont.render(text5, True, WHITE)
            extra1_rect = extra1.get_rect(center=(screen_width / 2, 600))
            extra2 = myfont.render(text6, True, WHITE)
            extra2_rect = extra2.get_rect(center=(screen_width / 2, 650))
            if text1 != "none":
                screen.blit(nlabel, nlabel_rect)
            if text2 != "none":
                screen.blit(instructions, instructions_rect)
            if text3 != "none":
                screen.blit(instructions_2, instructions_2_rect)
            if text4 != "none":
                screen.blit(start, start_rect)
            if text5 != "none":
                screen.blit(extra1, extra1_rect)
            if text6 != "none":
                screen.blit(extra2, extra2_rect)
            pygame.display.flip()

        clock.tick(60)
    return done, quit


done, quit = cut_screen("Welcome to Tarik Cohen Kick Returner!", "Use the arrow keys to move, and WASD to", "juke.", "Click to begin!", "none", "none")

# THIS IS HIGH SCORE CODE EDITED FROM http://programarcadegames.com/python_examples/show_file.php?file=high_score.py
def get_high_score():
    # Default high score
    high_score = 0

    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()

    except IOError:
        # Error reading file, no high score
        pass
    except ValueError:
        # There's a file there, but we don't understand the number.
        pass

    return high_score


def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        pass

def main():
    """ Main program is here. """
    # Get the high score
    high_score = get_high_score()

    # Get the score from the current game
    current_score = score

    # See if we have a new high score
    if current_score > high_score:
        # We do! Save to disk
        save_high_score(current_score)
    else:
        pass
test = 0
# Game loop
if not quit:
    while not done:
        if test < 10:
            player.rect.x = (screen_width / 2) - 10
            player.rect.y = screen_height - 73
            test += 1

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                # Move with arrow keys
                if event.key == pygame.K_LEFT:
                    player.changespeed(-player_speed, 0, False)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(player_speed, 0, False)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -player_speed, False)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, player_speed, False)
                elif event.key == pygame.K_n:
                    done = True
                # Reset high score
                elif event.key == pygame.K_ESCAPE:
                    high_score_file = open("high_score.txt", "w")
                    high_score_file.write(str(0))
                    high_score_file.close()
                    # Flip with space
                elif event.key == pygame.K_SPACE:
                    player.image = pygame.transform.flip(player.image, True, True)
                    # Juke with WASD
                elif event.key == pygame.K_w and jukes > 0:
                    speed_lines_number = 100
                    player.rect.y -= 50
                    jukes -=1
                elif event.key == pygame.K_a and jukes > 0:
                    speed_lines_number = 100
                    player.rect.x -= 50
                    jukes -= 1
                elif event.key == pygame.K_d and jukes > 0:
                    speed_lines_number = 100
                    player.rect.x += 50
                    jukes -= 1
                elif event.key == pygame.K_s and jukes > 0:
                    speed_lines_number = 100
                    player.rect.y += 50
                    jukes -= 1

            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(player_speed, 0, False)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-player_speed, 0, False)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, player_speed, False)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -player_speed, False)
                elif event.key == pygame.K_SPACE:
                    player.image = pygame.transform.flip(player.image, True, True)
            else:
                player.changespeed(0, 0, False)
        # Set defense speed and position
        for enemy in enemy_list:
            if player.rect.x >= enemy.rect.x:
                enemy.rect.x += random.randrange(0, level + 1)
            else:
                enemy.rect.x += random.randrange(-level, 0)
            if player.rect.y >= enemy.rect.y:
                enemy.rect.y += speed
            else:
                enemy.rect.y -= speed

            # Add a juke powerup
            add_juke = pygame.sprite.spritecollide(player, power_up_list, False)

            for juke_powerup in add_juke:
                juke_powerup.rect.x = 1000
                jukes += 1

        # Restart game if tackled
        get_tackled = pygame.sprite.spritecollide(player, enemy_list, False)

        # Don't let enemies be in a line
        for enemy in enemy_list:
            for enemy1 in enemy_list:
                if enemy.rect.x == enemy1.rect.x and enemy.rect.y != enemy1.rect.y:
                    enemy.rect.x += random.randrange(-20, 20)

        for enemy in enemy_list:
            for enemy1 in enemy_list:
                if enemy.rect.y == enemy1.rect.y and enemy.rect.x != enemy1.rect.x:
                    enemy.rect.y += random.randrange(-20, 20)

        # Restart game if tackled
        for enemy in get_tackled:
            player_speed1 = player_speed
            player.changespeed(0, 0, True)
            you_got_tackled()
            power_up_odds = random.randrange(1, 4)
            jukes = 5
            juke_powerup.rect.x = random.randrange(30, screen_width - 30)
            juke_powerup.rect.y = random.randrange(0, screen_height)
            cut_screen("You got tackled :( with a score of " + str(score), "Release the arrow keys and press", "Y to play again,", "Or N to quit.", "Press ESC if you want to reset the highscore,", "it saves locally on your computer.")
            player_speed = 3
            player.changespeed(0, 0, True)
            level, speed, score = you_got_tackled()



        # Don't let player go out of bounds
        if 498 <= player.rect.x:
            player.changespeed(0, 0, False)
            player.rect.x = 497
            bump_sound.play()

        if 27 >= player.rect.x:
            player.changespeed(0, 0, False)
            player.rect.x = 28
            bump_sound.play()


        speed_lines_number -= 15



        # Next level if player scores
        if player.rect.top <= 50 and test > 1:
            player.changespeed(0, 0, False)
            you_scored(level, speed)
            level, speed = you_scored(level, speed)
            power_up_odds = random.randrange(1, 4)
            juke_powerup.rect.x = random.randrange(0, screen_width)
            juke_powerup.rect.y = random.randrange(0, screen_height)
            cut_screen("Level " + str(level) + "!", "none", "Release the arrow keys and", "click to continue!", "none", "none")
            if level % 4 == 1:
                player.changespeed(0, 0, False)
                player_speed += 2
              # increase speed eventually
            score += 7



        main()
        high_score = get_high_score()

        # All drawing code happens after the for loop and but
        # inside the main while not done loop.

        all_sprites_list.update()

        # Create Background
        screen.blit(background_image, [0, 0])
        # Draw Sprites
        if power_up_odds == 2:
            power_up_list.draw(screen)

        all_sprites_list.draw(screen)


        # Render the  text
        score_text = my_font.render(("Score: " + str(score)), True, BLACK)
        juke_text = my_font.render(("Jukes remaining: " + str(jukes)), True, BLACK)
        high_score_text = my_font.render(("High score:" + str(high_score)), True, BLACK)

        # Blit text to screen

        screen.blit(score_text, [20, 20])
        screen.blit(juke_text, [screen_width - 250, 20])
        screen.blit(high_score_text, [20, 50])
        if speed_lines_number > 0:
            screen.blit(speed_lines, [player.rect.centerx - 175, player.rect.centery - 175])
        # Update screen
        pygame.display.flip()


        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(60)

# Be IDLE friendly
pygame.quit()
