import pygame

# drawing bullet in the middle of player ship
class Bullet():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('assets/bomba1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def blitbullet(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y -= 1.2
        self.rect.y = self.y