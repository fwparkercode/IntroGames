"""
Jonah's final game
"""
import random
import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
level = 1
pygame.init()
jump_sound = pygame.mixer.Sound("bounce.ogg")



# classes
class Player(pygame.sprite.Sprite):

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width, color
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.speed_x = 55
        self.speed_y = -10
        self.accel_y = 0.1
        self.walls = None

    def changespeed(self, x, y):  # set movement
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):  # make the player update in the new position
        """ Update the player position. """
        # Move left/right
        self.change_y += self.accel_y
        self.rect.x += self.change_x

        # how the block collides with the walls
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.change_y = min(self.change_y, 5)

                self.change_y *= -1
                jump_sound.play()
            else:
                self.rect.top = block.rect.bottom


# make the first cut screen (the one that plays when the game begins)\
def cut_screen():
    done = False  # make the cut down program loop
    my_font = pygame.font.SysFont('Sprocket', 50, False, False)  # making the font
    while not done:
        # Main event loop (for cut screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)  # screen fill for cut screen

        my_text = my_font.render("Welcome to PLATFORM HOPPER!", True, WHITE)  # text creation (what the text says)
        screen.blit(my_text, [0, 0])  # where the text is blitted to the screen
        my_text_two = my_font.render("Use the ARROW KEYS to move the Player.", True,
                                     WHITE)  # text creation (what the text says)
        screen.blit(my_text_two, [0, 50])  # where the text is blitted to the screen
        my_text3 = my_font.render("Use the TRACK PAD to shoot.", True, WHITE)  # text creation (what the text says)
        screen.blit(my_text3, [0, 100])  # where the text is blitted to the screen
        my_text4 = my_font.render("Get to the yellow line to reach the next level.", True, WHITE)  # text creation (what the text says)
        screen.blit(my_text4, [0, 150])  # where the text is blitted to the screen
        my_text5 = my_font.render("Click to begin!", True, WHITE)  # text creation (what the text says)
        screen.blit(my_text5, [0, 200])  # where the text is blitted to the screen
        pygame.display.flip()  # everything is drawn
        clock.tick(60)


def win_screen():
    done = False  # make the cut down program loop
    my_font = pygame.font.SysFont('Sprocket', 80, False, False)  # making the font
    while not done:
        # Main event loop (for cut screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)  # screen fill for cut screen
        my_text = my_font.render("You Win!", True, WHITE)  # text creation (what the text says)
        screen.blit(my_text, [0, 0])  # where the text is blitted to the screen
        my_text_two = my_font.render("Click to Exit.", True, WHITE)  # text creation (what the text says)
        screen.blit(my_text_two, [0, 50])  # where the text is blitted to the screen
        pygame.display.flip()
        clock.tick(60) # clock tick for the win screen
def lose_screen():
    done = False  # make the cut down program loop
    my_font = pygame.font.SysFont('Sprocket', 80, False, False)  # making the font
    while not done:
        # Main event loop (for cut screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)  # screen fill for cut screen
        my_text = my_font.render("You Lose!", True, WHITE)  # text creation (what the text says)
        screen.blit(my_text, [0, 0])  # where the text is blitted to the screen
        my_text_two = my_font.render("Click to Exit.", True, WHITE)  # text creation (what the text says)
        screen.blit(my_text_two, [0, 50])  # where the text is blitted to the screen
        pygame.display.flip()
        clock.tick(60) # clock tick for the win screen

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speedy = 2 # where the vertical speed is made (this is why they fall.)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randrange(75, SCREEN_WIDTH - self.rect.width) # this makes the enemies not spawn in the safe zone


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20
                                        , 40]) # shape of bullet (a fun way to cheat is to make these numbers really big)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <= 0:
            self.kill()  # ):


# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('FINAL GAME: PLATFORM HOPPER')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

wall = Wall(0, 590, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, -100, 10, 700)
wall_list.add(wall)
all_sprite_list.add(wall)

# Create the player paddle object

player = Player(5, 550)
player.walls = wall_list

all_sprite_list.add(player)

clock = pygame.time.Clock()

done = False # enemies are created
for i in range(5):
    enemy = Enemy()
    enemy.rect.x = random.randrange(30, SCREEN_WIDTH - enemy.rect.width)
    enemy.rect.y = random.randrange(-600, SCREEN_HEIGHT)
    all_sprite_list.add(enemy)
    enemy_group.add(enemy)
cut_screen() # run the first cut screen
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet() # how the bullets are shot upward
            bullet.rect.centerx = player.rect.centerx #centering them on the player
            bullet.rect.centery = player.rect.centery
            all_sprite_list.add(bullet)
            bullet_group.add(bullet)

    all_sprite_list.update()
    for bullet in bullet_group: # how the enemies die and are reborn when hit by the bullets
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, False)
        for enemy in hit_list:
            enemy.rect.y = (-2 * SCREEN_HEIGHT)

    hit_list = pygame.sprite.spritecollide(player, enemy_group, True) # what makes the player die
    for hit in hit_list:
        lose_screen()
        done = True
    all_sprite_list.update()

    if player.rect.right >= SCREEN_WIDTH: # how the player wins
        level += 1
        player.rect.left = 15
        for i in range(5):
            enemy = Enemy()
            enemy.rect.x = random.randrange(30, SCREEN_WIDTH - enemy.rect.width)
            enemy.rect.y = random.randrange(-600, SCREEN_HEIGHT)
            all_sprite_list.add(enemy)
            enemy_group.add(enemy)
            enemy.speedy = level * 2

        if level == 3:
            wall = Wall(250, 550, 45, 10)
            wall_list.add(wall)
            all_sprite_list.add(wall)

        if level == 3:
            wall = Wall(200, 450, 45, 10)
            wall_list.add(wall)
            all_sprite_list.add(wall)

        if level == 2:
            wall = Wall(350, 0, 45, 275)
            wall_list.add(wall)
            all_sprite_list.add(wall)

        if level == 5:
            wall = Wall(350, 400, 45, 400)
            wall_list.add(wall)
            all_sprite_list.add(wall)

        if level == 6:
            win_screen()
            done = True
    screen.fill(BLACK)
    my_font = pygame.font.SysFont('Times new Roman', 40, False, False)  # making the font
    my_text = my_font.render("Level: " + str(level), True, WHITE)  # text creation (what the text says)
    screen.blit(my_text, [10, 0])  # where the text is blitted to the screen
    all_sprite_list.draw(screen)

    pygame.draw.rect(screen, YELLOW, [790, 0, 10, 600], )
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
