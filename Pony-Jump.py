from pygame import *
x = 500
y = 700
screen = display.set_mode((x,y))
display.set_caption('Pony Jump')
background = transform.scale(image.load('clouds.png'), (x,y))

mixer.init()
#!mixer.music.load('.mp3')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < 635:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 435:
            self.rect.x += self.speed

FlutterShy = Player('Pony.jpg', 225, 500, 5)

class Wall(GameSprite):
    def update_w():
        None
    def spawn():
        None
#игра
game = True
clock = time.Clock()
FPS = 60
finished = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    screen.blit(background, (0,0))
    if not finished:
        
        FlutterShy.update()
        FlutterShy.reset()

    clock.tick(FPS)
    display.update()
