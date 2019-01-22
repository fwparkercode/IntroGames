import pygame
import random
# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTB = (153, 204, 255)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.init()

clock = pygame.time.Clock()
block_list = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("female_walk1.png")

        self.rect = self.image.get_rect()
        self.health = 1
        self.helth1 = 1

        self.change_x = 0
        self.change_y = 0


        self.level = None

    def update(self):

        self.calc_grav()

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35


        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.image.load("carBlue1_006.png")
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, SCREEN_WIDTH)

    def update(self):
        self.rect.y += 2
        if self.rect.y > 410:
            self.reset_pos()

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

wall = Wall(400, 595, 900, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 0, 0, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 595, 325, 10)
wall_list.add(wall)
all_sprite_list.add(wall)


class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height):

        super().__init__()

        self.image = pygame.image.load("ground_stone.png")
        self.rect = self.image.get_rect()


class MovingPlatform(Platform):

    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    player = None

    level = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        self.rect.x += self.change_x

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:

            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right


        self.rect.y += self.change_y

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:

            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1


class Level(object):


    def __init__(self, player):


        self.platform_list = pygame.sprite.Group()

        self.player = player


        self.background = pygame.image.load

        self.world_shift = 0
        self.level_limit = -1000


    def update(self):

        self.platform_list.update()


    def draw(self, screen):


        screen.fill(LIGHTB)


        self.platform_list.draw(screen)



    def shift_world(self, shift_x):


        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x


all_sprites_list = pygame.sprite.Group()

class Level_01(Level):

    def __init__(self, player):


        Level.__init__(self, player)

        self.level_limit = -1500

        level = [[210, 70, 600, 500],
                 [210, 70, 400, 600],
                 [210, 70, 275, 600],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [210, 70, 1800, 300],
                 [210, 70, 2000, 400],
                 [210, 70, 2400, 500],
                 [210, 70, 2600, 300],
                 [210, 70, 2200, 350]]

        level2 = [[210, 70, 600, 500],

                 [210, 70, 275, 600],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [210, 70, 1800, 300],
                 [210, 70, 2000, 400],
                 [210, 70, 2200, 350]]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for block in level:
            block = Block(block[0], block[1], block [2])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


        block = MovingPlatform(70, 40)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)



class Level_02(Level):


    def __init__(self, player):


        Level.__init__(self, player)

        self.level_limit = -1000

        #
        level = [[210, 70, 600, 500],
                 [210, 70, 275, 600],
                 [210, 70, 200, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [210, 70, 1800, 300],
                 [210, 70, 2200, 350]]
        level2 = [[210, 70, 600, 500],
                 [210, 70, 275, 600],
                 [210, 70, 800, 400],
                 [210, 70, 1800, 300],
                 [210, 70, 2000, 400],
                 [210, 70, 2200, 350]]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        for block in level:
            block = Block(block[0], block[1], block [2])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_03(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[210, 70, 500, 550],
                 [210, 70, 685, 400],
                 [210, 70, 956, 500],
                 [210, 70, 1239, 300],
                 [210, 70, 1456, 200],
                 [210, 70, 1550, 500],
                 ]
        level2 = [[210, 70, 500, 550],
                 [210, 70, 800, 400],
                 [210, 70, 1120, 500],
                 [210, 70, 1400, 280],
                 ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for block in level2:
            block = Block(block[0], block[1], block [2])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        block = MovingPlatform(70, 70)
        block.rect.x = 1700
        block.rect.y = 500
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
class Level_04(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        Level.__init__(self, player)

        self.level_limit = -1000


        level = [[210, 70, 600, 500],
                 [210, 70, 275, 600],
                 [210, 70, 900, 400],
                 [210, 70, 1200, 500],
                 [210, 70, 1420, 280],
                 [210, 70, 1700, 300],
                 [210, 70, 1900, 400],
                 [210, 70, 2200, 350]]
        level2 = [[210, 70, 600, 500],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [210, 70, 1800, 300],
                 [210, 70, 2000, 400],
                 [210, 70, 2200, 350]]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        for block in level:
            block = Block(block[0], block[1], block [2])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        # Add a custom moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

def intro_screen():
    done = False
    my_font = pygame.font.SysFont("tahoma", 26, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        background_image = pygame.image.load("images.jpg")
        text = my_font.render("You're running late! Can you make it to your meeting?", True, RED)
        text1 = my_font.render("Don't run into any cars and don't hit the floor!", True, WHITE)
        text2 = my_font.render("Use the arrow keys to move, space bar to jump.", True, WHITE)

        screen.blit(text, [30, 200])
        screen.blit(text2, [78, 250])
        screen.blit(text1, [100, 300])
        pygame.display.flip()
        clock.tick(60)


intro_screen()

def game_screen():
    done = False
    my_font = pygame.font.SysFont("tahoma", 40, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        text3 = my_font.render("GAME OVER!", True, RED)
        text4 = my_font.render("You missed your meeting!", True, WHITE)
        screen.blit(text3, [265, 225])
        screen.blit(text4, [147, 260])

        pygame.display.flip()
        clock.tick(60)
def win_screen():
    done = False
    my_font = pygame.font.SysFont("tahoma", 40, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(BLACK)
        text5 = my_font.render("NICE JOB!", True, GREEN)
        text6 = my_font.render("You made it to your meeting on time!", True, GREEN)
        screen.blit(text5, [300, 225])
        screen.blit(text6, [25, 300])

        pygame.display.flip()
        clock.tick(60)
def main():
    """ Main Program """
    pygame.init()
    background_music = pygame.mixer.Sound("blast_off!(wav).wav")
    death_sound = pygame.mixer.Sound("PAIN.wav")
    background_music.set_volume(0.2)
    background_music.play(-1)

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with moving platforms")


    player = Player()

    #levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))




    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    done = False


    clock = pygame.time.Clock()
    all_sprites_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()

    cool_hit_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()
    for i in range(3):

        block = Block(BLACK, 20, 15)


        block.rect.x = random.randrange(SCREEN_WIDTH)
        block.rect.y = random.randrange(SCREEN_HEIGHT)


        block_list.add(block)
        all_sprites_list.add(block)

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()


        active_sprite_list.update()

        current_level.update()
        font = pygame.font.SysFont('Calibri', 25, True, False)
        hit_list = pygame.sprite.spritecollide(player, enemy_list, False)

        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)


        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            if current_level_no < len(level_list)-1:
                player.rect.x = 120
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        current_level.draw(screen)
        active_sprite_list.draw(screen)
        all_sprite_list.draw(screen)

        hit_list = pygame.sprite.spritecollide(player, wall_list, False)
        for wall in hit_list:
            player.health -= 1
            if player.health <= 0:
                done = True
            death_sound.play()
            game_screen()

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
