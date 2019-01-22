
"""
Final Project: Apple Picker

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

# Import a library of functions called 'pygame'
import pygame
import random
apple_number = 70
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#good_sound = pygame.mixer.Sound("click.wav")
#bad_sound = pygame.mixer.Sound("clang - Marker #11.wav")
background_music = pygame.mixer.Sound("happy.wav")
background_music.play()



screen_width = 800
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)


# Create Class

class Apple (pygame.sprite.Sprite):
	"""
	This class represents the ball.
	It derives from the "Sprite" class in Pygame.
	"""

	def __init__(self, image):
		# Parent Class
		super().__init__()
		self.change_y = 3
		# Load the image: Apple
		self.image = pygame.image.load(image)
		# Update the position of the Apples
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y+= self.change_y



class Basket(pygame.sprite.Sprite):
	# -- Methods
	def __init__(self, x, y):
		"""Constructor function"""
		# Call the parent's constructor
		super().__init__()
		# Set the width, height
		self.image = pygame.image.load("basket.png")

	# Make basket: Return to screen from Top Left
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	# Attributes
	# Speed Vector
		self.change_x = 0
		self.change_y = 0

	def changespeed(self, x, y):
		self.change_x += x
		self.change_y += y

	def update(self):
		self.rect.x += self.change_x
		self.rect.y += self.change_y

		if self.rect.x >= screen_width - 15:
			self.rect.x = screen_width - 16

		if self.rect.y >= screen_height -15:
			self.rect.y = screen_height - 16















# List of Sprites
block_list = pygame.sprite.Group()
basket = Basket(0, 0)

# List of Every Sprite
all_sprites_list = pygame.sprite.Group()
good_apple_list = pygame.sprite.Group()
bad_apple_list = pygame.sprite.Group()

basket = Basket(0, screen_height - 200)
all_sprites_list.add(basket)

for i in range (150):
	# This represents a apple
	good_apple = Apple("redapple.png")
	# Randomize the Good Apples
	good_apple.rect.x = random.randrange(screen_width)
	good_apple.rect.y = random.randrange(-screen_height * 8, 0)
	# Add Good apple to the list of objects
	good_apple_list.add(good_apple)
	all_sprites_list.add(good_apple)


for i in range(apple_number):
	# This represents a apple
	bad_apple = Apple("greenapple.png")
	# Randomize the Bad Apples
	bad_apple.rect.x = random.randrange(screen_width)
	bad_apple.rect.y = random.randrange(-screen_height * 8, 0)
	# Add bad apple to the list of objects
	bad_apple_list.add(bad_apple)
	all_sprites_list.add(bad_apple)

background_image = pygame.image.load("background.jpeg")

# Loop until user clicks he button
done = False

# Manages how fast the screen updates
clock = pygame.time.Clock()

my_font = pygame.font.SysFont('Calibri', 30, True, False)

background_image = pygame.image.load("background.jpeg")

score = 0


def intro_screen():
	done = False
	frame = 0
	my_font = pygame.font.SysFont("Calibri", 50, True, False)
	while not done:
		# --- Main event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				done = True
		frame += 1
		if frame > 600:
			done = True
		screen.fill(RED)
		my_text = my_font.render("Click to Pick Apples!", True, WHITE)
		screen.blit(my_text, [screen_width/3, screen_height/2])

		pygame.display.flip()

		# --- Limit to 60 frames per second
		clock.tick(60)

def cut_screen():
	done = False
	frame = 0
	my_font = pygame.font.SysFont("Calibri", 35, True, False)
	while not done:
		# --- Main event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				done = True
		frame += 1
		if frame > 600:
			done = True
		screen.fill(RED)
		my_text = my_font.render("Your objective is to collect the RED APPLES", True, WHITE)
		intro_text = my_font.render("Do not collect the GREEN APPLES", True, WHITE)
		screen.blit(my_text, [screen_width/3 - 250, screen_height/2 - 100])
		screen.blit(intro_text, [screen_width / 3 - 250, screen_height / 2 - 50])

		pygame.display.flip()

		# --- Limit to 60 frames per second
		clock.tick(60)


def game_over():
	done = False
	frame = 0
	my_font = pygame.font.SysFont("Calibri", 70, True, False)
	while not done:
		# --- Main event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				done = True
		frame += 1
		if frame > 600:
			done = True
		screen.fill(BLUE)
		my_text = my_font.render("GAME OVER", True, WHITE)
		screen.blit(my_text, [screen_width/3, screen_height/2])

		pygame.display.flip()

		# --- Limit to 60 frames per second
		clock.tick(60)
	pygame.quit()
intro_screen()
cut_screen()

frame = 0
level_time = 30  # seconds per level
level = 1
# -------- Main Program Loop -----------
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			# Set the speed based on the key pressed
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				basket.changespeed(-4, 0)
			elif event.key == pygame.K_RIGHT:
				basket.changespeed(4, 0)


		# Reset speed when key goes up
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				basket.changespeed(4, 0)
			elif event.key == pygame.K_RIGHT:
				basket.changespeed(-4, 0)




	#Timer
	level_time -= 1/30

	all_sprites_list.update()
	# Clear the screen
	screen.fill(WHITE)
	screen.blit(background_image, [0,0])



	# See if the basket has collided with anything
	apple_hit_list = pygame.sprite.spritecollide(basket,good_apple_list, True)

	# Check List of collisions
	for good_apple in apple_hit_list:
		score += 1
		#good_sound.play()
		print(score)

	bad_apple_hit_list = pygame.sprite.spritecollide(basket, bad_apple_list, True)

	for bad_apple in bad_apple_hit_list:
		score-= 1
		#bad_sound.play()
		print(score)

	#print("green_apples", len(good_apple_list))


	if score > level * 20:
		frame = 0
		level += 1
		level_time = 30 - (level - 1) * 5
		all_sprites_list.empty()
		good_apple_list.empty()
		bad_apple_list.empty()
		all_sprites_list.add(basket)
		for i in range(100):
			# This represents a apple
			good_apple = Apple("redapple.png")
			# Randomize the Good Apples
			good_apple.rect.x = random.randrange(screen_width)
			good_apple.rect.y = random.randrange(-screen_height * 8, 0)
			# Add Good apple to the list of objects
			good_apple_list.add(good_apple)
			all_sprites_list.add(good_apple)

		for i in range(apple_number):
			# This represents a apple
			bad_apple = Apple("greenapple.png")
			# Randomize the Bad Apples
			bad_apple.rect.x = random.randrange(screen_width)
			bad_apple.rect.y = random.randrange(-screen_height * 8, 0)
			# Add bad apple to the list of objects
			bad_apple_list.add(bad_apple)
			all_sprites_list.add(bad_apple)

	if level_time < 0:
		game_over()

	print(level_time)


	if (frame // 30 > level_time):
		done = True


	# Draw all the sprites
	all_sprites_list.draw(screen)

	my_text = my_font.render("Score: " + str(score), True, BLACK)
	screen.blit(my_text, [50, 50])

	my_text = my_font.render("Timer: " + str(int(level_time)), True, BLACK)
	screen.blit(my_text, [0, 0])





	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# Limit to 60 frames per second
	clock.tick(30)

pygame.quit()