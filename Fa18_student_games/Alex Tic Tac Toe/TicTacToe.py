board = [1, 2, 3, 4, 5, 6, 7, 8, 9]



import pygame

# define some colors
BLACK = (0, 0, 0)  # red, green and blue
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.init()


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

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([150, 100])
        self.color = GRAY
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = 65
        self.rect.y = 50

my_font = pygame.font.SysFont("Calibri", 40, True, False)
def intro_screen():
    done = False
    frame = 0
    my_font = pygame.font.SysFont("Calibri", 40, True, False)
    while not done:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(BLACK)
        my_text = my_font.render("Welcome to Tic Tac Toe!", True, WHITE)
        screen.blit(my_text, [175, 50])
        other_text = my_font.render("Red goes first.", True, RED)
        screen.blit(other_text, [220, 100])
        again_text = my_font.render("Made by: Alex Feitler", True, WHITE)
        screen.blit(again_text, [175, 400])
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

def check_win(board):
    if board[0].color == board[1].color and board[1].color == board[2].color and board[0].color and board[0].color != GRAY:
        if turn == BLUE:
            msg = "RED"
        else:
            msg = "BLUE"
        win_text = my_font.render(msg + " wins!", True, BLACK)
        screen.blit(win_text, [250, 450])
    if board[3].color == board[4].color and board[4].color == board[5].color and board[3].color and board[
        3].color != GRAY:
        if turn == BLUE:
            msg = "RED"
        else:
            msg = "BLUE"
        win_text = my_font.render(msg + " wins!", True, BLACK)
        screen.blit(win_text, [250, 450])
    if board[6].color == board[7].color and board[7].color == board[8].color and board[6].color and board[
        6].color != GRAY:
        if turn == BLUE:
            msg = "RED"
        else:
            msg = "BLUE"
        win_text = my_font.render(msg + " wins!", True, BLACK)
        screen.blit(win_text, [250, 450])
    if board[0].color == board[3].color and board[3].color == board[6].color and board[0].color and board[
        0].color != GRAY:
        if turn == BLUE:
            msg = "RED"
        else:
            msg = "BLUE"
        win_text = my_font.render(msg + " wins!", True, BLACK)
        screen.blit(win_text, [250, 450])
    if board[1].color == board[4].color and board[4].color == board[7].color and board[1].color and board[
        1].color != GRAY:
        if turn == BLUE:
            msg = "RED"
        else:
            msg = "BLUE"
        win_text = my_font.render(msg + " wins!", True, BLACK)
        screen.blit(win_text, [250, 450])
    if board[2].color == board[5].color and board[5].color == board[8].color and board[2].color and board[
        2].color != GRAY:
        if turn == BLUE:
            msg = "RED"
        else:
            msg = "BLUE"
        win_text = my_font.render(msg + " wins!", True, BLACK)
        screen.blit(win_text, [250, 450])
    if board[0].color == board[4].color and board[4].color == board[8].color and board[0].color and board[
        0].color != GRAY:
        if turn == BLUE:
            msg = "RED"
        else:
            msg = "BLUE"
        win_text = my_font.render(msg + " wins!", True, BLACK)
        screen.blit(win_text, [250, 450])
    if board[2].color == board[4].color and board[4].color == board[6].color and board[2].color and board[
        2].color != GRAY:
        if turn == BLUE:
            msg = "RED"
        else:
            msg = "BLUE"
        win_text = my_font.render(msg + " wins!", True, BLACK)
        screen.blit(win_text, [250, 450])

def check_draw(board):
    for block in board:
        if block.color == GRAY:
            break
    else:
        win_text = my_font.render("It's a Draw", True, BLACK)
        screen.blit(win_text, [250, 450])


all_sprites_group = pygame.sprite.Group()

for i in range(9):
    block = Block()
    all_sprites_group.add(block)
    board[i] = block

print(board)

for i in range(len(board)):
    if i < 3:
        board[i].rect.topleft = (50 + 200 * i, 50)
    elif i < 6:
        board[i].rect.topleft = (50 + 200 * i - 600, 200)
    else:
        board[i].rect.topleft = (50 + 200 * i - 1200, 350)



intro_screen()

'''
self.image = pygame.draw.rect(screen, WHITE, [50, 50, 165, 120])
self.image = pygame.draw.rect(screen, WHITE, [250, 50, 165, 120])
self.image = pygame.draw.rect(screen, WHITE, [450, 50, 165, 120])
self.image = pygame.draw.rect(screen, WHITE, [50, 200, 165, 120])
self.image = pygame.draw.rect(screen, WHITE, [250, 200, 165, 120])
self.image = pygame.draw.rect(screen, WHITE, [450, 200, 165, 120])
self.image = pygame.draw.rect(screen, WHITE, [50, 350, 165, 120])
self.image = pygame.draw.rect(screen, WHITE, [250, 350, 165, 120])
self.image = pygame.draw.rect(screen, WHITE, [450, 350, 165, 120])
'''
# Sound
'''
Imagine the music
button_sound = pygame.mixer.Sound('button-1.ogg')

background_music = pygame.mixer.Sound("bg.ogg")
background_music.set_volume(0.5)
background_music.play()
'''


x = 0
turn = RED

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            #button_sound.play(1)
            for block in all_sprites_group:
                if block.rect.collidepoint(event.pos):
                   if block.color == GRAY:
                       if turn == RED:
                           block.color = turn
                           block.image.fill(block.color)
                           turn = BLUE
                       else:
                           block.color = turn
                           block.image.fill(block.color)
                           turn = RED
                       check_win(board)


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    pygame.draw.line(screen, BLACK, [225, 50], [225, 450], 10)
    pygame.draw.line(screen, BLACK, [425, 50], [425, 450], 10)
    pygame.draw.line(screen, BLACK, [50, 175], [600, 175], 10)
    pygame.draw.line(screen, BLACK, [50, 325], [600, 325], 10)

    # Sprites in board
    pygame.draw.rect(screen, WHITE, [50, 50, 165, 120])
    pygame.draw.rect(screen, WHITE, [250, 50, 165, 120])
    pygame.draw.rect(screen, WHITE, [450, 50, 165, 120])
    pygame.draw.rect(screen, WHITE, [50, 200, 165, 120])
    pygame.draw.rect(screen, WHITE, [250, 200, 165, 120])
    pygame.draw.rect(screen, WHITE, [450, 200, 165, 120])
    pygame.draw.rect(screen, WHITE, [50, 350, 165, 120])
    pygame.draw.rect(screen, WHITE, [250, 350, 165, 120])
    pygame.draw.rect(screen, WHITE, [450, 350, 165, 120])
    all_sprites_group.draw(screen)

    check_win(board)
    check_draw(board)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second

    clock.tick(60)




