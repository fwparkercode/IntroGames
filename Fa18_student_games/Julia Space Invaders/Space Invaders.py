'''
Intro to Programming
Julia Marks Final Game
Space invaders
'''


import pygame
import random
pygame.init()

# ----------------Define some colors---------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# ----------------Set height and width---------------------
screen_width = 550
screen_height = 680
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")

done = False

score = 0
lives = 3
level = 1

timer = 0

# ------------- Classes ----------------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("shooter.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 638
        self.change_x = 0
        self.reload = 0

    def changespeed(self, x):
        self.change_x += x

    def update(self):
        self.rect.x += self.change_x

        if self.rect.x > 500 - 5:
            self.rect.x = 500 - 5
        if self.rect.x < 10:
            self.rect.x = 10

        self.reload += 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 8])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.speedy = -8

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Bullet_one(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 8])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedy = + 6

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom > 680:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("creature1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 100
        self.speedx = 1
    def update(self):
        self.rect.x += self.speedx

        if self.rect.right > 570:
            self.rect.x -= self.speedx
            for enemy in enemy_group_three:
                enemy.speedx *= - 1
                enemy.rect.y += 10
        if self.rect.left < -20:
            self.rect.x -= self.speedx
            for enemy in enemy_group_three:
                enemy.speedx *= - 1
                enemy.rect.y += 10


class Shelter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Ufo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ufo.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 40
        self.speedx = 3


    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > 570:
            self.kill()


# Groups
all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
bullet_group_one = pygame.sprite.Group()
shelter_group = pygame.sprite.Group()

player = Player(0, 0)
player_group = pygame.sprite.Group()
all_sprites_group.add(player)


enemy_group = pygame.sprite.Group()
enemy_group_one = pygame.sprite.Group()
enemy_group_two = pygame.sprite.Group()
enemy_group_three = pygame.sprite.Group()
ufo_group = pygame.sprite.Group()


# Shelter
for i in range(20):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 30
        shelter.rect.y = 4 * j + 556

for i in range(20):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 170
        shelter.rect.y = 4 * j + 556

for i in range(20):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 304
        shelter.rect.y = 4 * j + 556

for i in range(20):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 440
        shelter.rect.y = 4 * j + 556


for i in range(7):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 20
        shelter.rect.y = 4 * j + 585

for i in range(7):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 93
        shelter.rect.y = 4 * j + 585

for i in range(7):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 93 + 67
        shelter.rect.y = 4 * j + 585

for i in range(7):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 230
        shelter.rect.y = 4 * j + 585

for i in range(7):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 364
        shelter.rect.y = 4 * j + 585

for i in range(7):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 294
        shelter.rect.y = 4 * j + 585

for i in range(7):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 502
        shelter.rect.y = 4 * j + 585

for i in range(7):
    for j in range(8):
        shelter = Shelter()
        all_sprites_group.add(shelter)
        shelter_group.add(shelter)
        shelter.rect.x = 4 * i + 427
        shelter.rect.y = 4 * j + 585


# Enemies
for i in range(8):
    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_group_two.add(enemy)
    enemy_group_three.add(enemy)
    enemy.image = pygame.image.load("creature3.png")
    enemy.rect.x = 50 * i + 36
    enemy.rect.y = 85

for i in range(8):
    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)
    enemy_group_three.add(enemy)
    enemy.image = pygame.image.load("creature1.png")
    enemy.rect.x = 50 * i + 36
    enemy.rect.y = 280

for i in range(8):
    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_group.add(enemy)
    enemy_group_three.add(enemy)
    enemy.image = pygame.image.load("creature1.png")
    enemy.rect.x = 50 * i + 36
    enemy.rect.y = 245

for i in range(8):
    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_group_one.add(enemy)
    enemy_group_three.add(enemy)
    enemy.image = pygame.image.load("creature2.png")
    enemy.rect.x = 50 * i + 36
    enemy.rect.y = 205

for i in range(8):
    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_group_one.add(enemy)
    enemy_group_three.add(enemy)
    enemy.image = pygame.image.load("creature2.png")
    enemy.rect.x = 50 * i + 36
    enemy.rect.y = 165

for i in range(8):
    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_group_two.add(enemy)
    enemy_group_three.add(enemy)
    enemy.image = pygame.image.load("creature3.png")
    enemy.rect.x = 50 * i + 36
    enemy.rect.y = 125


# ---------------Photos and Sounds-----------------------

shooter = pygame.image.load("shooter.png")
creature_1 = pygame.image.load("creature1.png")
creature_2 = pygame.image.load("creature2.png")
creature_3 = pygame.image.load("creature3.png")
ufo = pygame.image.load("ufo.png")
lives_pic = pygame.image.load("lives.png")


background_music = pygame.mixer.Sound("spaceinvaders1.ogg")
background_music.play(-1)


shoot_sound = pygame.mixer.Sound("shoot.wav")
shoot_sound.set_volume(0.1)
explosion_sound = pygame.mixer.Sound("explosion.wav")
explosion_sound.set_volume(0.6)
invader_killed = pygame.mixer.Sound("invaderkilled.wav")
invader_killed.set_volume(0.3)
ufo_sound = pygame.mixer.Sound("ufo.wav")
invader_killed.set_volume(0.7)


# -------Used to manage how fast the screen updates------------
clock = pygame.time.Clock()

# -----------------Fonts---------------------
my_font = pygame.font.SysFont('Orbitron', 28, True, False)

pygame.mouse.set_visible(False)

# --------------INTRO SCREEN ----------------------------

def intro_screen():
    done = False
    frame = 0
    my_font = pygame.font.SysFont('Orbitron', 80, True, False)
    my_font_one = pygame.font.SysFont('Orbitron', 42, True, False)
    logo = pygame.image.load("logo.png")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(BLACK)
        screen.blit(logo, [20, 220])

        my_text_one = my_font.render("WELCOME TO", True, WHITE)
        screen.blit(my_text_one, [52, 100])

        my_text = my_font_one.render("CLICK THE MOUSE TO CONTINUE", True, WHITE)
        screen.blit(my_text, [screen_width / 2 - 260, screen_height - 160])


        pygame.display.flip()
        clock.tick(60)

    return False

done = intro_screen()


# -------------------- GAME OVER SCREEN ------------------------

def end_screen():
    done = False
    frame = 0
    game_over = pygame.image.load("gameover.png")
    gameover = pygame.mixer.Sound("gameover.wav")

    background_music.stop()
    gameover.play(1)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return True
        frame += 1
        if frame > 600:
            done = True
        screen.fill(BLACK)

        screen.blit(game_over, [25, 180])

        pygame.display.flip()
        clock.tick(60)
    return False


# -------- Main Program Loop ---------------------------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x = -3
            elif event.key == pygame.K_RIGHT:
                player.change_x = 3
            elif event.key == pygame.K_SPACE and player.reload >= 15:
                bullet = Bullet()
                bullet.rect.centerx = player.rect.centerx
                bullet.rect.centery = player.rect.centery
                bullet_group.add(bullet)
                all_sprites_group.add(bullet)
                shoot_sound.play()
                player.reload = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_x = 0
            elif event.key == pygame.K_RIGHT:
                player.change_x = 0


    # --- Game logic
    all_sprites_group.update()
    shelter_group.update()
    ufo_group.update()

    timer += 1

    player_group.add(player)
    for enemy in enemy_group_three:
        if random.randrange(1600) == 0 and lives > 0:
            bullet_one = Bullet_one()
            bullet_one.rect.centerx = enemy.rect.centerx
            bullet_one.rect.centery = enemy.rect.centery
            all_sprites_group.add(bullet_one)
            bullet_group_one.add(bullet_one)
            shoot_sound.play()

    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for hit in hit_list:
            bullet.kill()
            score += 5
            invader_killed.play()

    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group_one, True)
        for hit in hit_list:
            bullet.kill()
            score += 10
            invader_killed.play()

    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_group_two, True)
        for hit in hit_list:
            bullet.kill()
            score += 15
            invader_killed.play()


    for bullet in bullet_group_one:
        hit_list = pygame.sprite.spritecollide(bullet, shelter_group, True)
        for hit in hit_list:
            bullet.kill()


    for bullet in bullet_group_one:
        if pygame.sprite.collide_rect(bullet, player):
            bullet.kill()
            bullet_group_one.empty()
            all_sprites_group.empty()
            all_sprites_group.add(player)
            for enemy in enemy_group_three:
                all_sprites_group.add(enemy)
            player.rect.centerx = screen_width/2
            lives = lives - 1
            explosion_sound.play()


    for bullet in bullet_group:
        hit_list = pygame.sprite.spritecollide(bullet, shelter_group, True)
        for hit in hit_list:
            bullet.kill()

    for enemy in enemy_group_three:
        hit_list_two = pygame.sprite.spritecollide(enemy, shelter_group, True)


# Deaths
    for enemy in enemy_group_three:
        if pygame.sprite.collide_rect(enemy, player):
            enemy.kill()
            end_screen()
            done = True

# UFO
    for bullet in bullet_group:
        hit_list_three = pygame.sprite.spritecollide(bullet, ufo_group, True)
        for hit in hit_list_three:
            bullet.kill()
            score += 50
            invader_killed.play()

    if timer >= 1000:
        ufo = Ufo()
        ufo.rect.x += ufo.speedx
        all_sprites_group.add(ufo)
        ufo_group.add(ufo)
        ufo_sound.play()
        timer = 0


# ------------NEXT LEVEL -----------------
    count = 0

    for enemy in enemy_group_three:
        count += 1
    if count == 0:
        level += 1
        all_sprites_group.empty()
        bullet_group.empty()
        all_sprites_group.add(player)


        for i in range(8):
            enemy = Enemy()
            all_sprites_group.add(enemy)
            enemy_group.add(enemy)
            enemy_group_three.add(enemy)
            enemy.image = pygame.image.load("creature1.png")
            enemy.rect.x = 50 * i + 36
            enemy.rect.y = 280
            enemy.speedx = level


        for i in range(8):
            enemy = Enemy()
            all_sprites_group.add(enemy)
            enemy_group.add(enemy)
            enemy_group_three.add(enemy)
            enemy.image = pygame.image.load("creature1.png")
            enemy.rect.x = 50 * i + 36
            enemy.rect.y = 245
            enemy.speedx = level


        for i in range(8):
            enemy = Enemy()
            all_sprites_group.add(enemy)
            enemy_group_one.add(enemy)
            enemy_group_three.add(enemy)
            enemy.image = pygame.image.load("creature2.png")
            enemy.rect.x = 50 * i + 36
            enemy.rect.y = 205
            enemy.speedx = level


        for i in range(8):
            enemy = Enemy()
            all_sprites_group.add(enemy)
            enemy_group_one.add(enemy)
            enemy_group_three.add(enemy)
            enemy.image = pygame.image.load("creature2.png")
            enemy.rect.x = 50 * i + 36
            enemy.rect.y = 165
            enemy.speedx = level


        for i in range(8):
            enemy = Enemy()
            all_sprites_group.add(enemy)
            enemy_group_two.add(enemy)
            enemy_group_three.add(enemy)
            enemy.image = pygame.image.load("creature3.png")
            enemy.rect.x = 50 * i + 36
            enemy.rect.y = 125
            enemy.speedx = level


        for i in range(8):
            enemy = Enemy()
            all_sprites_group.add(enemy)
            enemy_group_two.add(enemy)
            enemy_group_three.add(enemy)
            enemy.image = pygame.image.load("creature3.png")
            enemy.rect.x = 50 * i + 36
            enemy.rect.y = 85
            enemy.speedx = level


    if lives <= 0:
        end_screen()
        done = True
        break


# -----------------SCREEN LAYOUT-----------------------

    screen.fill(BLACK)

    # --- Drawing code should go here
    all_sprites_group.draw(screen)
    shelter_group.draw(screen)

    pygame.draw.line(screen, GREEN, [2, 0], [2, 700], 5)
    pygame.draw.line(screen, GREEN, [547, 0], [547, 700], 5)

    # --- Text
    my_text = my_font.render("Score: " + str(score), True, WHITE)
    screen.blit(my_text, [15, 12])

    my_text = my_font.render("LEVEL " + str(level), True, WHITE)
    screen.blit(my_text, [232, 12])


    # --- LIVES
    #my_text = my_font.render("Lives: " + str(lives), True, WHITE)
    #screen.blit(my_text, [450, 12])

    if lives == 1:
        screen.blit(lives_pic, [430, 5.3])
    if lives == 2:
        screen.blit(lives_pic, [430, 5.3])
        screen.blit(lives_pic, [470, 5.3])
    if lives == 3:
        screen.blit(lives_pic, [430, 5.3])
        screen.blit(lives_pic, [470, 5.3])
        screen.blit(lives_pic, [510, 5.3])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# -----------------Close the window and quit---------------
pygame.quit()