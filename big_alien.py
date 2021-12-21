import pygame
import random

# alien appears on random position of top on screen
# moves from from one side to another
# shoots laser once
# falls down targeting bottom middle of screen
class Alien():
    def __init__(self, ai_game):
            
        self.screen = ai_game.screen
        # alien drawn on random position on screen
        self.screen_rect = (random.randint(90, 660), 0)
        # pool of alien images to randomly choose from
        self.image = pygame.image.load(random.choice(['assets/laivas2.png',\
            'assets/laivas1.png','assets/laivas3.png','assets/laivas4.png'])).convert_alpha()
        # laser image
        self.laserImage1 = pygame.image.load('laser/l1.png').convert_alpha()
        self.laserImage2 = pygame.image.load('laser/l2.png').convert_alpha()
        self.laserImage3 = pygame.image.load('laser/l3.png').convert_alpha()
        self.laserImage4 = pygame.image.load('laser/l4.png').convert_alpha()
        self.laserImage5 = pygame.image.load('laser/l5.png').convert_alpha()
        self.laserImage6 = pygame.image.load('laser/l6.png').convert_alpha()
        self.laserImage7 = pygame.image.load('laser/l7.png').convert_alpha()
        self.laserImage8 = pygame.image.load('laser/l8.png').convert_alpha()
        self.laserImage9 = pygame.image.load('laser/l9.png').convert_alpha()
        self.laserImage10 = pygame.image.load('laser/l10.png').convert_alpha()
        self.laserImage11 = pygame.image.load('laser/l11.png').convert_alpha()
        self.laserImage12 = pygame.image.load('laser/l12.png').convert_alpha()
        # laser grows in size
        self.image1 = pygame.transform.scale(self.laserImage1,
                (30, 110))
        self.image2 = pygame.transform.scale(self.laserImage2,
                (30, 180))
        self.image3 = pygame.transform.scale(self.laserImage3,
                (30, 250))
        self.image4 = pygame.transform.scale(self.laserImage4,
                (30, 320))
        self.image5 = pygame.transform.scale(self.laserImage5,
                (30, 390))
        self.image6 = pygame.transform.scale(self.laserImage6,
                (30, 460))
        self.image7 = pygame.transform.scale(self.laserImage7,
                (30, 530))
        self.image8 = pygame.transform.scale(self.laserImage8,
                (30, 600))
        self.image9 = pygame.transform.scale(self.laserImage9,
                (30, 670))
        self.image10 = pygame.transform.scale(self.laserImage10,
                (30, 740))
        self.image11 = pygame.transform.scale(self.laserImage11,
                (30, 740))
        self.image12 = pygame.transform.scale(self.laserImage12,
                (30, 740)) 
               
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect
        # alien position on x and y axis
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        # used to count when to draw laser and choose laser image
        self.g = 0
        # used to count alien time on screen
        self.i = 0

        self.z = random.choice([-2, -1, 1, 2])
        self.laser = 0
        self.laser2 = 0

        self.g +=1
        self.laserstretchedImage1 = pygame.transform.scale(self.laserImage1,
                (30, 40))
        self.laserstretchedImage2 = pygame.transform.scale(self.laserImage2,
                (30, 40))
        self.laserstretchedImage3 = pygame.transform.scale(self.laserImage3,
                (30, 40))
        self.laserstretchedImage4 = pygame.transform.scale(self.laserImage4,
                (30, 40))
        self.laserstretchedImage5 = pygame.transform.scale(self.laserImage5,
                (30, 40))
        self.laserstretchedImage6 = pygame.transform.scale(self.laserImage6,
                (30, 40))
        self.laserstretchedImage7 = pygame.transform.scale(self.laserImage7,
                (30, 40))
        self.laserstretchedImage8 = pygame.transform.scale(self.laserImage8,
                (30, 40))
        self.laserstretchedImage9 = pygame.transform.scale(self.laserImage9,
                (30, 40))
        self.laserstretchedImage10 = pygame.transform.scale(self.laserImage10,
                (30, 40))
        self.laserstretchedImage11 = pygame.transform.scale(self.laserImage11,
                (30, 40))
        self.laserstretchedImage12 = pygame.transform.scale(self.laserImage12,
                (30, 40))


    def blitalien(self):
        self.screen.blit(self.image, self.rect)

    
    def update(self):
        # alien movement logic
        self.i += 1
        if self.i <= 700 and self.y < 80:
            self.y += 0.2
            self.rect.y = self.y
        elif self.i > 700 and self.i < 1100:
            if self.rect.x < 680 and self.rect.x > 80:
                self.x -= self.z/3
                self.rect.x = self.x
        elif self.i > 1400 and self.i < 2500:
            if self.rect.x < 681 and self.rect.x > 79:
                self.x += self.z/3
                self.rect.x = self.x
        elif self.i > 2700 and self.i < 3300:
            if self.rect.x < 682 and self.rect.x > 78:
                self.x -= self.z/3
                self.rect.x = self.x        
        if self.i >= 2800:
            self.y += 2
            self.rect.y = self.y
        
        
    def blitalien2(self):
        # drawing laser
        self.g +=1
        self.laser = int(self.y)
        self.laser2 = int(self.x)
        if self.g < 100:
            self.screen.blit(self.image1, (self.laser2 + 37, self.laser + 100))
        elif self.g > 100 and self.g < 150:
            self.screen.blit(self.image2, (self.laser2 + 37, self.laser + 100))
        elif self.g >= 150 and self.g < 200:
            self.screen.blit(self.image3, (self.laser2 + 37, self.laser + 100))
        elif self.g >= 200 and self.g < 250:
            self.screen.blit(self.image4, (self.laser2 + 37, self.laser + 100))
        elif self.g >= 250 and self.g < 300:
            self.screen.blit(self.image5, (self.laser2 + 37, self.laser + 100))
        elif self.g >= 300 and self.g < 350:
            self.screen.blit(self.image6, (self.laser2 + 37, self.laser + 100))
        elif self.g >= 350 and self.g < 400:
            self.screen.blit(self.image7, (self.laser2 + 37, self.laser + 100))
        elif self.g >= 400 and self.g < 450:
            self.screen.blit(self.image8, (self.laser2 + 37, self.laser + 100))
        elif self.g >= 450 and self.g < 600:
            self.screen.blit(self.image9, (self.laser2 + 37, self.laser + 100))
        elif self.g >= 600 and self.g < 650:
            self.screen.blit(self.image10, (self.laser2 + 37, self.laser + 100))
        elif self.g >= 650 and self.g < 700:
            self.screen.blit(self.image11, (self.laser2 + 37, self.laser + 100))
        else:
            self.screen.blit(self.image12, (self.laser2 + 37, self.laser + 100))
        

    
    

    
        
