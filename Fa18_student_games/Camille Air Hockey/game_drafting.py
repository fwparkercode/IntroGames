import pygame
import math
import random
pygame.init()

# Define some colors
BLACK = (0, 0, 0)  # (red, green, blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Template")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width / 2
        self.rect.centery = screen_height / 2

        # count the number of joysticks
        self.joystick_count = pygame.joystick.get_count()
        if self.joystick_count == 0:
            print("Error, I didn't find any joysticks.")
        else:
            self.my_joystick = pygame.joystick.Joystick(0)
            self.my_joystick.init()

    def update(self):
        if self.joystick_count != 0:
            # This gets the position of the axis on the game controller
            # It returns a number between -1.0 and +1.0
            horiz_axis_pos = self.my_joystick.get_axis(0)
            vert_axis_pos = self.my_joystick.get_axis(1)

            # Move x according to the axis. We multiply by 10 to speed up the
            # movement.
            self.rect.x = self.rect.x + horiz_axis_pos * 10
            self.rect.y = self.rect.y + vert_axis_pos * 10

        # stick to wall
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height



player1 = Player()


class Puck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        # self.image = pygame.image.load("puck.png")
        self.rect = self.image.get_rect()
        self.speed = 1
        self.angle = 0

    def update(self):
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed

        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.right >= screen_width:
            self.angle = math.pi - self.angle

            # check for boundary collision
            hit_list = pygame.sprite.spritecollide(self, self.boundary_list, False)
            for boundary in hit_list:
                # MOVE X
                if self.vx > 0:
                    self.rect.right = boundary.rect.left
                    self.angle = math.pi - self.angle
                    self.speed *= self.elasticity
                else:
                    self.rect.left = boundary.rect.right
                    self.angle = -(self.angle - math.pi)
                    self.speed *= self.elasticity

                self.rect.centerx = int(self.x)  # move the rect to reflect the x move

    hit_list = pygame.sprite.spritecollide(self, self.boundary_list, False)
    for boundary in hit_list:
        if self.vy > 0:
            self.rect.bottom = boundary.rect.top
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity
        else:
            self.rect.top = boundary.rect.bottom
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity

        self.rect.centery = int(self.y)

    # check for net collision
    net_hit_list = pygame.sprite.spritecollide(self, self.net_list, False)
    for net in net_hit_list:
        # MOVE X
        if self.vx > 0:
            self.rect.right = net.rect.left
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity
        else:
            self.rect.left = net.rect.right
            self.angle = -(self.angle - math.pi)
            self.speed *= self.elasticity

        self.rect.centerx = int(self.x)  # move the rect to reflect the x move

    net_hit_list = pygame.sprite.spritecollide(self, self.net_list, False)
    for net in net_hit_list:
        if self.vy > 0:
            self.rect.bottom = net.rect.top
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity
        else:
            self.rect.top = net.rect.bottom
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity

        self.rect.centery = int(self.y)
    def draw(self):
        pygame.draw.ellipse(screen, BLACK, [10, 10, 10, 10])


class Net(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface([2, 60])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = screen_height / 2
        self.rect.x = x

# instances of Net
net_left = Net(30)
net_right = Net(screen_width - 30)

boundary_list.add(net_right)
boundary_list.add(net_left)

boundary_left_top = Boundary(45, screen_height / 2 - 30)
boundary_left_bottom = Boundary(45, screen_height / 2 + 28)
boundary_right_top = Boundary(825, screen_height / 2 - 30)
boundary_right_bottom = Boundary(825, screen_height / 2 + 28)
boundary_list.add(boundary_left_top)
boundary_list.add(boundary_left_bottom)
boundary_list.add(boundary_right_top)
boundary_list.add(boundary_right_bottom)

all_sprites_group.add(boundary_right_top)
all_sprites_group.add(boundary_right_bottom)
all_sprites_group.add(net_left)
all_sprites_group.add(net_right)

puck = Puck()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here


    puck.draw()
    puck.update()
    player1.update()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

game_over = my_font.render("Game Over", True, RED)
        screen.blit(screen, game_over, [screen_width / 2, screen_height / 2])

screen.blit(screen, game_over, [screen_width / 2, screen_height / 2])
game_over()
game_over = my_font.render("Game Over", True, RED)