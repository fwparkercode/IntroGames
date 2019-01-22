"""
 Pygame base template for opening a window

Into to Programming
2018

"""

import pygame
pygame.init()
import random

# Define some colors
BLACK = (0, 0, 0)   # (red, green, blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 155)
GRAY = (120, 120, 120)
YELLOW = (255, 155, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PURPLE = (155, 0, 255)



# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
class Ball():
    def __init__(self):
        self.size = random.randrange(30, 100)
        self.brightness = random.randrange(150, 256)
        self.x = random.randrange(screen_width - self.size)
        self.y = random.randrange(screen_height - self.size)
        self.speedx = random.randrange(1, 6)
        self.speedy = 0
    def draw(self):
        pygame.draw.ellipse(screen, (155, self.brightness, 255), [self.x, self.y, self.size, self.size])
    def update(self):
        self.x += self.speedx
        if self.x > screen_width:
            self.x = -self.size
            self.y = random.randrange(screen_height - self.size)
        if self.y > screen_height:
            self.y = -self.size
            self.x = random.randrange(screen_width - self.size)
        self.y += self.speedy

class Bubble(Ball):
    def __init__(self):
        super().__init__()
        self.speedx = 0
        self.speedy = random.random() * 2
    def draw(self):
        pygame.draw.ellipse(screen, (255, self.brightness, 155), [self.x, self.y, self.size, self.size])


ball_list = []
for i in range(100):
    ball = Ball()
    ball_list.append(ball)

more_bubbles = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            more_bubbles = True
        if event.type == pygame.MOUSEBUTTONUP:
            more_bubbles = False

    # --- Game logic should go here
    if more_bubbles:
        x, y = pygame.mouse.get_pos()
        new_bubble = Bubble()
        new_bubble.x = x
        new_bubble.y = y
        ball_list.append(new_bubble)

    for ball in ball_list:
        ball.update()

    screen.fill(WHITE)

    # --- Drawing code should go here
    for ball in ball_list:
        ball.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()