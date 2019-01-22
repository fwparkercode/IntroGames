import pygame
import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

pizzapos = (576, 720, 70, 70)

class Za(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        level = None
        self.image = pygame.image.load("za.tiff")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.change_x = 0
'''   
    def update(self):
        self.rect.x += self.level.world_shift
        
'''      
        
        
        
        