#Create your own shooter

from pygame import *
from random import randint

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter Game")
background =transform.scale(image.load("images.jpeg"), (win_width, win_height))

font.init()
font1 = font.SysFont('Arial', 16)
font2 = font.SysFont('Arial', 36)
font3 = font.SysFont('Arial', 76)
you_lose = font2.render('YOU LOSE', 1,(0,0,0))
you_win = font3.render('YOU WIN!!', 1,(0,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width, player_height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image ,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 10,20,20)
        bullets.add(bullet)


win=0
missed=0    
class Enemy(GameSprite):
    def update(self):
        global missed
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.rect.y = 2
            self.rect.x = randint(5, win_width-50)
            self.speed = randint(1,3)
            missed += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed


class Enemy2(GameSprite):
    def update(self):
        global missed
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.rect.y = 2
            self.rect.x = randint(5, win_width-50)
            self.speed = randint(1,3)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

enemy = sprite.Group()
for i in range(5):
    bom = Enemy('bom.png',randint(5, win_width - 50),randint(-30,-2), randint(1,3),100,60)
    enemy.add(bom)
        
bom = Enemy('bom.png',5,2,5,100,60)



player = Player('tangan.png',5, win_height - 80, 10,65,65)
ufo = Enemy('nyamuk.png',5,2,5,100,60)

enemy = sprite.Group()
for i in range(5):
    ufo = Enemy('nyamuk.png',randint(5, win_width - 50),randint(-30,-2), randint(1,3),100,60)
    enemy.add(ufo)

bullets = sprite.Group()

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.set_volume(0.4)



clock = time.Clock()
FPS = 60
run = True
score = 0


finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        if e.type == KEYDOWN:
            keys = key.get_pressed()
            if keys[K_SPACE]:
                player.fire()
        
        collides = sprite.groupcollide(enemy, bullets, True, True)
        if collides:
            ufo = Enemy("nyamuk.png", randint(5, win_width - 40), 2, randint(1,5), 100,60)
            enemy.add(ufo)
            score += 1 
    text_lose = font1.render('Nyamuk terlewat:' + str(missed),1,(0,0,0))
    text_score = font1.render('Nyamuk mati:' +str(score),1,(0,0,0))

    if missed > 5 :
        finish = True
        window.blit(you_lose,(win_width/3.3, win_height/2))

    if score > 20 :
        finish = True
        window.blit(you_win,(win_width/3.3, win_height/2))

    if not finish:
        window.blit(background,(0, 0))
        window.blit(text_lose,(0,20))
        window.blit(text_score,(0,0))
        player.reset()
        player.update()
        ufo.reset()
        ufo.update()
        enemy.draw(window)
        enemy.update()
        bullets.draw(window)
        bullets.update()
        bom.reset()
        bom.update()
    display.update()
    clock.tick(FPS)
