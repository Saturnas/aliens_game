import sys
import pygame
import random
import time
from player_ship import Ship
from player_bullet import Bullet
from big_asteroid import Asteroid
from big_alien import Alien
from collision_explosion import Explosion
from small_asteroid import SmallAsteroid
from small_alien import SmallAlien
from damage_effect import Damage
from boss_enemy import Boss
from boss_bomb import Bomb


# game settings
WINDOWWIDTH = 800
WINDOWHEIGHT = 1000
FPS = 300
TEXTCOLOR = (255, 255, 255)
mainClock = pygame.time.Clock()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Aliens")
        pygame.mouse.set_visible(False)
        self.score = 0
        self.shield = 100
        self.font = pygame.font.SysFont(None, 40)
        # using alpha with images to improve fps
        self.endscreen = pygame.image.load('assets/end.jpg').convert_alpha()
        self.damage = pygame.image.load('assets/broken.png').convert_alpha()
        self.bgOne = pygame.image.load('assets/ocean.jpg').convert_alpha()
        self.bgTwo = pygame.image.load('assets/ocean.jpg').convert_alpha()
        self.bgOne2 = pygame.image.load('assets/ocean8.png').convert_alpha()
        self.bgTwo2 = pygame.image.load('assets/ocean3.png').convert_alpha()
        self.game_over = False
        self.bgOne_y = 0
        self.bgTwo_y = self.bgOne.get_height()
        self.bgOne_y2 = 0
        self.bgTwo_y2 = self.bgOne2.get_height()
        
        # game sounds
        self.end_music = pygame.mixer.Sound('assets/gameover.mp3')
        self.explosion_sound = pygame.mixer.Sound('assets/explosion.mp3')
        self.rocket = pygame.mixer.Sound('assets/rocket.mp3')
        self.glass = pygame.mixer.Sound('assets/glass.mp3')
        self.background_position = [0, 0]
        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.asteroid = Asteroid(self)
        self.smallAsteroid = SmallAsteroid(self)
        self.alien = Alien(self)
        self.boss = Boss(self)
        self.bombs = Bomb(self)
        self.smallalien = SmallAlien(self)
        self.damage = Damage(self)
        self.explosion = Explosion(self)
        self.bosses = []
        self.bombs = []
        self.explosions = []
        self.bullets = []
        self.asteroids = []
        self.smallasteroids = []
        self.aliens = []
        self.smallaliens = []
        self.damages = []
        self.boss_life = 10
        # only one bullet can be on screen at any time
        self.bullet_counter = 0
        # timer for big indestructible asteroid
        self.big_asteroid_timer = 0
        # timer for drawing explosion images on screen
        self.explosions_counter = 0
        # drawing one big alien on screen if player score less than 1000
        self.alien_counter = 0
        # after two big asteroids appears many small asteroids and counter reset
        self.asterdoids_counter = 0
        # counter for making random amount of small aliens
        self.small_alien_counter = 0
        # checking if player takes damage
        self.damage_counter = 0
        # checking if boss enemy have bombs available
        self.bomb_counter = 1
    

    def run_game(self):
        while True:
            # creation of two backgrounds moving with different speed
            # background number 1 moving with speed 1
            self.screen.blit(self.bgOne, (0, self.bgOne_y))
            self.screen.blit(self.bgTwo, (0, self.bgTwo_y)) 
            self.bgOne_y -= 1
            self.bgTwo_y -= 1
            if self.bgOne_y == -1 * self.bgOne.get_height():
                self.bgOne_y = self.bgTwo_y + self.bgTwo.get_height()
            if self.bgTwo_y == -1 * self.bgTwo.get_height():
                self.bgTwo_y = self.bgOne_y + self.bgOne.get_height()
            # background number 2 moving with speed 0.5
            self.screen.blit(self.bgOne2, (0, self.bgOne_y2))
            self.screen.blit(self.bgTwo2, (0, self.bgTwo_y2)) 
            self.bgOne_y2 -= 0.5
            self.bgTwo_y2 -= 0.5
            if self.bgOne_y2 == -1 * self.bgOne2.get_height():
                self.bgOne_y2 = self.bgTwo_y2 + self.bgTwo2.get_height()
            if self.bgTwo_y2 == -1 * self.bgTwo2.get_height():
                self.bgTwo_y2 = self.bgOne_y2 + self.bgOne2.get_height()

            self._check_events()

            # drawing player ship on screen
            self.ship.blitme()

            # only one bullet on screen at any time
            for b in self.bullets:
                b.blitbullet()
                b.update()
            for b in self.bullets:
                if b.rect.bottom <= 0:
                    self.bullets.remove(b)
                    self.bullet_counter -= 1

            # creating big asteroid at random time
            self.big_asteroid_timer += random.randrange(1, 1000, 10)
            if self.big_asteroid_timer >= 3000 and self.score <= 1000:
                self._fall_asteroid()
            # small asteroids created after two big asteroids
            for b in self.asteroids:
                self.big_asteroid_timer = 0
                b.blitasteroid()
                b.update()
            for b in self.asteroids:
                if b.rect.top >= 1000:
                    self.asteroids.remove(b)
                    self.asterdoids_counter += 1
                    
           # creating random amount of small aliens if score less than 1000         
            if self.small_alien_counter == 1 and self.score <= 1000:
                for x in range(1, 10):
                    self._fall_small_alien()
                    self.small_alien_counter = 0
            for b in self.smallaliens:
                b.blitsmallalien()
                b.update()
                if b.rect.top >= 1000:
                    self.smallaliens.remove(b)

            # removing small asteroids if reaching bottom of screen
            if self.asterdoids_counter == 2 and self.score <= 1000:
                for x in range(1, 15):
                    self._fall_small_asteroid()
                    self.asterdoids_counter = 0 
            for b in self.smallasteroids:
                b.blitsmallasteroid()
                b.update()
                if b.rect.top >= 1000:
                    self.smallasteroids.remove(b)
            
            # creating big alien
            if len(self.aliens) < 1 and self.score <= 1000:
                self._fall_alien()
                self.small_alien_counter += 1
            for b in self.aliens:
                b.blitalien()
                b.update()
            for b in self.aliens:
                self.alien_counter+=1
                if self.alien_counter > 1000 and self.alien_counter < 1800:
                    b.blitalien2()
                # removing big alien if reaching bottom of screen
                if b.rect.top >= 1000:
                    self.alien_counter = 0
            # removing big alien if reaching bottom of screen
            for b in self.aliens:
                if b.rect.top >= 1000:
                    self.aliens.remove(b)

            # drawing explosion on screen
            for x in self.explosions:
                        x.blitexplosion()
                        self.explosions_counter += 1
                        if self.explosions_counter > 300:
                            self.explosions.remove(x)
                            self.explosions_counter = 0

            # creating boss if screen is empty and score more than 1000
            if len(self.aliens) < 1 and len(self.asteroids) < 1:
                if len(self.bosses) < 1 and self.score >= 1000:
                    self._make_boss()
                for b in self.bosses:
                    b.blitboss()
                    b.update()
            # boss throwing random amount of indestructible bombs
            if len(self.bosses) == 1 and self.bomb_counter == 1:
                for x in range(1, 10):
                    self._make_bomb()
                    self.bomb_counter = 0 
            for b in self.bombs:
                b.blitbomb()
                b.update()
                if b.rect.top >= 1000:
                    self.bombs.remove(b)
                # removing bombs if reaching bottom of screen
                if len(self.bombs) == 0:
                    self.bomb_counter = 1

            # checking if bullet collide with boss
            for a in self.bullets:
                for b in self.bosses:         
                    if a.rect.colliderect(b):
                        self.bullets.remove(a)
                        self.bullet_counter -= 1 
                        self.g = int(a.rect.x)
                        self.h = int(a.rect.y)
                        self.get_coord()
                        self.score += 100
                        self._make_explosion()
                        self.boss_life -= 1

            # checking if bullet collide with small asteroids
            for a in self.bullets:
                for b in self.smallasteroids:         
                    if a.rect.colliderect(b):
                        self.smallasteroids.remove(b)
                        self.bullet_counter -= 1 
                        self.g = int(a.rect.x)
                        self.h = int(a.rect.y)
                        self.get_coord()
                        self.score += 50
                        self._make_explosion()
                        # placeholder to avoid crashing if multiple rect hit
                        try:
                            self.bullets.clear()
                        except:
                            pass
            
            # checking if bullet collide with big alien                   
            for a in self.bullets:
                for c in self.aliens:          
                    if a.rect.colliderect(c):
                        self.alien_counter = 0
                        self.g = int(a.rect.x)
                        self.h = int(a.rect.y)
                        self.get_coord()
                        self._make_explosion()
                        self.score += 50
                        self.aliens.remove(c)
                        self.bullets.remove(a)
                        self.bullet_counter -= 1

            # checking if bullet collide with small alien
            for a in self.bullets:
                for d in self.smallaliens:          
                    if a.rect.colliderect(d):
                        self.smallaliens.remove(d)
                        self.bullet_counter -= 1
                        self.g = int(a.rect.x)
                        self.h = int(a.rect.y)
                        self.get_coord()
                        self.score += 50
                        self._make_explosion()
                        # placeholder to avoid crashing if multiple rect hit
                        try:
                            self.bullets.clear()
                        except:
                            pass
                        
            # if player collide with something play 'breaking glass' sound
            # remove obstacle player collided
            if pygame.sprite.spritecollideany(self.ship, self.asteroids):
                self._make_damage()
                for b in self.asteroids:
                    pygame.mixer.Sound.play(self.glass)
                    self.asteroids.remove(b)             
            elif pygame.sprite.spritecollideany(self.ship, self.aliens):
                self._make_damage()
                for b in self.aliens:
                    pygame.mixer.Sound.play(self.glass)
                    self.aliens.remove(b)
            elif pygame.sprite.spritecollideany(self.ship, self.smallaliens):
                self._make_damage()
                for b in self.smallaliens:
                    pygame.mixer.Sound.play(self.glass)
                    self.smallaliens.remove(b)
            elif pygame.sprite.spritecollideany(self.ship, self.smallasteroids):
                self._make_damage()
                for b in self.smallasteroids:
                    pygame.mixer.Sound.play(self.glass)
                    self.smallasteroids.remove(b)
            elif pygame.sprite.spritecollideany(self.ship, self.bombs):
                self._make_damage()
                for b in self.bombs:
                    pygame.mixer.Sound.play(self.glass)
                    self.bombs.clear()
                    self.bomb_counter = 1
            else:    
                self.take_damage()
            
            # draw score and sheald value on screen              
            self.drawText('Score: %s' % (self.score), self.font,
             self.screen, 10, 0)
            self.drawText('Shield: %s' % (self.shield) + '%', self.font,
             self.screen, 10, 50)         
            
            # game over conditions
            if self.shield <= 0 or self.boss_life == 0:
                self.game_over = True
                self.screen.blit(self.endscreen, (0, 0))
                self.drawText('Your score: %s' % (self.score), self.font,
                 self.screen, 300, 800)
                self.drawText('Press R to play again', self.font,
                 self.screen, 300, 850)
                pygame.mixer.Sound.play(self.end_music)
                   
            pygame.display.update()
            mainClock.tick(FPS)
    
    # draw broken glass on screen and remove 20 of shield
    def take_damage(self):
        for b in self.damages:
            b.blitdamage()
            self.damage_counter += 1
        if self.damage_counter >= 300:
            self.shield -= 20
            self.damage_counter = 0
            self.damages.clear()
            
    # using text file to get bullet/enemy collision coordinates
    def get_coord(self):
        pygame.mixer.find_channel(True).play(self.explosion_sound)
        file = open('cord1.txt', 'w')
        file.write('%s'% (self.g))
        file.close()
        file = open('cord2.txt', 'w')
        file.write('%s'% (self.h))
        file.close()
      

    def _check_events(self):
        # exit game if close window pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # player position
            elif event.type == pygame.MOUSEMOTION:
                self.ship.rect.x = event.pos[0]
                self.ship.rect.y = event.pos[1]
            # if no bullet on screen and space pressed, create new bullet
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.game_over == False:
                    if self.bullet_counter < 1:
                        self.bullet_counter += 1
                        self._fire_bullet()
                        pygame.mixer.find_channel(True).play(self.rocket)
            # restart game if R pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r and self.game_over == True:
                    pygame.mixer.Sound.stop(self.end_music)
                    ai = Game()
                    ai.run_game()
                    self.game_over = False
                    
    # function for drawing text on screen               
    def drawText(self, text, font, surface, x, y):
        self.textobj = font.render(text, 1, TEXTCOLOR)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (x, y)
        self.screen.blit(self.textobj, self.textrect)

    # fuctions for appending assets to lists
    def _make_boss(self):
        new_boss = Boss(self)
        self.bosses.append(new_boss)
    def _make_bomb(self):
        new_bomb = Bomb(self)
        self.bombs.append(new_bomb)
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.append(new_bullet)
    def _fall_asteroid(self):
        new_asteroid = Asteroid(self)
        self.asteroids.append(new_asteroid)
    def _fall_small_alien(self):
        new_small_alien = SmallAlien(self)
        self.smallaliens.append(new_small_alien)
    def _fall_small_asteroid(self):
        new_small_asteroid = SmallAsteroid(self)
        self.smallasteroids.append(new_small_asteroid)
    def _fall_alien(self):
        new_alien = Alien(self)
        self.aliens.append(new_alien)
    def _make_explosion(self):
        new_explosion = Explosion(self)
        self.explosions.append(new_explosion)
    def _make_damage(self):
        new_damage = Damage(self)
        self.damages.append(new_damage)

       
if __name__ == '__main__':
    ai = Game()
    ai.run_game()