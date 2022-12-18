import random
import pygame

def draw_text(screen,text,size,x,y,color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_imag = font.render(text, True, color)
    text_rect = text_imag.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_imag,text_rect)


pygame.init()

widht = 1200
height = 700
game_name ='Game1'
fps = 60
color = (158,4,219)

screen = pygame.display.set_mode((widht, height))
pygame.display.set_caption(game_name)

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

smile = pygame.image.load('smile.png')
sm_rect = smile.get_rect()

racket = pygame.image.load('racket.png')
racket_rect = racket.get_rect()

racket_rect.x = widht/ 2 - racket.get_width()
racket_rect.y = height - 50

bg = pygame.image.load('bg.jpg')
bg_rect = bg.get_rect()

speedx = 9
speedy = 9

lives = 3

ping = pygame.mixer.Sound('ping.mp3')
loose = pygame.mixer.Sound('loose.mp3')

pygame.mixer.music.load('8bit.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)



run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key [pygame.K_LEFT] and racket_rect.left > 0:
        racket_rect.x -= 10
    if key [pygame.K_RIGHT] and racket_rect.right < widht:
        racket_rect.x += 10

    screen.blit(bg,bg_rect)
    sm_rect.x += speedx
    sm_rect.y += speedy
    screen.blit(smile, sm_rect)
    screen.blit(racket, racket_rect)
    draw_text(screen,'lives:'+str(lives),30,widht//2,30,(255,255,255))

    bg_rect.x -= 2
    if bg_rect.x <-widht:
        bg_rect.x = 0

    if sm_rect.bottom > height:
        lives -= 1
        loose.play()
        sm_rect.x = random.randint(0, widht - sm_rect.width)
        sm_rect.y = 0
        if lives == 0:
            run = False
            print('game over')
    if sm_rect.right > widht:
        speedx = -speedx
    if sm_rect.top < 0:
        speedy = -speedy
    if sm_rect.left < 0:
        speedx = -speedx

    if sm_rect.colliderect(racket_rect):
        ping.play()
        speedy =- speedy

    clock.tick(fps)
    pygame.display.update()

pygame.quit()

