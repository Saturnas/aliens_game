import pygame
import random

# creating boss enemy on screen with animated movement
# boss is moving from one side of screen to another
class Boss():
    def __init__(self, ai_game):    
        self.screen = ai_game.screen
        # pool of boss images
        self.screen_rect = (random.randint(200, 500), 0)
        self.image1 = pygame.image.load('boss/b1.png').convert_alpha()
        self.image2 = pygame.image.load('boss/b2.png').convert_alpha()
        self.image3 = pygame.image.load('boss/b3.png').convert_alpha()
        self.image4 = pygame.image.load('boss/b4.png').convert_alpha()
        self.image5 = pygame.image.load('boss/b5.png').convert_alpha()
        self.image6 = pygame.image.load('boss/b6.png').convert_alpha()
        self.image7 = pygame.image.load('boss/b7.png').convert_alpha()
        self.image8 = pygame.image.load('boss/b8.png').convert_alpha()
        self.image9 = pygame.image.load('boss/b9.png').convert_alpha()
        self.image10 = pygame.image.load('boss/b10.png').convert_alpha()
        self.image11 = pygame.image.load('boss/b11.png').convert_alpha()
        self.image12 = pygame.image.load('boss/b12.png').convert_alpha()
        self.image13 = pygame.image.load('boss/b13.png').convert_alpha()
        self.image14 = pygame.image.load('boss/b14.png').convert_alpha()
        self.image15 = pygame.image.load('boss/b15.png').convert_alpha()
        self.image16 = pygame.image.load('boss/b16.png').convert_alpha()
        self.image17 = pygame.image.load('boss/b17.png').convert_alpha()
        self.image18 = pygame.image.load('boss/b18.png').convert_alpha()
        self.image19 = pygame.image.load('boss/b19.png').convert_alpha()
        self.image20 = pygame.image.load('boss/b20.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.midbottom = self.screen_rect
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        # counter for choosing boss image
        self.i = 0
        # counters used to calculate boss position on screen
        self.g1 = 0
        self.g = 0
        self.z = random.choice([-1, -0.5, 0.5, 1])

    def blitboss(self):
        # boss image logic
        self.i += 2.7
        if self.i < 100:
            self.screen.blit(self.image1, self.rect)
        elif self.i > 100 and self.i < 150:
            self.screen.blit(self.image2, self.rect)
        elif self.i > 150 and self.i < 200:
            self.screen.blit(self.image3, self.rect)
        elif self.i > 200 and self.i < 250:
            self.screen.blit(self.image3, self.rect)
        elif self.i > 250 and self.i < 300:
            self.screen.blit(self.image4, self.rect)
        elif self.i > 300 and self.i < 350:
            self.screen.blit(self.image5, self.rect)
        elif self.i > 350 and self.i < 400:
            self.screen.blit(self.image6, self.rect)
        elif self.i > 400 and self.i < 450:
            self.screen.blit(self.image7, self.rect)
        elif self.i > 450 and self.i < 500:
            self.screen.blit(self.image8, self.rect)
        elif self.i > 500 and self.i < 550:
            self.screen.blit(self.image9, self.rect)
        elif self.i > 550 and self.i < 600:
            self.screen.blit(self.image10, self.rect)
        elif self.i > 600 and self.i < 650:
            self.screen.blit(self.image11, self.rect)
        elif self.i > 650 and self.i < 700:
            self.screen.blit(self.image12, self.rect)
        elif self.i > 700 and self.i < 750:
            self.screen.blit(self.image13, self.rect)
        elif self.i > 750 and self.i < 800:
            self.screen.blit(self.image14, self.rect)
        elif self.i > 800 and self.i < 850:
            self.screen.blit(self.image15, self.rect)
        elif self.i > 850 and self.i < 900:
            self.screen.blit(self.image16, self.rect)
        elif self.i > 900 and self.i < 950:
            self.screen.blit(self.image17, self.rect)
        elif self.i > 950 and self.i < 1000:
            self.screen.blit(self.image18, self.rect)
        elif self.i > 1000 and self.i < 1050:
            self.screen.blit(self.image19, self.rect)
        elif self.i > 1050 and self.i < 1150:
            self.screen.blit(self.image20, self.rect)
        else:
            self.i = 0
            
    def update(self):
        # boss position logic
        self.g += 1
        self.g1 += 1
        if self.g1 <= 700 and self.y < 70:
            self.y += 0.2
            self.rect.y = self.y
        elif self.g > 700 and self.g < 1100:
            if self.rect.x < 600 and self.rect.x > 80:
                self.x -= self.z/2
                self.rect.x = self.x
        elif self.g > 1400 and self.g < 2500:
            if self.rect.x < 601 and self.rect.x > 79:
                self.x += self.z/2
                self.rect.x = self.x
        elif self.g > 2700 and self.g < 3300:
            if self.rect.x < 602 and self.rect.x > 78:
                self.x -= self.z/2
                self.rect.x = self.x            
        if self.g > 3300:
            self.g = 0