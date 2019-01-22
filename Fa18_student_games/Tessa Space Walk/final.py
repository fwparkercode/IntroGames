import pygame
import random

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
screen_width = 800
screen_height = 600

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(BLACK)

        # Return the image
        return image


class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        self.change_x = 0
        self.change_y = 0

        self.score = 0
        self.lives = 4

        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None


        sprite_sheet = SpriteSheet("p1_walk.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Move the player. """

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]


        # Move up/down
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.rock_list, True)
        rock_collide_sound = pygame.mixer.Sound("collision.wav")

        for i in block_hit_list:
            self.lives -= 1
            rock_collide_sound.set_volume(0.5)
            rock_collide_sound.play(0)

        # Gem collision
        gem_hit_list = pygame.sprite.spritecollide(self, self.level.gem_list, True)
        gem_sound = pygame.mixer.Sound("gem.wav")

        for gem in gem_hit_list:
            print(gem)
            self.score += 1
            gem_sound.set_volume(0.5)
            gem_sound.play(0)

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y



class Rock(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("space rock.png")

        self.rect = self.image.get_rect()


class Gem(pygame.sprite.Sprite):

    def __init__(self):
        super(Gem, self).__init__()
        self.images = []
        self.images.append(pygame.image.load("b1.png"))
        self.images.append(pygame.image.load("b2.png"))
        self.images.append(pygame.image.load("b3.png"))
        self.images.append(pygame.image.load("b4.png"))
        self.images.append(pygame.image.load("b5.png"))
        self.images.append(pygame.image.load("b6.png"))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.counter = 0

    def update(self):

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        self.counter += 3

        if self.counter >= 20:
            self.counter = 0
            self.index += 1

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()

        self.image = pygame.image.load("platform space.png")

        self.rect = self.image.get_rect()


class Level():
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.rock_list = pygame.sprite.Group()
        self.player = player
        self.all_sprites_list = pygame.sprite.Group()
        self.gem_list = pygame.sprite.Group()

        self.background = pygame.image.load("space.jpg").convert()
        self.background.set_colorkey(WHITE)

        # How far this world has been scrolled left/right
        self.world_shift = 0

        self.lives = 4

    def update(self):
        self.platform_list.update()
        self.rock_list.update()
        self.gem_list.update()
        self.all_sprites_list.update()


    def draw(self, screen):

        # Draw the background
        screen.fill(BLACK)
        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.rock_list.draw(screen)
        self.gem_list.draw(screen)


    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for rock in self.rock_list:
            rock.rect.x += shift_x

        for gem in self.gem_list:
            gem.rect.x += shift_x



# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(10):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(15):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)

class Level_03(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(20):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)

class Level_04(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(25):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)

class Level_05(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(30):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)

class Level_06(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(35):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)

class Level_07(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(40):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)

class Level_08(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(45):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)

class Level_09(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(50):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)

class Level_10(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        for i in range(55):
            block = Rock()
            block.rect.x = random.randrange(300, 1800)
            block.rect.y = random.randrange(screen_height - 56)
            block.player = self.player
            self.rock_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(2):
            gems = Gem()
            gems.rect.x = random.randrange(300, 1800)
            gems.rect.y = random.randrange(screen_height - 40)
            self.gem_list.add(gems)
            self.all_sprites_list.add(gems)


def main():
    """ Main Program """
    pygame.init()


    # Set the height and width of the screen
    size = [screen_width, screen_height]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Space Adventure")

    # Create the player
    player = Player(50, screen_width - 50)

    # Create all the levels
    level_list = []

    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))
    level_list.append(Level_05(player))
    level_list.append(Level_06(player))
    level_list.append(Level_07(player))
    level_list.append(Level_08(player))
    level_list.append(Level_09(player))
    level_list.append(Level_10(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 240
    player.rect.y = screen_height - player.rect.height
    active_sprite_list.add(player)


    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    background_music = pygame.mixer.Sound("music.wav")
    background_music.set_volume(0.5)
    background_music.play(-1)

    def intro_screen():
        done = False
        my_font = pygame.font.SysFont("comicsansms", 50, True, False)
        my_font_two = pygame.font.SysFont("comicsansms", 30, True, False)
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] > 206 and event.pos[0] < 591 and event.pos[1] > 299 and event.pos[1] < 325:
                        instruction_screen()
                        done = True
                    if event.pos[0] > 186 and event.pos[0] < 611 and event.pos[1] > 359 and event.pos[1] < 387:
                        done = True
                    if event.pos[0] > 344 and event.pos[0] < 454 and event.pos[1] > 487 and event.pos[1] < 516:
                        credits_screen()

            screen.fill(BLACK)
            my_text_one = my_font.render("Welcome to Space Adventure", True, WHITE)
            text_rect = my_text_one.get_rect(center=(screen_width / 2, screen_height / 2 - 150))
            screen.blit(my_text_one, text_rect)

            my_text_two = my_font_two.render("Click here for instructions", True, WHITE)
            text_rect = my_text_two.get_rect(center=(screen_width / 2, screen_height / 2 + 10))
            screen.blit(my_text_two, text_rect)

            my_text_three = my_font_two.render("Or click here begin the game", True, WHITE)
            text_rect = my_text_three.get_rect(center=(screen_width / 2, screen_height / 2 + 70))
            screen.blit(my_text_three, text_rect)

            my_text_four = my_font_two.render("Credits", True, WHITE)
            text_rect = my_text_four.get_rect(center=(screen_width / 2, screen_height / 2 + 200))
            screen.blit(my_text_four, text_rect)

            pygame.display.flip()
            # --- Limit to 60 frames per second
            clock.tick(60)


    def instruction_screen():
        done = False
        my_font = pygame.font.SysFont("comicsansms", 50, True, False)
        my_font_two = pygame.font.SysFont("comicsansms", 30, True, False)
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] > 171 and event.pos[0] < 628 and event.pos[1] > 484 and event.pos[1] < 521:
                        intro_screen()
                        done = True

            screen.fill(BLACK)
            my_text_one = my_font.render("INSTRUCTIONS", True, WHITE)
            text_rect = my_text_one.get_rect(center=(screen_width / 2, screen_height / 2 - 250))
            screen.blit(my_text_one, text_rect)

            my_text_two = my_font_two.render("Use the right arrow to move right", True, WHITE)
            text_rect = my_text_two.get_rect(center=(screen_width / 2, screen_height / 2 - 40))
            screen.blit(my_text_two, text_rect)

            my_text_three = my_font_two.render("Use the left arrow to move left", True, WHITE)
            text_rect = my_text_three.get_rect(center=(screen_width / 2, screen_height / 2))
            screen.blit(my_text_three, text_rect)

            my_text_four = my_font_two.render("Use the up arrow to move up", True, WHITE)
            text_rect = my_text_four.get_rect(center=(screen_width / 2, screen_height / 2 + 40))
            screen.blit(my_text_four, text_rect)

            my_text_five = my_font_two.render("Use the down arrow to move down", True, WHITE)
            text_rect = my_text_five.get_rect(center=(screen_width / 2, screen_height / 2 + 80))
            screen.blit(my_text_five, text_rect)

            my_text_five = my_font_two.render("Go back to the menu", True, WHITE)
            text_rect = my_text_five.get_rect(center=(screen_width / 2, screen_height / 2 + 200))
            screen.blit(my_text_five, text_rect)

            pygame.display.flip()
            # --- Limit to 60 frames per second
            clock.tick(60)


    def level_screen():
        done = False
        my_font = pygame.font.SysFont("comicsansms", 50, True, False)
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    done = True
            screen.fill(BLACK)
            player.change_x = 0
            player.change_y = 0
            my_text_one = my_font.render("Level " + str(current_level_no + 1), True, WHITE)
            text_rect = my_text_one.get_rect(center=(screen_width / 2, screen_height / 2 - 100))
            screen.blit(my_text_one, text_rect)

            pygame.display.flip()
            # --- Limit to 60 frames per second
            clock.tick(60)


    def game_over():
        done = False
        my_font = pygame.font.SysFont("comicsansms", 40, True, False)
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if event.pos[0] > 151 and event.pos[0] < 246 and event.pos[1] > 480 and event.pos[1] < 517:
                        done = True
                    if event.pos[0] > 524 and event.pos[0] < 673 and event.pos[1] > 483 and event.pos[1] < 520:
                        intro_screen()

            screen.fill(BLACK)
            player.change_x = 0
            player.change_y = 0
            my_text_one = my_font.render("GAME OVER", True, WHITE)
            text_rect = my_text_one.get_rect(center=(screen_width / 2, screen_height / 2 - 150))
            screen.blit(my_text_one, text_rect)

            my_text_two = my_font.render("Quit", True, WHITE)
            text_rect = my_text_two.get_rect(center=(screen_width / 2 - 200, screen_height / 2 + 200))
            screen.blit(my_text_two, text_rect)

            my_text_three = my_font.render("Restart", True, WHITE)
            text_rect = my_text_three.get_rect(center=(screen_width / 2 + 200, screen_height / 2 + 200))
            screen.blit(my_text_three, text_rect)

            my_text_four = my_font.render("Gem's Collected " + str(player.score), True, WHITE)
            text_rect = my_text_four.get_rect(center=(screen_width / 2, screen_height / 2))
            screen.blit(my_text_four, text_rect)

            pygame.display.flip()
            # --- Limit to 60 frames per second
            clock.tick(60)
        pygame.quit()

    def win():
        done = False
        my_font = pygame.font.SysFont("comicsansms", 40, True, False)
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if event.pos[0] > 151 and event.pos[0] < 246 and event.pos[1] > 480 and event.pos[1] < 517:
                        done = True
                    if event.pos[0] > 524 and event.pos[0] < 673 and event.pos[1] > 483 and event.pos[1] < 520:
                        instruction_screen()

            screen.fill(BLACK)
            player.change_x = 0
            player.change_y = 0
            my_text_one = my_font.render("YOU WIN", True, WHITE)
            text_rect = my_text_one.get_rect(center=(screen_width / 2, screen_height / 2 - 150))
            screen.blit(my_text_one, text_rect)

            my_text_two = my_font.render("Quit", True, WHITE)
            text_rect = my_text_two.get_rect(center=(screen_width / 2 - 200, screen_height / 2 + 200))
            screen.blit(my_text_two, text_rect)

            my_text_three = my_font.render("Restart", True, WHITE)
            text_rect = my_text_three.get_rect(center=(screen_width / 2 + 200, screen_height / 2 + 200))
            screen.blit(my_text_three, text_rect)

            my_text_four = my_font.render("Gem's Collected " + str(player.score), True, WHITE)
            text_rect = my_text_four.get_rect(center=(screen_width / 2, screen_height / 2))
            screen.blit(my_text_four, text_rect)

            pygame.display.flip()
            # --- Limit to 60 frames per second
            clock.tick(60)
        pygame.quit()

    def credits_screen():
        done = False
        my_font = pygame.font.SysFont("comicsansms", 50, True, False)
        my_font_two = pygame.font.SysFont("comicsansms", 30, True, False)
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if event.pos[0] > 208 and event.pos[0] < 592 and event.pos[1] > 508 and event.pos[1] < 537:
                        intro_screen()
                        done = True

            screen.fill(BLACK)
            my_text_one = my_font.render("CREDITS", True, WHITE)
            text_rect = my_text_one.get_rect(center=(screen_width / 2, screen_height / 2 - 250))
            screen.blit(my_text_one, text_rect)

            my_text_two = my_font_two.render("Everything:", True, WHITE)
            text_rect = my_text_two.get_rect(center=(screen_width / 2, screen_height / 2 - 100))
            screen.blit(my_text_two, text_rect)

            my_text_three = my_font_two.render("Tessa Samuels", True, WHITE)
            text_rect = my_text_three.get_rect(center=(screen_width / 2, screen_height / 2 - 60))
            screen.blit(my_text_three, text_rect)

            my_text_four = my_font_two.render("Special Thanks to:", True, WHITE)
            text_rect = my_text_four.get_rect(center=(screen_width / 2, screen_height / 2))
            screen.blit(my_text_four, text_rect)

            my_text_five = my_font_two.render("Mr Lee", True, WHITE)
            text_rect = my_text_five.get_rect(center=(screen_width / 2, screen_height / 2 + 40))
            screen.blit(my_text_five, text_rect)

            my_text_six = my_font_two.render("Sleep Deprivation", True, WHITE)
            text_rect = my_text_six.get_rect(center=(screen_width / 2, screen_height / 2 + 80))
            screen.blit(my_text_six, text_rect)

            my_text_seven = my_font_two.render("And Procrastination", True, WHITE)
            text_rect = my_text_seven.get_rect(center=(screen_width / 2, screen_height / 2 + 120))
            screen.blit(my_text_seven, text_rect)

            my_text_eight = my_font_two.render("Go back to the main menu", True, WHITE)
            text_rect = my_text_eight.get_rect(center=(screen_width / 2, screen_height / 2 + 220))
            screen.blit(my_text_eight, text_rect)

            pygame.display.flip()
            # --- Limit to 60 frames per second
            clock.tick(60)
        pygame.quit()

    intro_screen()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-4, 0)
                    player.direction = "L"
                if event.key == pygame.K_RIGHT:
                    player.changespeed(4, 0)
                    player.direction = "R"
                if event.key == pygame.K_UP:
                    player.changespeed(0, -4)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 4)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(4, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-4, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 4)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -4)

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                level_screen()
                current_level = level_list[current_level_no]
                player.level = current_level


        if player.lives <= 0:
            game_over()

        if current_level_no >= 11:
            win()

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)


        my_font = pygame.font.SysFont("comicsansms", 50, True, False)

        my_text = my_font.render("Score: " + str(player.score), True, WHITE)
        screen.blit(my_text, [50, 40])

        level_text = my_font.render("Lives: " + str(player.lives), True, WHITE)

        screen.blit(level_text, [400, 40])



        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
pygame.quit()


if __name__ == "__main__":
    main()