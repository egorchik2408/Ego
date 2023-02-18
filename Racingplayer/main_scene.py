import pygame
from road import Road
from board import Board
from tre import Tree
from explosion import Explosion
pygame.init()                           # Инициализируем модуль pygame

width = 1200                            # ширина игрового окна
height = 600                            # высота игрового окна
fps = 240                               # частота кадров в секунду
game_name = "Racing"                   # название нашей игры

img_dir = "media/img/"
snd_dir = "media/snd/"

pygame.mixer.music.load(snd_dir + "music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


def draw_text(screen, text, size, x, y, color):
    font_name = "media/font.ttf"
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)



icon = pygame.image.load(img_dir + 'icon.png') # Загружаем файл с иконкой
pygame.display.set_icon(icon) # Устанавливаем иконку в окно

all_sprites = pygame.sprite.Group() # Создаем группу для спрайтов
  
tre = Tree()
road = Road()
boardl = Board('left')
boardr = Board('right')
all_sprites.add(road, boardl, boardr, tre)

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"
GOLD = "#FFD700"

#Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)   # Заголовок окна
icon = pygame.image.load(img_dir + 'icon.png')  # загружаем файл с иконкой
pygame.display.set_icon(icon)  # устанавливаем иконку в окно
timer = pygame.time.Clock()             # Создаем таймер pygame
run = True

while run:                              # Начинаем бесконечный цикл
    timer.tick(fps)			            # Контроль времени (обновление игры)
    all_sprites.update() # Выполняем действия всех спрайтов в групп
    for event in pygame.event.get():     # Обработка ввода (события)
        if event.type == pygame.QUIT:    # Проверить закрытие окна
            run = False                  # Завершаем игровой цикk
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:                       
            expl = Explosion([width/2,height/2])
            all_sprites.add(expl)

    # Рендеринг (прорисовка)
    all_sprites.draw(screen)
    draw_text(screen, r'Score = {player.score}', 50,120,20, GOLD)
    pygame.display.update()  # Переворачиваем экран

pygame.quit()  




    

