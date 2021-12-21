import pygame
import random

# drawing random explosion image in collision position
class Explosion():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # pool of explosion images to randomly choose
        self.image = pygame.image.load(random.choice(['assets/e1.png',\
            'assets/e2.png', 'assets/e3.png','assets/e4.png','assets/e5.png',\
            'assets/e6.png','assets/e7.png','assets/e8.png',\
            'assets/e9.png',])).convert_alpha()
        self.rect = self.image.get_rect()

        # text file used to get coordinates to draw explosion on screen
        file = open('cord1.txt', 'r')
        self.a = float(file.read())
        file.close()
        file = open('cord2.txt', 'r')
        self.b = float(file.read())
        file.close()
        
        self.rect.midbottom = (self.a, self.b)

    def blitexplosion(self):
        self.screen.blit(self.image, self.rect)
