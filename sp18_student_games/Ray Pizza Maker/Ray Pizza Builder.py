import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

background = pygame.image.load("610015020.png")
music = pygame.mixer.Sound("sketch4.wav")
music.set_volume(0.2)
landing = pygame.mixer.Sound("landing.wav")

pizza_base = pygame.image.load("pizza.png")
pepperoni = pygame.image.load("pepperoni.png")
mushrooms = pygame.image.load("mushrooms_good.png")
extra_cheese = pygame.image.load("extra_cheese.png")
sausage = pygame.image.load("sausage.png")
black_olives = pygame.image.load("blackolives.png")
bacon = pygame.image.load("bacon.png")
green_peppers = pygame.image.load("greenpeppers.png")
pineapple = pygame.image.load("pineapple.png")

toppings_list = [pepperoni, mushrooms, extra_cheese, sausage, black_olives, bacon, green_peppers, pineapple]

class Pizza_Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pizza_base
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.rect.centery = screen_height - 50
    def move(self):
        self.rect.x = screen_width / 2
        self.rect.y = screen_height
    def changespeed(self, x, y):
        self.change_x += x
    def update(self):
        self.rect.x += self.change_x
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width
        
        

class Topping(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(toppings_list)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = 0
        self.change_x = 0
        self.change_y = random.randrange(1, 5)
        self.offset = 0
    def update(self):
        self.rect.y += self.change_y
    

frame = 0
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
score = 0
 
pygame.display.set_caption("My Game")

enemy_list = pygame.sprite.Group()
added_toppings_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
captured_toppings = pygame.sprite.Group()
 
done = False
 
clock = pygame.time.Clock()

pizza = Pizza_Base()
all_sprites_list.add(pizza)

font = pygame.font.Font(None, 26)
display_instructions = True
instruction_page = 1

order_1 = random.choice(toppings_list)
order_2 = random.choice(toppings_list)
order_3 = random.choice(toppings_list)

order_4 = random.choice(toppings_list)
order_5 = random.choice(toppings_list)
order_6 = random.choice(toppings_list)
order_7 = random.choice(toppings_list)

order_8 = random.choice(toppings_list)
order_9 = random.choice(toppings_list)
order_10 = random.choice(toppings_list)
order_11 = random.choice(toppings_list)
order_12 = random.choice(toppings_list)

clock = pygame.time.Clock()
 
frame_count = 0
frame_rate = 60
start_time = 90
game_over = False
 
# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
         
    
    # Set the screen background
    screen.fill(BLACK)
    
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        text = font.render("Instructions", True, WHITE)
        screen.blit(text, [10, 10])
 
        text = font.render("Make the customer's order without collecting unordered toppings!", True, WHITE)
        screen.blit(text, [10, 40])
        
        text = font.render("Use the arrow keys to move the pizza base.", True, WHITE)
        screen.blit(text, [10, 70])
        
        text = font.render("Click for first order.", True, WHITE)
        screen.blit(text, [10, 100])
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
      
    if instruction_page == 2:
        text = font.render("The first customer's order is", True, WHITE)
        screen.blit(text, [10, 10])
 
        screen.blit(order_1, [10, 40])
        screen.blit(order_2, [100, 40])
        screen.blit(order_3, [190, 40])
        
        text = font.render("Collect as many of the customer's toppings as possible before time runs out.", True, WHITE)
        screen.blit(text, [10, 90])
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            display_instructions = False    
                
    if instruction_page == 3:
        text = font.render("The second customer's order is", True, WHITE)
        screen.blit(text, [10, 10])
 
        screen.blit(order_4, [10, 40])
        screen.blit(order_5, [100, 40])
        screen.blit(order_6, [190, 40])
        screen.blit(order_7, [280, 40])
        
        text = font.render("Collect as many of the customer's toppings as possible before time runs out.", True, WHITE)
        screen.blit(text, [10, 90]) 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            display_instructions = False           
        
    if instruction_page == 4:
        text = font.render("The third customer's order is", True, WHITE)
        screen.blit(text, [10, 10])
 
        screen.blit(order_8, [10, 40])
        screen.blit(order_9, [100, 40])
        screen.blit(order_10, [190, 40])
        screen.blit(order_11, [280, 40])
        screen.blit(order_12, [370, 40])
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            display_instructions = False           
        
        text = font.render("Collect as many of the customer's toppings as possible before time runs out.", True, WHITE)
        screen.blit(text, [10, 90])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pizza.changespeed(0, 0)
                pizza.changespeed(-4, 0)
            elif event.key == pygame.K_RIGHT:
                pizza.changespeed(4, 0)       
                pizza.changespeed(0, 0)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pizza.changespeed(4, 0)
            elif event.key == pygame.K_RIGHT:
                pizza.changespeed(-4, 0)
    
    music.play()                
    
    total_seconds = frame_count // frame_rate      
    
    frame += 1
    if frame % 50 == 0:
        topping = Topping()
        all_sprites_list.add(topping)
        added_toppings_list.add(topping)
    
    hit_list = pygame.sprite.spritecollide(pizza, added_toppings_list, False)
    for hit in hit_list:
        landing.play()
        hit.rect.y = pizza.rect.y + 10
        hit.change_y = 0
        hit.remove(added_toppings_list)
        captured_toppings.add(hit)
        hit.offset = pizza.rect.x - hit.rect.x
        if hit.image == order_1 or hit.image == order_2 or hit.image == order_3:
            score += 1
        else:
            score -=1
        print(score)

    for topping in captured_toppings:
        topping.rect.x = pizza.rect.x - topping.offset

    if game_over:
        # If game over is true, draw game over
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
   
    if frame >= 1500:
        instruction_page += 1
        display_instructions = True
    
    if instruction_page == 5:
        game_over = True     
        
    screen.blit(background, [0, 0])
    
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
 
    clock.tick(60)


pygame.quit()