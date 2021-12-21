import pygame
import random

# drawing indestructible bombs if boss is on screen
class Bomb():
    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        self.screen_rect = (random.randint(300, 500), -50)
        self.bomb = pygame.image.load('assets/bomb.png').convert_alpha()  
        self.rect = self.bomb.get_rect()
        self.rect.midbottom = self.screen_rect
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        # counters for bombs to fall in random directions
        self.z = random.choice([-0.4, -0.3, -0.2, -0.1 ,0 ,0.1, 0.2, 0.3, 0.4,])
        self.g = random.choice([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        self.b = random.choice([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        self.i = 0
        
    def blitbomb(self):
        self.screen.blit(self.bomb, self.rect)

    def update(self):    
        self.x -= self.z
        self.rect.x = self.x
        self.y += (self.g + self.b)/1.5
        self.rect.y = self.y