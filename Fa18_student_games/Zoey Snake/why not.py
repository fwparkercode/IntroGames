import pygame
import random

screen_width = 600
screen_height = 400

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (178, 207, 255)
PINK = (168, 94, 153)
BLUE = (0, 0, 255)
PURPLE = (234, 191, 239)
TEAL = (128, 191, 183)

# Make Snake Blocks
segment_width = 10
segment_height = 10
segment_margin = 2

# Make Snake Start Speed
x_change = segment_width + segment_margin
y_change = 0

# Set x and y Variables
x = random.randrange(600)
y = random.randrange(400)

# Lists
all_sprites_list = pygame.sprite.Group()  # stores all the sprites in one group
block_list = pygame.sprite.Group()  # stores all of the blocks for the snake to eat in one group
blocks_hit_list = pygame.sprite.Group()  # stores all of the snakes hit blocks in one group
segment_list = pygame.sprite.Group()  # stores all of he snake segments in one group


# Intro and Outro Screens

def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(LIGHT_BLUE)
        text = my_font.render("WELCOME TO SNAKE!", True, WHITE)
        text2 = my_font.render("Collect the teal blocks to grow!", True, WHITE)
        text5 = my_font.render("Hit the wall and you'll die!", True, WHITE)
        text3 = my_font.render("Use the arrow keys to control the snake's location!", True, WHITE)
        text4 = my_font.render("Press the mouse button to begin!", True, WHITE)
        text6 = my_font.render("Try to get the highest score you can without dying!", True, WHITE)
        screen.blit(text4, [0, 250])
        screen.blit(text, [0, 0])
        screen.blit(text2, [0, 50])
        screen.blit(text3, [0, 200])
        screen.blit(text5, [0, 100])
        screen.blit(text6, [0, 150])
        pygame.display.flip()
        clock.tick(60)


def outro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(LIGHT_BLUE)
        text = my_font.render("YOU DIED!", True, WHITE)
        text2 = my_font.render("THANKS FOR PLAYING.", True, WHITE)
        screen.blit(text, [0, 0])
        screen.blit(text2, [0, 30])
        pygame.display.flip()
        clock.tick(60)


# Classes
class Segment(pygame.sprite.Sprite):  # creates one snake segment as a sprite
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(LIGHT_BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2


pygame.init()


class Block(pygame.sprite.Sprite):  # creates on block as a sprite
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(TEAL)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(11, screen_width - 11)
        self.rect.y = random.randrange(11, screen_height - 11)


class Wall(pygame.sprite.Sprite):  # makes the wall so the snake dies if it hits the edge
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


# Create the Screen
screen = pygame.display.set_mode([600, 400])

# Set the name of the Window
pygame.display.set_caption("Zoey Snake Final")

# Put the walls on the edge of the screen
wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 10, 400)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(10, 0, 600, 10)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(590, 10, 400, 400)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(0, 390, 600, 10)
wall_list.add(wall)
all_sprites_list.add(wall)


# Create the initial Snake
snake_segments = []
for i in range(3):
    x = random.randrange(screen_width / 4, screen_width * 3 / 4) - (segment_width + segment_margin) * i
    y = random.randrange(screen_height / 4, screen_height * 3 / 4)
    segment = Segment()
    snake_segments.append(segment)
    segment_list.add(segment)
    all_sprites_list.add(segment)


clock = pygame.time.Clock()
done = False

# Get first Block on the Screen
block = Block()
all_sprites_list.add(block)
block_list.add(block)

# Run the Intro screen
intro_screen()

# Create the Score
score = len(snake_segments) - 3

# Background Music Resources
background_music = pygame.mixer.Sound('backgroundmusic.aiff')

# Start Music
background_music.play()

# Main Event Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN: # Makes the snake move when you hit the keys
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)

    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    all_sprites_list.update()
    old_segment = snake_segments.pop()
    all_sprites_list.remove(old_segment)

    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment()

    # Insert new segment into the list
    snake_segments.insert(0, segment)
    all_sprites_list.add(segment)
    segment_list.add(segment)

    # Sprites Colliding
    for segment in segment_list:
        blocks_hit_list = pygame.sprite.spritecollide(segment, block_list, True)  # adds new segment to the end of snake
        for block in blocks_hit_list:
            segment = Segment()
            # Insert new segment into the list
            snake_segments.append(segment)
            all_sprites_list.add(segment)
            segment_list.add(segment)
            # Draw New Block
            block = Block()
            all_sprites_list.add(block)
            block_list.add(block)
            my_sound = pygame.mixer.Sound("collect.wav")
            my_sound.play()
            score += 1
            print(score)

        wall_hit_list = pygame.sprite.spritecollide(segment, wall_list, True)  # dies if you hit wall
        for segment in wall_hit_list:
            all_sprites_list.empty()
            segment_list.empty()
            done = True
            outro_screen()

        '''self_hit_list = pygame.sprite.spritecollide(segment, segment_list, False)
        if len(self_hit_list) > 1:
            segment_list.empty()
            all_sprites_list.empty()
            outro_screen()'''
        # when the above section is not commented out then it dies when it hits a teal block too

    # Clear the Screen
    screen.fill(PINK)
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    text = my_font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [10, 10])
    all_sprites_list.draw(screen)

    # Flip the Screen
    pygame.display.flip()

    # Pause
    clock.tick(score + 5)

pygame.quit()