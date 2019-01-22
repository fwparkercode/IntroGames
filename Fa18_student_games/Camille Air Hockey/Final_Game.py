"""
 Pygame base template for opening a window

 Intro to Programming
 Camille Freedman 2018

 Explanation video: http://youtu.be/vRB_983kUMc
"""
import random
import math
import pygame


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
screen_width = 900
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hockey")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Score

score1 = 0
score2 = 0


# Player Class

class Player(pygame.sprite.Sprite):

    def __init__(self, joystick_no, x, color):
        super().__init__()
        self.radius = 15
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = screen_height / 2
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.joystick = None
        self.color = color

        # count the number of joysticks
        self.joystick_count = pygame.joystick.get_count()
        print(self.joystick_count)

        if self.joystick_count <joystick_no + 1:
            print("Error, I didn't find any joysticks.")

        else:
            self.joystick = pygame.joystick.Joystick(joystick_no)
            self.joystick.init()

    def update(self):
        if self.joystick != None:
            # get the position of the axis on the game controller
            # It returns a number between -1.0 and +1.0
            self.horiz_axis_pos = self.joystick.get_axis(0)
            self.vert_axis_pos = self.joystick.get_axis(1)
            if abs(self.vert_axis_pos) < 0.05:
                self.vert_axis_pos = 0
            if abs(self.horiz_axis_pos) < 0.05:
                self.horiz_axis_pos = 0
            print(self.horiz_axis_pos, self.vert_axis_pos)

            # Move x according to the axis. multiply by 10 to speed up the movement.
            self.rect.x = self.rect.x + self.horiz_axis_pos * 10
            self.rect.y = self.rect.y + self.vert_axis_pos * 10

        # stick to player to the sides of the screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    def draw_me(self):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)


# instances of the player class
player1 = Player(0, 200, GREEN)
player2 = Player(1, 600, MAGENTA)


# Class for the Puck


class Puck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.elasticity = 0.95  # 1.0 is perfectly elastic, 0 is perfectly inelastic
        self.friction = 0.005  # friction applied:  0 is none
        self.radius = 15
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.vx = 0
        self.vy = 0  # velocity x and y
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.speed = random.randrange(-5, 6)
        self.angle = random.random() * math.pi * 2

    def draw_me(self):
        pygame.draw.circle(screen, BLACK, self.rect.center, 10)

    def update(self):
        # friction
        self.speed *= (1 - self.friction)  # slow down the puck as it slides across ice
        if self.speed < 0.1:
            # stop the puck if it gets really slow
            self.speed = 0

        #  MOVE X
        # always do x and y separately to avoid collision errors
        self.vx = math.cos(self.angle) * self.speed
        self.x += self.vx

        # check for edge collision
        if self.x + self.radius >= screen_width:
            self.x = screen_width - self.radius
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.angle = -(self.angle - math.pi)
            self.speed *= self.elasticity

        self.rect.centerx = int(self.x)  # move the rect to reflect the x move

        #  MOVE Y
        self.vy = -math.sin(self.angle) * self.speed
        self.y += self.vy

        # check for edge collision
        if self.y + self.radius >= screen_height:
            self.y = screen_height - self.radius
            self.angle = (math.pi * 3/2 - self.angle) + math.pi/2
            self.speed *= self.elasticity

        if self.y <= self.radius:
            self.y = self.radius
            self.angle = math.pi / 2 - self.angle + math.pi * 3/2
            self.speed *= self.elasticity

        self.rect.centery = int(self.y)

    def move_back(self):
        # undo the collision condition by moving back where you were
        # if you don't do this, you risk vibrating in place on edge of puck
        self.x -= self.vx
        self.y -= self.vy


# instance of the puck
puck = Puck()
puck.x, puck.y = puck.rect.center

# Goal Class


class Goal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 60])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centery = screen_height / 2


# instances of the goals
goal_left = Goal()
goal_left.rect.right = 90

goal_right = Goal()
goal_right.rect.left = 810

# goal group
goal_left_group = pygame.sprite.Group()
goal_left_group.add(goal_left)
goal_right_group = pygame.sprite.Group()
goal_right_group.add(goal_right)

# Goal Boundary Class


class Boundary(pygame.sprite.Sprite):

    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface([60, 80])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = screen_height / 2
        self.rect.x = x


# instances of the boundary
boundary_left = Boundary(15)
boundary_right = Boundary(825)

# boundary group
boundary_list = pygame.sprite.Group()
boundary_list.add(boundary_right)
boundary_list.add(boundary_left)
puck.boundary_list = boundary_list


# FUNCTIONS


def collision_calc(puck, player):
    # deltas between two circles
    dx = puck.x - player.rect.centerx
    dy = puck.y - player.rect.centery

    # calculate the angle between the two centers using atan2
    # puck is effectively bouncing off a "wall" placed on the tangent of the two circles at collision pt
    # atan2 was invented for programming, it gives an unambiguous (0 to 360) angle for a vector.
    angle_to = math.atan2(-dy, dx) - math.pi    # normal angle in direction of contact (-dy due to inverted axis)
    print("angle_to", math.degrees(angle_to))
    print("angle", math.degrees(puck.angle))

    # Now you have to rotate the axis to make it look like it is bouncing off the tangent.
    puck.angle = (puck.angle + 2 * (angle_to - puck.angle)) % (math.pi * 2) + math.pi

    puck.speed *= puck.elasticity  # lose energy when you bounce based on elasticity
    puck.vx += player.horiz_axis_pos * 10
    puck.vy += player.vert_axis_pos * 10
    puck.speed = math.hypot(puck.vx, puck.vy)


# creating all sprites group groups
all_sprites_group = pygame.sprite.Group()

# adding sprites to groups
all_sprites_group.add(boundary_left)
all_sprites_group.add(boundary_right)
all_sprites_group.add(goal_left)
all_sprites_group.add(goal_right)
all_sprites_group.add(puck)
all_sprites_group.add(player1)
all_sprites_group.add(player2)


# Sound Resources
background_music = pygame.mixer.Sound("background.wav")
background_music.set_volume(0.85)
background_music.play(-1)

goal_sound = pygame.mixer.Sound("goal.wav")
bump_sound = pygame.mixer.Sound("bump.wav")
bump_sound.set_volume(0.5)

# make my font(s)
my_font = pygame.font.SysFont('Cambria', 20, True, False)


# intro screen
def intro_screen():

    done = False
    while not done:
        # --- Intro event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        screen.fill(WHITE)

        # --- Drawing code should go here
        intro_text = my_font.render("Welcome to Air Hockey", True, BLACK)
        my_text = my_font.render("Click to Continue", True, BLACK)
        instruct_text = my_font.render("Instructions: Use game controller to move your player.", True, BLACK)
        instruct_text2 = my_font.render("Hit the puck into the opposite player's goal.", True, BLACK)
        instruct_text3 = my_font.render("When one player gets 5 goals, the game is over.", True, BLACK)

        # blit the text to the screen.
        screen.blit(my_text, [screen_width / 2 - 50, screen_height / 2])
        screen.blit(intro_text, [screen_width / 2 - 50, screen_height / 2 - 25])
        screen.blit(instruct_text, [50, 50])
        screen.blit(instruct_text2, [50, 100])
        screen.blit(instruct_text3, [50, 150])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


intro_screen()

# Game Over Screen


def game_over():

    done = False
    while not done:
        # --- Game Over event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        screen.fill(WHITE)

        # --- Drawing code should go here
        game_over_text = my_font.render("The game is over.", True, BLACK)
        again_text = my_font.render("Click to keep playing.", True, BLACK)

        # blit the text to the screen
        screen.blit(again_text, [screen_width / 2 - 50, screen_height / 2])
        screen.blit(game_over_text, [screen_width / 2 - 50, screen_height / 2 - 25])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # checking for collision with boundary
    boundary_hit_list = pygame.sprite.spritecollide(puck, boundary_list, False)
    for hit in boundary_hit_list:
        bump_sound.play()
        puck.angle = math.atan2(puck.vy, puck.vx)
        puck.vx *= -1
        puck.vy *= -1

    # checking for goal on left goal
    goal_left_list = pygame.sprite.spritecollide(puck, goal_left_group, False)
    for goal_left in goal_left_list:
        score2 += 1
        print(score2)
        goal_sound.play()
        puck.__init__()

    # checking for goal on right goal
    goal_right_list = pygame.sprite.spritecollide(puck, goal_right_group, False)
    for goal in goal_right_list:
        score1 += 1
        print(score1)
        goal_sound.play()
        puck.__init__()

    # ending the game if someone gets 5 points
    if score1 == 5:
        game_over()
        score1 = 0
        score2 = 0

    if score2 == 5:
        game_over()
        score1 = 0
        score2 = 0


    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here

    all_sprites_group.update()
    all_sprites_group.draw(screen)
    puck.draw_me()
    player1.draw_me()
    player2.draw_me()


    # checking for puck and player collision
    if pygame.sprite.collide_circle(puck, player1):
        bump_sound.play()
        puck.move_back()  # move back to undo the collision condition
        collision_calc(puck, player1)  # geometry to change puck angle

    if pygame.sprite.collide_circle(puck, player2):
        bump_sound.play()
        puck.move_back()  # move back to undo the collision condition
        collision_calc(puck, player2)  # geometry to change puck angle

    # Background #

    # red circles

    pygame.draw.ellipse(screen, RED, [screen_width / 8, 50, 150, 150], 2)
    pygame.draw.ellipse(screen, RED, [screen_width - 262, 50, 150, 150], 2)
    pygame.draw.ellipse(screen, RED, [screen_width / 8, screen_height - 200, 150, 150], 2)
    pygame.draw.ellipse(screen, RED, [screen_width - 262, screen_height - 200, 150, 150], 2)

    # red dotted line
    line_y = 0
    for i in range(100):
        pygame.draw.line(screen, RED, [screen_width / 2, line_y], [screen_width / 2, line_y + 5], 2)
        line_y += 10

    # red lines
    red_line_x = 0
    for i in range(2):
        pygame.draw.line(screen, RED, [screen_width - 825 + red_line_x, 0], [screen_width - 825 + red_line_x, screen_height], 2)
        red_line_x += 750

    # blue lines
    line_x = 0
    for i in range(2):
        pygame.draw.line(screen, BLUE, [line_x + 350, 0], [line_x + 350, screen_height], 2)
        line_x += 200

    # blue circle
    pygame.draw.ellipse(screen, BLUE, [screen_width / 2 - 75, screen_height / 2 - 75, 150, 150], 2)

    # drawing the score

    score1_text = my_font.render("Score: " + str(score1), True, MAGENTA)
    score2_text = my_font.render("Score: " + str(score2), True, GREEN)

    screen.blit(score1_text, [50, 50])
    screen.blit(score2_text, [800, 50])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()