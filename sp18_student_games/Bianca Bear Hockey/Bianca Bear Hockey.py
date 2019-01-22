import pygame
import random

pygame.init()

screen_width = 425
screen_height = 638
size = (screen_width, screen_height)
BLACK = (0, 0, 0)
BLUE = (0 , 0 , 255)
RED = (255, 0, 0)
WHITE = (255,255,255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Air Hockey")

my_font = pygame.font.SysFont("Calibri", 20, True, False)
my_music = pygame.mixer.Sound("music.wav")
my_music.play(100)

class Button (pygame.sprite.Sprite):
    def __init__(self,text, y):
        super().__init__()
        self.image = pygame.Surface ([100,50])
        self.image.fill(BLUE) 
        self.rect = self.image.get_rect()
        self.rect.x = 170
        self.rect.y = y
        self.text = text 
    def draw_text (self):
        
        text_level = my_font.render(self.text, False, WHITE)
        
        screen.blit(text_level, (self.rect.centerx - text_level.get_width()/2, self.rect.centery - text_level.get_height()/2))
        
        
    
class Goodgoal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface ([200,2])
        self.image.fill(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = 115
        self.rect.y = 12
        
class Badgoal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface ([200,2])
        self.image.fill(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = 115
        self.rect.y = 624
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()   
        self.image = pygame.Surface ([30,30])
        self.image.fill(BLACK) 
        self.image = pygame.image.load("redhandle.png")
        self.rect = self.image.get_rect()        
        self.rect.x = 0
        self.rect.y = 570
              
    def update(self):
        if self.rect.top <= 575: 
            self.rect.top = 575 
        if self.rect.right >= screen_width: 
            self.rect.right = screen_width 
        if self.rect.left <= 0: 
            self.rect.left = 0 
        if self.rect.bottom >= 625: 
            self.rect.bottom = 625
            
class Puck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface ([30,30])
        self.image.fill(BLUE) 
        self.rect = self.image.get_rect()
        self.rect.x = 199
        self.x = self.rect.y
        self.rect.y = 305
        self.y = self.rect.y
        self.x_speed = 2
        self.y_speed = 3 
        self.count = 60
        self.image = pygame.image.load("puck.png")
        
    def update(self):
        
        self.count -= 1
        if self.count < 0:
               
            self.x += self.x_speed
            self.rect.x = int(self.x)
            if self.rect.right > screen_width:
                self.rect.right = screen_width
                self.x_speed *= -1
            if self.rect.x < 0:
                self.rect.x = 0
                self.x_speed *= -1
            
            self.y += self.y_speed
            self.rect.y = int(self.y)
            if self.rect.y > 625-30:
                self.rect.y = 625-30
                self.y_speed *= -1
            if self.rect.y < 12:
                self.rect.y = 12
                self.y_speed *= -1
            
   
        

        
 
class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface ([50,50])
        self.image.fill(RED) 
        self.image = pygame.image.load("blackhandle.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.speed_x = 0
        
        self.rect.y = 100
        self.speed_y = 0
        
    def update(self):
        if self.rect.top >= 100: 
            self.rect.top = 100 
        if self.rect.right >= screen_width: 
            self.rect.right = screen_width 
        if self.rect.left <= 0: 
            self.rect.left = 0 
        if self.rect.bottom <= 12: 
            self.rect.bottom = 12    
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        
hit_noise = pygame.mixer.Sound("hittingnoise.wav")
goal_noise = pygame.mixer.Sound("goalnoise.wav")
bear_noise = pygame.mixer.Sound("bearnoise.wav")
    
    
    
done = False
clock = pygame.time.Clock()



player_score = 0
opponent_score = 0

 

goodgoal = Goodgoal()
badgoal = Badgoal()
player = Player()
puck = Puck()
opponent = Opponent()
button = Button("Easy",200)
button2 = Button("Medium",300)
button3 = Button("Hard",400)
background_image = pygame.image.load("bariers.png")
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(goodgoal)
all_sprites_list.add(badgoal)
all_sprites_list.add(player)
all_sprites_list.add(puck)
all_sprites_list.add(opponent)

button_list = pygame.sprite.Group()
button_list.add(button)
button_list.add(button2)
button_list.add(button3)

def intro_screen():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if button.rect.collidepoint(x,y):
                    max_speed = 2
                    min_speed = -2
                    done = True
                if button2.rect.collidepoint(x,y):
                    max_speed = 6
                    min_speed = -6
                    done = True 
                if button3.rect.collidepoint(x,y):
                    max_speed = 80
                    min_speed = -80
                    done = True 
            
                
                    
            
                    
                           
        screen.fill(BLACK)
        bear = pygame.image.load("bear.png")
        screen.blit(bear, [70,350])
        button_list.draw(screen)
        for my_button in button_list:
            my_button.draw_text()
        text = my_font.render("BAir Hockey", True, BLUE)
        text2 = my_font.render("Instructions: Move with mouse,", True, BLUE)
        text3 = my_font.render(" score 8 goals to win!", True, BLUE)
        screen.blit(text, [150, 50])
        screen.blit(text2, [40, 100])
        screen.blit(text3, [100, 120])
        pygame.display.flip()
        clock.tick(60)
    return min_speed, max_speed
    
        
def final_screen_player():
    
    done = False
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True     
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                    intro_screen()
                    done = True  
            '''

        screen.fill(WHITE)
        bear_noise.play(1)
        text = my_font.render("You Win", True, RED)
        bear = pygame.image.load("bear.png")
        screen.blit(bear, [70,350])            
        screen.blit(text,[160, 50])
        pygame.display.flip()
        clock.tick(60)
        
            
def final_screen_opponent():
    
    done = False
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
        
        
    
           # if event.type == pygame.MOUSEBUTTONDOWN:
                #intro_screen()
               # done = True 
        
                
                
            screen.fill(WHITE)
            bear_noise.play(1)


            text = my_font.render("I'm beary sorry you lost :(", True, RED)
            bear = pygame.image.load("bear.png")
            screen.blit(bear, [70,350])            
            screen.blit(text,[150, 50])
            pygame.display.flip()
            clock.tick(60) 
        


            
            
        
min_speed, max_speed = intro_screen()






while not done:
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
            '''
        if player.rect.top == puck.rect.bottom:
            self.puck.speedy+=1
            
            
            '''
    print (puck.y_speed)
    
    if puck.x_speed >= 12:
        puck.x_speed = 11
    elif puck.x_speed <= -12:
        puck.x_speed = 11
        
    if puck.y_speed == 0:
        puck.x_speed = 2
    elif puck.y_speed >= 9:
        puck.y_speed = 6
    elif puck.y_speed <= -9:
        puck.y_speed = -6
        
    if puck.x_speed == 0:
        puck.x_speed = random.choice([-1,1])
    
    all_sprites_list.update()
    button_list.update()
    
    deltax2 = opponent.rect.x - puck.rect.x
    if deltax2 > 0:
        opponent.speed_x = max(min_speed, -deltax2/5)
    elif deltax2 < 0:
        opponent.speed_x = min(max_speed, -deltax2/5)
    else:
        opponent.speed_x = 0
        
    deltax3 = opponent.rect.y - puck.rect.y
    if deltax3 > 0:
        opponent.speed_y = max(-4, -deltax3/5)
    elif deltax3 < 0:
        opponent.speed_y = min(4, -deltax3/5)
    else:
        opponent.speed_y = 0    
        
    
    if pygame.sprite.collide_rect(player, puck):
        deltax = puck.rect.x - player.rect.x
        
        puck.x_speed += deltax/30
        deltay = puck.rect.y - player.rect.y
        puck.y_speed += deltay/30
        puck.rect.y += 1
        #puck.rect.bottom = player.rect.top
        hit_noise.play(1)
        
    if pygame.sprite.collide_rect(puck, opponent):
        deltax = puck.rect.x - opponent.rect.x
        puck.x_speed += deltax/60
        deltay = puck.rect.y - opponent.rect.y
        puck.y_speed += deltay/60
        hit_noise.play(1)
        
    if pygame.sprite.collide_rect(puck, goodgoal):
        player_score += 1
        puck.rect.x = 199
        puck.x = 199
        puck.rect.y = 305
        puck.y = 305
        puck.count = 60
        puck.y_speed = random.choice([1,-1])
        puck.x_speed = random.randrange(-3,3)
        goal_noise.play(1)
        if puck.rect.top == player.rect.bottom:
            puct.rect.x = 200
            puck.rect.y = 400
            puck.y_speed = 1
        
    if pygame.sprite.collide_rect(puck, badgoal):
        opponent_score += 1
        puck.rect.x = 199
        puck.x = 199
        puck.rect.y = 305
        puck.y = 305   
        puck.count = 60
        puck.y_speed = random.choice([1,-1])
        puck.x_speed =1
        goal_noise.play(1)
        
        
        
            
    screen.blit(background_image, [0,0])
    
    all_sprites_list.draw(screen)
   
    
    
    x,y = pygame.mouse.get_pos()
    player.rect.centerx = x
    player.rect.centery = y
    
    
    
    
    text = my_font.render("Your Score: " + str(player_score), True, BLACK)
    text2 = my_font.render("Their Score: " + str(opponent_score), True, BLACK)
    
    if player_score == 8:
        final_screen_player() 
        
    if opponent_score == 8:
        final_screen_opponent()
    
    
    screen.blit(text, [40,330])
    screen.blit(text2, [35,300])
    
    
    pygame.display.flip()
 
   
    clock.tick(80)
     
 


pygame.quit()