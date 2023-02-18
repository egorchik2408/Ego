import pygame
pygame.init()                           # Инициализируем модуль pygame
from auto_forward import Auto_forward
from auto_back import Auto_back

def get_hit_sprite(hits_dict):  # Функция возвращает спрайт с которым столкнулись
   for hit in hits_dict.values():
       return hit[0]

cars = pygame.sprite.Group()
bullets = pygame.sprite.Group()

width = 1280                            # ширина игрового окна
height = 960                           # высота игрового окна
fps = 30                                # частота кадров в секунду
game_name = "Racing" 

img_dir = "media/img/"
snd_dir = "media/snd/"

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"
GOLD = "#FFD700"


all_sprites = pygame.sprite.Group()
auto_back = Auto_back()
auto_forward = Auto_forward()
all_sprites.add(auto_back)
all_sprites.add(auto_forward)

for i in range(4): # Создаем 4 автомобиля в попутном направлении
 auto = Auto_forward()
 all_sprites.add(auto)
 cars.add(auto)

for i in range(4): # Создаем 4 автомобиля во встречном направлении
 auto = Auto_back()
 all_sprites.add(auto)
 cars.add(auto)

#Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)   # Заголовок окна
icon = pygame.image.load(img_dir + 'icon.png')  # загружаем файл с иконкой
pygame.display.set_icon(icon)  # устанавливаем иконку в окно
timer = pygame.time.Clock()             # Создаем таймер pygame
run = True

while run:                              # Начинаем бесконечный цикл
    timer.tick(fps)
    all_sprites.update() # Выполняем действия всех спрайтов в группе
    
    for event in pygame.event.get():     # Обработка ввода (события)
     
        if event.type == pygame.QUIT:  # Проверить закрытие окна
            
          run = False                  # Завершаем игровой цикл
          
    hit_bullets = pygame.sprite.groupcollide(bullets, cars, True, False)
    if hit_bullets:
      car = get_hit_sprite(hit_bullets)
      car.sound.play()
      if car.type == 'forward':
          auto = Auto_forward()
          cars.add(auto)
          auto.sound.play()
          all_sprites.add(auto)
      else:
         auto = Auto_back()
         cars.add(auto)
         auto.sound.play()
         all_sprites.add(auto)
      car.kill()
            
    for car in cars:
      cars.remove(car)
      hit_another_car = pygame.sprite.spritecollide(car,cars,False)
      if hit_another_car:
        car.sound.play()
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
          
    # Рендеринг (прорисовка)
    screen.fill(GREEN) # Заливка заднего фона
    all_sprites.draw(screen) # Отрисовываем все спрайты
    pygame.display.update()                 # Переворачиваем экран
  
pygame.quit()                              # Корректно завершаем игру