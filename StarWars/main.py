import pygame
from player import Player
from enemy_bottom import Enemy_bottom
from enemy_left import Enemy_left
from enemy_top import Enemy_top
from enemy_right import Enemy_right
from bullet import Bullet

def get_hit_sprite(hits_dict):
    for hit in hits_dict.values():
        return hit[0]


pygame.init()

width = 1366
height = 768
fps = 30
game_name = "Shooter"

snd_dir = 'media/snd/'
img_dir = 'media/img/'
icon = pygame.image.load(img_dir + 'icon.png')
pygame.display.set_icon(icon)

BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)


all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
bullets_sprites = pygame.sprite.Group()
players_sprites = pygame.sprite.Group()

player = Player()
enemy_bottom = Enemy_bottom()
enemy_left = Enemy_left()
enemy_top = Enemy_top()
enemy_right = Enemy_right()

enemy_sprites.add([enemy_left, enemy_right, enemy_top, enemy_bottom])
players_sprites.add(player)

all_sprites.add(player)
all_sprites.add(enemy_bottom)
all_sprites.add(enemy_left)
all_sprites.add(enemy_top)
all_sprites.add(enemy_right)

timer = pygame.time.Clock()
run = True

while run:
   timer.tick(fps)
   all_sprites.update()

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
       if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player)
                all_sprites.add(bullet)
                bullets_sprites.add(bullet)

   shots = pygame.sprite.groupcollide(bullets_sprites, enemy_sprites, True, True)
   if shots:
        sprite = get_hit_sprite(shots)
        sprite.snd_expl.play()
   if scratch:
        sprite = get_hit_sprite(scratch)
        sprite.snd_scratch.play()

   screen.fill(CYAN)
   all_sprites.draw(screen)
   pygame.display.update()
pygame.quit()