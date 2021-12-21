import pygame
import random

# small asteroids appear on screen and falls down with random speed
class SmallAsteroid():
    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        # asteroid random position
        self.screen_rect = (random.randint(30, 770), random.randint(10, 30))
        self.smallasteroiImage = pygame.image.load('assets/smallasteroid.png').convert_alpha()
        # asteroid image transformed by given random values
        self.smallasteroidstretchedImage = pygame.transform.scale(
        self.smallasteroiImage,(random.randint(20, 50), random.randint(40, 50)))
        self.rect = self.smallasteroiImage.get_rect()
        self.rect.midbottom = self.screen_rect
        self.y = float(self.rect.y)
        # counter for asteroids position and fall speed
        self.x = 0
        self.z = 0
        self.i = random.randint(2, 20)
        self.g = random.randint(1000, 3000)
        self.g2 = random.randint(2000, 8000)


    def blitsmallasteroid(self):
        self.z += random.randint(1, 10)
        if self.z >= self.g:
            self.screen.blit(self.smallasteroidstretchedImage, self.rect)

    def update(self):
        self.x += random.randint(1, 15)
        if self.x >= self.g2:
            self.y += 4/self.i
            self.rect.y = self.y