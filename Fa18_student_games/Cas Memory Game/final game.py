import pygame
import random
import time
pygame.init()
pygame.mixer.init()

size = (700, 650)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 102, 0)
RED = (153, 0, 0)
YELLOW = (255, 255, 153)
BLUE = (0, 92, 230)

# Flash colours
GREENFLASH = (0, 230, 0)
REDFLASH = (255, 26, 26)
YELLOWFLASH = (255, 255, 0)
BLUEFLASH = (102, 163, 255)

# defining variables
levelfont = pygame.font.SysFont('Calibri', 30, False, False)
instructionfont = pygame.font.SysFont('Calibri', 45, True, False)
gameoverfont = pygame.font.SysFont('Calibri', 100, True, False)
failed = False
delay = 0.25
nextlevel = False
level = 1
inlevel = True
text = levelfont.render("Level: " + str(level), True, WHITE)
instructions = instructionfont.render("Just repeat the pattern!", True, WHITE)
gameovertext = gameoverfont.render("Game Over!", True, WHITE)

# the pattern
playerlist = []
computerlist = []

# background music
pygame.mixer.music.load("Jacoo_-_If_You_Only_Knew_Original-164402528.ogg")
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# sounds
levelup_sound = pygame.mixer.Sound("level up.ogg")
levelup_sound.set_volume(.4)
green_click = pygame.mixer.Sound("Green.ogg")
green_click.set_volume(2)
red_click = pygame.mixer.Sound("Red.ogg")
red_click.set_volume(2.5)
yellow_click = pygame.mixer.Sound("Yellow.ogg")
yellow_click.set_volume(4.5)
blue_click = pygame.mixer.Sound("Blue.ogg")
blue_click.set_volume(3)
# functions
def levelup():
    computerlist.append(random.randrange(0, 4))
    levelup_sound.play()
    if level != len(computerlist):
        print("error with the leveling program")

'''def flashpattern():
    for i in range(len(computerlist)):
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, (51, 51, 276, 251))
        pygame.draw.rect(screen, RED, (375, 51, 276, 251))
        pygame.draw.rect(screen, YELLOW, (51, 350, 276, 251))
        pygame.draw.rect(screen, BLUE, (375, 350, 276, 251))
        pygame.display.flip()
        time.sleep(delay)
        if computerlist[i] == 0:
            pygame.draw.rect(screen, GREENFLASH, (51, 51, 274, 249))
            pygame.display.flip()
            green_click.play()
            time.sleep(delay)
            pygame.draw.rect(screen, GREEN, (51, 51, 274, 249))
            pygame.display.flip()
        elif computerlist[i] == 1:
            pygame.draw.rect(screen, REDFLASH, (375, 51, 276, 249))
            pygame.display.flip()
            red_click.play()
            time.sleep(delay)
            pygame.draw.rect(screen, RED, (375, 51, 276, 249))
            pygame.display.flip()
        elif computerlist[i] == 2:
            pygame.draw.rect(screen, YELLOWFLASH, (51, 350, 274, 251))
            pygame.display.flip()
            yellow_click.play()
            time.sleep(delay)
            pygame.draw.rect(screen, YELLOW, (51, 350, 274, 251))
            pygame.display.flip()
        elif computerlist[i] == 3:
            pygame.draw.rect(screen, BLUEFLASH, (375, 350, 276, 251))
            pygame.display.flip()
            blue_click.play()
            time.sleep(delay)
            pygame.draw.rect(screen, BLUE, (375, 350, 276, 251))
            pygame.display.flip()
        else:
            print("error with the flash")'''

# original screen
screen.fill(BLACK)
screen.blit(instructions, [150, 310])
pygame.draw.rect(screen, GREEN, (51, 51, 276, 251))
pygame.draw.rect(screen, RED, (375, 51, 276, 251))
pygame.draw.rect(screen, YELLOW, (51, 350, 276, 251))
pygame.draw.rect(screen, BLUE, (375, 350, 276, 251))
screen.blit(text, [25, 15])
computerlist.append(random.randrange(0, 4))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.constants.USEREVENT:
            pygame.mixer.music.play()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            if mouse_x >= 51 and mouse_x <= 315 and mouse_y >= 51 and mouse_y <= 290:
                playerlist.append(0)
                green_click.play()
            elif mouse_x >= 375 and mouse_x <= 641 and mouse_y >= 51 and mouse_y <= 290:
                playerlist.append(1)
                red_click.play()
            elif mouse_x >= 51 and mouse_x <= 315 and mouse_y >= 350 and mouse_y <= 591:
                playerlist.append(2)
                yellow_click.play()
            elif mouse_x >= 375 and mouse_x <= 641 and mouse_y >= 350 and mouse_y <= 591:
                playerlist.append(3)
                blue_click.play()
            else:
                print("you clicked somewhere else")

    screen.fill(BLACK)
    screen.blit(instructions, [150, 310])
    pygame.draw.rect(screen, GREEN, (51, 51, 276, 251))
    pygame.draw.rect(screen, RED, (375, 51, 276, 251))
    pygame.draw.rect(screen, YELLOW, (51, 350, 276, 251))
    pygame.draw.rect(screen, BLUE, (375, 350, 276, 251))
    screen.blit(text, [25, 15])

    # checks to see if player is matching the pattern
    for i in range(len(computerlist)):
        if len(playerlist) <= i:
            nextlevel = False
        elif computerlist[i] == playerlist[i]:
            if computerlist == playerlist:
                nextlevel = True
        elif computerlist[i] >= playerlist[i] or computerlist[i] <= playerlist[i]:
            failed = True
        else:
            print("error with the checking program")

    text = levelfont.render("Level: " + str(level), True, WHITE)

    # level logic
    if nextlevel:
        level += 1
        playerlist = []
        time.sleep(.2)
        levelup()
        pygame.draw.line(screen, BLACK, (0, 0), (700, 0), 100)
        screen.blit(text, [25, 15])
        # flashpattern()


    print(computerlist)

    if level == 6:
        delay = .1

    # if they lose
    if failed:
        done = True
        print("you failed")

    pygame.display.flip()
    clock.tick(60)