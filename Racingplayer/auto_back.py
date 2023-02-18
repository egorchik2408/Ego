import pygame
import random

width = 1200 # ширина игрового окна
height = 600 # высота игрового окна

img_dir = 'media/img/' # папка с картинками
snd_dir = 'media/snd/' # папка со звуками

class Auto_back(pygame.sprite.Sprite):
  def __init__(self): # Функция, где указываем что будет у авто
      pygame.sprite.Sprite.__init__(self)
    
      self.type = "back"
      self.image = pygame.image.load(img_dir + f"/auto/{random.randint(0,4)}.png")
      self.sound = pygame.mixer.Sound(snd_dir + 'explosion_car.mp3')
      self.rect = self.image.get_rect()
      self.max_speed = 25
      self.min_speed = 2
      self.speed = random.randint(self.min_speed, self.max_speed)
    
      self.global_speed = 0 # Общая скорость движения
      self.global_min_speed = 0 # Общая минимальная скорость движения
      self.global_max_speed = 50 # Общая максимальная скорость движения
      self.rect.y = random.randrange(-height, 0, 300)
      self.points = [(width / 2 - 50), (width / 2 - 130),  (width / 2 - 210), (width / 2 - 290)]
      # Точки спауна по горизонтали          
      
      self.rect.centerx = random.choice(self.points) # Случайное значение центра рамки по оси X
    
      self.image = pygame.transform.rotate(self.image, 180)



    
  def update(self): # Функция, действия которой будут выполняться каждый тик
    keystate = pygame.key.get_pressed() # Сохраняем нажатие на кнопку
    
    if keystate[pygame.K_UP] and self.global_speed <= self.global_max_speed:
      self.global_speed += 1
      
    elif keystate[pygame.K_DOWN] and self.global_speed >= self.global_min_speed:
      self.global_speed -= 1
      
    self.rect.y += self.speed + self.global_speed
      
    if self.rect.top > height: # Если осталась далеко позади
        self.speed = random.randint(self.min_speed, self.max_speed)
        self.rect.centerx = random.choice(self.points)
        self.rect.y = random.randrange(-height, 0, 300) # Спауним сверху
  def get_hit_sprite(hits_dict):
    for hit in hits_dict.values():
      return hit[0]