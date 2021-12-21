import pygame
import random

# big indestructible asteroid created on screen
# blinks few times and falls down to bottom of screen
class Asteroid():
    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        # drawing randomly on top of screen
        self.screen_rect = (random.randint(50, 750), 100)
        self.image = pygame.image.load('assets/asteroid.png').convert_alpha()
        self.image2 = pygame.image.load('assets/asteroid2.png').convert_alpha()
        self.image3 = pygame.image.load('assets/asteroid3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect
        self.y = float(self.rect.y)
        # used to count time for falling
        self.x = 0
        # used to count time for blinking
        self.i = 0

    def blitasteroid(self):
        self.i += 1
        if self.x <= 5000:
            if self.i <= 100:
                self.screen.blit(self.image, self.rect)
            elif self.i >= 100:
                self.screen.blit(self.image2, self.rect)
            if self.i > 200:
                self.i = 0
        else:
            self.screen.blit(self.image3, self.rect)

    def update(self):
        self.x += random.randint(1, 10)
        if self.x >= 5000:
            self.y += 1
            self.rect.y = self.y