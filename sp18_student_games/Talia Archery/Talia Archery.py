import pygame
import random
import math

# arrows stay where you click and if they land on one of the colors it will give you points.
# if you get above 35 points you move on to the next level
# it goes faster as the levels go up

if __name__ == "__main__":
  pass

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (109, 165, 255)
YELLOW = (242, 216, 19)
LIGHT_BLUE = (147, 177, 226)
PINK = (170, 78, 183)
COOL = (10, 126, 155)
FRAME_RATE = 60

pygame.init()

font = pygame.font.SysFont("Times New Roman", 42)
# ARROW_MISS = font.render("x", True, RED)
ARROW_HIT = font.render("x", True, BLACK)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
# done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

background_sound = pygame.mixer.Sound("ShootClean.wav")
arrow_sound = pygame.mixer.Sound("Arrow+Swoosh+1.wav")
my_font = pygame.font.SysFont('Times New Roman', 25, True, False)


def draw_target(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 200, 200])
    # score += 5
    pygame.draw.ellipse(screen, BLACK, [25 + x, 25 + y, 150, 150])
    # score += 6
    pygame.draw.ellipse(screen, BLUE, [50 + x, 50 + y, 100, 100])
    # score += 7
    pygame.draw.ellipse(screen, RED, [70 + x, 70 + y, 60, 60])
    # score += 8
    pygame.draw.ellipse(screen, YELLOW, [80 + x, 80 + y, 40, 40])
    # score += 10
    # find center of yellow = x + 100 and y + 100


class Arrow:
    def __init__(self, x, y):
        self.before_counter = 0
        self.after_counter = 0
        self.x = x
        self.y = y


# xarrow, yarrow
# square root of change in x^2 + change in y^2 = r
# if statement
background_sound.set_volume(.3)
background_sound.play(-1)


def intro_screen():
    # The intro screen
    # Loop until the user clicks the close button.
    done = False
    intro_text1 = "Welcome To Arrow Game!"
    intro_text2 = "Press enter to start"

    font1 = pygame.font.SysFont("Times New Roman", 34)
    text1 = font1.render(intro_text1, True, PINK)
    font2 = pygame.font.SysFont("Times New Roman", 24)
    text2 = font2.render(intro_text2, True, COOL)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # intro_font = pygame.font.SysFont(None, 50, True, False)
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # return True
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False

        # --- Game logic should go here

        # --- Screen-clearing code goes here
        screen.fill(LIGHT_BLUE)

        screen.blit(text1, (155, 100))
        screen.blit(text2, (245, 250))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(10)
    return True


def level_screen(level_num):
    # The intro screen
    # Loop until the user clicks the close button.
    done = False
    intro_text1 = "Welcome To Level " + str(level_num) + "!"
    intro_text2 = "Press enter to start"
    intro_text3 = "You must get above a 35 to move on"

    font1 = pygame.font.SysFont("Times New Roman", 34)
    text1 = font1.render(intro_text1, True, PINK)
    font2 = pygame.font.SysFont("Times New Roman", 24)
    text2 = font2.render(intro_text2, True, COOL)
    font3 = pygame.font.SysFont("Times New Roman", 24)
    text3 = font3.render(intro_text3, True, COOL)
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # intro_font = pygame.font.SysFont(None, 50, True, False)
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # return True
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False

        # --- Game logic should go here

        # --- Screen-clearing code goes here
        screen.fill(LIGHT_BLUE)

        screen.blit(text1, (195, 100))
        screen.blit(text2, (245, 250))
        screen.blit(text3, (170, 300))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(10)
    return True


def loser_screen():
    # The intro screen
    # Loop until the user clicks the close button.
    done = False
    intro_text1 = "You Lost "
    intro_text2 = "that sucks....."

    font1 = pygame.font.SysFont("Times New Roman", 100)
    text1 = font1.render(intro_text1, True, PINK)
    font2 = pygame.font.SysFont("Times New Roman", 24)
    text2 = font2.render(intro_text2, True, COOL)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # intro_font = pygame.font.SysFont(None, 50, True, False)
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # return True
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False

        # --- Game logic should go here

        # --- Screen-clearing code goes here
        screen.fill(LIGHT_BLUE)

        screen.blit(text1, (170, 100))
        screen.blit(text2, (290, 250))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(10)
    return True


def winner_screen():
    # The intro screen
    # Loop until the user clicks the close button.
    done = False
    intro_text1 = "You Won "
    intro_text2 = "congrats!"

    font1 = pygame.font.SysFont("Times New Roman", 100)
    text1 = font1.render(intro_text1, True, PINK)
    font2 = pygame.font.SysFont("Times New Roman", 24)
    text2 = font2.render(intro_text2, True, COOL)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # intro_font = pygame.font.SysFont(None, 50, True, False)
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # return True
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False

        # --- Game logic should go here

        # --- Screen-clearing code goes here
        screen.fill(LIGHT_BLUE)

        screen.blit(text1, (170, 100))
        screen.blit(text2, (290, 250))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(10)
    return True


def level(level_num, speed):
    current_arrow = None
    num_arrows = 5
    score = 0
    x = 0
    y = 0
    x_speed = speed
    y_speed = speed
    done = level_screen(level_num)

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # return True
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN and current_arrow is None and num_arrows > 0:
                x2, y2 = pygame.mouse.get_pos()
                current_arrow = Arrow(x2, y2)
                num_arrows -= 1
                arrow_sound.play()

                # print(score)
                # calculate the distance from each and then do the points
                # mousebuttondown away from the middle

        # --- Game logic should go here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        x += x_speed
        if x > 700 - 200:
            x_speed *= -1
        if x < 0:
            x_speed *= -1
        y += y_speed
        if y > 500 - 200:
            y_speed *= -1
        if y < 0:
            y_speed *= -1

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(GREEN)

        # --- Drawing code should go here
        draw_target(x, y)

        if current_arrow is not None:
            if current_arrow.before_counter < FRAME_RATE / 3:
                current_arrow.before_counter += 1
            elif current_arrow.after_counter == 0:
                screen.blit(ARROW_HIT, (current_arrow.x - 10, current_arrow.y - 27))  # ADJUST TO BE AT CLICK LOCATION
                r = ((current_arrow.x - (x + 100)) ** 2 + (current_arrow.y - (y + 100)) ** 2) ** 0.5

                # if r < 100:
                #     arrow_hits.append((current_arrow, x - current_arrow.x, y - current_arrow.y))
                # else:
                #     arrow_misses.append((current_arrow.x, current_arrow.y))

                if r <= 18:
                    score += 10
                elif r <= 30 and r >= 18:
                    score += 8
                elif r <= 50 and r >= 30:
                    score += 7
                elif r <= 73 and r >= 50:
                    score += 6
                elif r <= 100 and r >= 73:
                    score += 5
                elif r >= 100:
                    score += 0

                current_arrow.after_counter += 1

                # current_arrow = None
            elif current_arrow.after_counter <= FRAME_RATE * 2:
                current_arrow.after_counter += 1
                screen.blit(ARROW_HIT, (current_arrow.x - 10, current_arrow.y - 27))
            else:
                current_arrow = None

        if score >= 35:
            return False
        elif num_arrows == 0 and current_arrow is None:
            done = True

        my_text = my_font.render("Score: " + str(score), True, BLACK)
        my_text_two = my_font.render("Arrows Left: " + str(num_arrows), True, BLACK)
        screen.blit(my_text, [20, 20])
        screen.blit(my_text_two, [515, 20])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FRAME_RATE)

    return True


# return True


if not intro_screen() and not level(1, 2) and not level(2, 3) and not level(3, 4):
    winner_screen()
else:
    loser_screen()

# Close the window and quit.
pygame.quit()