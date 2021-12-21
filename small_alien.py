import pygame
import random

# creating random amount of small aliens
# aliens are falling down to random directions
class SmallAlien():
    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        self.screen_rect = (random.randint(200, 600), -50)
        self.smallalienImage = pygame.image.load('assets/smallalien.png').convert_alpha()
        self.rect = self.smallalienImage.get_rect()
        self.rect.midbottom = self.screen_rect
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        # counter for random falling direction
        self.z = random.choice([-0.4, -0.3, -0.2, -0.1 ,0 ,0.1, 0.2, 0.3, 0.4,])
        self.g = random.choice([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3])
        self.b = random.choice([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3])
        self.i = 0
        
    def blitsmallalien(self):
        self.screen.blit(self.smallalienImage, self.rect)

    def update(self):    
        self.x -= self.z
        self.rect.x = self.x
        self.y += (self.g + self.b)/1.7
        self.rect.y = self.y