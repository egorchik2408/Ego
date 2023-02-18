import pygame
from player import Player
from speedometr import Speedometr
from arrow import Arrow
from bullet import Bullet
from road import Road
from board import Board
from tre import Tree
from explosion import Explosion
from auto_forward import Auto_forward
from auto_back import Auto_back
import time
def get_hit_sprite(hits_dict):  # Функция возвращает спрайт с которым столкнулись
   for hit in hits_dict.values():
       return hit[0]
pygame.init()                           

  
def draw_text(screen, text, size, x, y, color):
    font_name = "media/font.ttf"
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)

pygame.init()

width = 1200
height = 600
fps = 600
game_name = "Steet racing"

img_dir = "media/img/"
snd_dir = "media/snd/"

pygame.mixer.music.load(snd_dir + "music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"
GOLD = "#FFD700"
players = pygame.sprite.Group()
cars = pygame.sprite.Group()
boards = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
players.add(player)
sped = Speedometr()
arow = Arrow()


all_sprites = pygame.sprite.Group()
auto_back = Auto_back()
auto_forward = Auto_forward()
all_sprites.add(auto_back)
all_sprites.add(auto_forward)
tre = Tree()
road = Road()
boardl = Board('left')
boardr = Board('right')
all_sprites.add(road, boardl, boardr, tre)

all_sprites.add(player, sped, arow)

for i in range(4): # Создаем 4 автомобиля в попутном направлении
 auto = Auto_forward()
 all_sprites.add(auto)
 cars.add(auto)

for i in range(4): # Создаем 4 автомобиля во встречном направлении
 auto = Auto_back()
 all_sprites.add(auto)
 cars.add(auto)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)
icon = pygame.image.load(img_dir + 'icon.png')
pygame.display.set_icon(icon)
timer = pygame.time.Clock()

run = True

while run:
  timer.tick(fps)
  all_sprites.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      expl = Explosion(player.rect.center)  # Создаем взрыв на месте игрока
      all_sprites.add(expl)

    if event.type == pygame.KEYDOWN: # Если клавиша нажата
      if event.key == pygame.K_SPACE:
        player.sound_shoot.play()
    
        bullet = Bullet(player) # Создаем пулю
        all_sprites.add(bullet) # Добавляем пулю ко всем спрайтам
        bullets.add(bullet)
      if event.key == pygame.K_q:                       
          expl = Explosion([width/2,height/2])
          all_sprites.add(expl)
  hit_boards = pygame.sprite.groupcollide(players, boards, False, False)

  hit_cars = pygame.sprite.groupcollide(players, cars, False, False)

  hit_bullets = pygame.sprite.groupcollide(bullets, cars, True, False)
  if hit_bullets:
    car = get_hit_sprite(hit_bullets)
    car.sound.play()
    expl = Explosion(player.rect.center)  # Создаем взрыв на месте игрока
    all_sprites.add(expl)
    if car.type == 'forward':
        auto = Auto_forward()
        cars.add(auto)
        auto.sound.play()
        all_sprites.add(auto)
        player.score += 10
    else:
        auto = Auto_back()
        cars.add(auto)
        auto.sound.play()
        all_sprites.add(auto)
        player.score += 10
    car.kill()

  if hit_boards or hit_cars:
    player.speed = 0
    player.sound_bum.play()
    player.kill()
  
  for car in cars:
      cars.remove(car)
      hit_another_car = pygame.sprite.spritecollide(car,cars,False)
      if hit_another_car:
        car.sound.play()
        expl = Explosion(player.rect.center)  # Создаем взрыв на месте игрока
        all_sprites.add(expl)

        if car.type == 'forward':
            auto = Auto_forward()
            cars.add(auto)
            all_sprites.add(auto)    
        else:
          auto = Auto_back()
          cars.add(auto)
          all_sprites.add(auto)
        car.kill()
      else:
        cars.add(car)
        end_time = time.time()  # Запоминаем время смерти игрока

  screen.fill(GREEN)
  all_sprites.draw(screen)
  draw_text(screen, r'Score = {player.score}', 50, 120, 20, GOLD)
  if len(players) == 0:
      draw_text(screen, 'Game Over', 100, width / 2, height / 2 - 50, WHITE)
      draw_text(screen, f'Score = {player.score}', 100, width / 2, height / 2 + 50, WHITE)


  if time.time() - end_time > 5 and len(players) == 0:
    run = False
  pygame.display.update()
  
pygame.quit()