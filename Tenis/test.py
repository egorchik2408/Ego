import pygame

pygame.init()

width = 800
height = 600
game_name = 'Game1'
fps = 60
color = (224, 110, 110)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

smile = pygame.image.load('smile.png')
sm_rect = smile.get_rect()

racket = pygame.image.load('racket.png')
racket_rect = racket.get_rect()

racket_rect.x = width / 2 - racket.get_width()/2
racket_rect.y = height - 50

speedx = 1
speedy = 1

run = True
while run:
    event = pygame.event.get()
    for event in event:
        if event.type == pygame.QUIT:
            run = False

    screen.fill(color)
    sm_rect.x += speedx
    sm_rect.y += speedy
    screen.blit(smile, sm_rect)
    screen.blit(racket, racket_rect)

    if sm_rect.bottom > height:
        speedy = - speedy
    if sm_rect.bottom > width:
        speedx = - speedx
    if sm_rect.top < 0:
        speedy = - speedy
    if sm_rect.top > 0:
        speedx = - speedx

    clock.tick(fps)
    pygame.display.update()

pygame-quit()
