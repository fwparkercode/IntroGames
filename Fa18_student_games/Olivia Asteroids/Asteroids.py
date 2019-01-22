"""
Olivia Hanley
Introduction to Computer Programming
Final Project - Asteroids
"""
import pygame
import random
import math

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.display.set_caption("Final Project: Asteroids")
done = False

# Define some images
player_image = pygame.image.load("new_arrow.png")
asteroid_image = pygame.image.load("large_asteroid.png")

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

my_font = pygame.font.SysFont('Calibri', 30, True, False)


# CLASSES
class Block(pygame.sprite.Sprite):
    # This class represents the block.
    def __init__(self, file):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.rect.x += self.change_x
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

        self.rect.y += self.change_y
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
        if self.rect.left < 0:
            self.rect.right = SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    # This class represents the Player.
    def __init__(self, file):
        # Set up the player on creation.
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load(file)
        self._image = self.image
        self.rect = self.image.get_rect()
        self.angle = 0
        self.width = self.rect.width
        self.height = self.rect.height

    def update(self):
        x, y = pygame.mouse.get_pos()

        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = self.rect.centerx - x
        y_diff = self.rect.centery - y
        angle = math.atan2(-y_diff, x_diff)
        angle = math.degrees(angle)
        print(angle)
        pos = self.rect.center
        self.image = pygame.transform.rotozoom(self._image, angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


class Bullet(pygame.sprite.Sprite):
    # This class represents the bullet.
    def __init__(self, start_x, start_y, dest_x, dest_y):
        # Constructor.
        # It takes in the starting x and y location.
        # It also takes in the destination x and y position.

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set up the image for the bullet
        self.image = pygame.Surface([4, 4])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # Move the bullet to our starting location
        self.rect.x = start_x
        self.rect.y = start_y

        # Because rect.x and rect.y are automatically converted
        # to integers, we need to create different variables that
        # store the location as floating point numbers. Integers
        # are not accurate enough for aiming.
        self.floating_point_x = start_x
        self.floating_point_y = start_y

        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        velocity = 8
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity

    def update(self):
        # Move the bullet.
        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, file):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1

        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1


# CREATE THE WINDOW

# SET THE HEIGHT AND WIDTH OF THE SCREEN
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# SPRITE LISTS

# List of each block in the game
block_list = pygame.sprite.Group()

# List of each bullet in the game
bullet_list = pygame.sprite.Group()
enemy_bullet_list = pygame.sprite.Group()

player_list = pygame.sprite.Group()

# List of each enemy in the game
enemy_list = pygame.sprite.Group()

# CREATE THE SPRITES
for i in range(2):
    # This represents a block
    block = Block("large_asteroid.png")

    # Set a random location for the block
    block.rect.x = random.choice([0, SCREEN_WIDTH - block.rect.width])
    block.rect.y = random.randrange(SCREEN_HEIGHT + 10)

    block.change_x += random.randrange(1, 3)
    block.change_y += random.randrange(1, 3)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

for i in range(1):
    enemy = Enemy("saucer.png")
    # This represents a block
    # Set a random location for the block
    enemy.rect.x = random.choice([0, SCREEN_WIDTH - 50])
    enemy.rect.y = random.randrange(SCREEN_HEIGHT + 10)

    enemy.change_x = random.randrange(-3, 3)
    enemy.change_y = random.randrange(-3, 3)
    enemy.left_boundary = 0
    enemy.top_boundary = 0
    enemy.right_boundary = SCREEN_WIDTH
    enemy.bottom_boundary = SCREEN_HEIGHT

    # Add the block to the list of objects
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)


# Create a red player block
player = Player("new_arrow.png")
all_sprites_list.add(player)
player_x = 0
player_y = 0


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0
lives = 5
level = 1

player.rect.x = SCREEN_WIDTH / 2 - 32.5
player.rect.y = SCREEN_HEIGHT / 2 - 32.5
display_instructions = True
instruction_page = 1

# Define some sounds
background_music = pygame.mixer.Sound("Orbital Colossus.wav")
background_music.play()
bullet_sound = pygame.mixer.Sound("GUN_FIRE-GoodSoundForYou-820112263.wav")
asteroid_sound = pygame.mixer.Sound("Shotgun_Blast-Jim_Rogers-1914772763.wav")
saucer_sound = pygame.mixer.Sound("Silencer-SoundBible.com-1632156458.wav")

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    # Set the screen background
    screen.fill(BLACK)

    if instruction_page == 1:
        # Draw instructions, page 1
        text = my_font.render("Welcome to Asteroids!", True, WHITE)
        screen.blit(text, [100, 80])

        text = my_font.render("You are a ship traveling through space.", True, WHITE)
        screen.blit(text, [150, 120])

        text = my_font.render("Destroy the saucers and asteroids to win!", True, WHITE)
        screen.blit(text, [200, 160])

    if instruction_page == 2:
        # Draw instructions, page 2
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
        text = my_font.render("Good luck!", True, WHITE)
        screen.blit(text, [600, 250])

        my_text = my_font.render("Click to Continue", True, WHITE)
        screen.blit(my_text, [600, 300])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


# -------- Game Over -----------
def end_screen():
    done = False
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        screen.fill(BLACK)
        # Render the score text
        my_text = my_font.render("GAME OVER THANKS FOR PLAYING!", True, WHITE)
        screen.blit(my_text, [20, 50])

        my_text = my_font.render("Score: " + str(score), True, WHITE)
        screen.blit(my_text, [20, 75])

        my_text = my_font.render("Level: " + str(level), True, WHITE)
        screen.blit(my_text, [20, 100])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # --- Limit to 60 frames per second
        clock.tick(60)


# MAIN PROGRAM LOOP
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet_sound.play()
            # Fire a bullet if the user clicks the mouse button
            # Get the mouse position
            pos = pygame.mouse.get_pos()

            mouse_x = pos[0]
            mouse_y = pos[1]

            # Create the bullet based on where we are, and where we want to go.
            bullet = Bullet(player.rect.centerx, player.rect.centery, mouse_x, mouse_y)

            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

        elif lives == 0:
            end_screen()
            done = True

    for enemy_ in enemy_list:
        if random.randrange(180) == 0:
            bullet = Bullet(enemy.rect.x, enemy.rect.y, player_x, player_y)

            bullet.image = pygame.Surface([10, 10])
            bullet.image.fill(RED)
            bullet.rect = bullet.image.get_rect()

            bullet.angle = random.random() * math.pi * 2
            velocity = 2
            bullet.change_x = math.cos(bullet.angle) * velocity
            bullet.change_y = math.sin(bullet.angle) * velocity
            enemy_bullet_list.add(bullet)
            all_sprites_list.add(bullet)

    if not done:
        # GAME LOGIC

        # Call the update() method on all the sprites
        all_sprites_list.update()

        # Calculate mechanics for each bullet
        for bullet in bullet_list:
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1
                print(score)
            enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)

            # For each block hit, remove the bullet and add to the score
            for enemy in enemy_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 5
                print(score)
            enemy_bullet_hit_list = pygame.sprite.spritecollide(bullet, enemy_bullet_list, True)

            for enemy in enemy_bullet_hit_list:
                bullet.kill()
                score += 2
                print(score)
            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

        hit_list = pygame.sprite.spritecollide(player, enemy_bullet_list, True)
        for hit in hit_list:
            lives -= 1
            enemy_bullet_list.empty()
            block_list.empty()
            enemy_list.empty()
            all_sprites_list.empty()
            all_sprites_list.add(player)

            for i in range(2 * level):
                # This represents a block
                block = Block("large_asteroid.png")

                # Set a random location for the block
                block.rect.x = random.choice([0, SCREEN_WIDTH - block.rect.width])
                block.rect.y = random.randrange(SCREEN_HEIGHT + 10)

                while block.change_x == 0 and block.change_y == 0:
                    block.change_x += random.randrange(1, 3)
                    block.change_y += random.randrange(1, 3)

                # Add the block to the list of objects
                block_list.add(block)
                all_sprites_list.add(block)

            for i in range(2):
                enemy = Enemy("saucer.png")
                # This represents a block
                # Set a random location for the block
                enemy.rect.x = random.randrange(SCREEN_WIDTH - enemy.rect.width)
                enemy.rect.y = random.randrange(SCREEN_HEIGHT + 10)

                enemy.change_x = random.randrange(-3, 3)
                enemy.change_y = random.randrange(-3, 3)
                enemy.left_boundary = 0
                enemy.top_boundary = 0
                enemy.right_boundary = SCREEN_WIDTH
                enemy.bottom_boundary = SCREEN_HEIGHT

                # Add the block to the list of objects
                enemy_list.add(enemy)
                all_sprites_list.add(enemy)

        player_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
        for enemy in player_hit_list:
            saucer_sound.play()
            lives -= 1
            print(lives)

        player_hit_list = pygame.sprite.spritecollide(player, enemy_bullet_list, True)
        for enemy_bullet in player_hit_list:
            lives -= 1
            print("HIT")

        player_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        for block in player_hit_list:
            asteroid_sound.play()
            lives -= 1
            print(lives)

        count = len(enemy_list) + len(block_list)  # number of enemies
        enemy_bullet_list.empty()

        if count == 0:
            level += 1
            print(level)
            all_sprites_list.empty()
            all_sprites_list.add(player)
            enemy_list.empty()
            bullet_list.empty()
            for i in range(2 * level):
                # This represents a block
                block = Block("large_asteroid.png")

                # Set a random location for the block
                block.rect.x = random.choice([0, SCREEN_WIDTH - block.rect.width])
                block.rect.y = random.randrange(SCREEN_HEIGHT + 10)

                while block.change_x == 0 and block.change_y == 0:
                    block.change_x += random.randrange(1, 3)
                    block.change_y += random.randrange(1, 3)

                # Add the block to the list of objects
                block_list.add(block)
                all_sprites_list.add(block)

            for i in range(2):
                enemy = Enemy("saucer.png")
                # This represents a block
                # Set a random location for the block
                enemy.rect.x = random.randrange(SCREEN_WIDTH - enemy.rect.width)
                enemy.rect.y = random.randrange(SCREEN_HEIGHT + 10)

                enemy.change_x = random.randrange(-3, 3)
                enemy.change_y = random.randrange(-3, 3)
                enemy.left_boundary = 0
                enemy.top_boundary = 0
                enemy.right_boundary = SCREEN_WIDTH
                enemy.bottom_boundary = SCREEN_HEIGHT

                # Add the block to the list of objects
                enemy_list.add(enemy)
                all_sprites_list.add(enemy)

    # DRAW A FRAME
    # Clear the screen
    screen.fill(BLACK)

    # Draw all the spites
    all_sprites_list.draw(screen)

    my_text = my_font.render("Score: " + str(score), True, WHITE)
    screen.blit(my_text, [50, 50])

    my_text = my_font.render("Lives: " + str(lives), True, WHITE)
    screen.blit(my_text, [50, 75])

    my_text = my_font.render("Level: " + str(level), True, WHITE)
    screen.blit(my_text, [50, 100])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(60)
