from pygame import *
x = 500
y = 700
screen = display.set_mode((x,y))
display.set_caption('Pony Jump')
background = transform.scale(image.load('clouds.png'), (x,y))


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
        None
    clock.tick(FPS)
    display.update()