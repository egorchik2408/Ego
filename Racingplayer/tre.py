import pygame
import random

width = 1200 # ширина игрового окна
height = 600 # высота
img_dir = "media/img/"
snd_dir = "media/snd/"

class Tree(pygame.sprite.Sprite):
  def __init__(self): # Функция, где указываем что будет у c
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(img_dir+f"trees/{random.randint(1,16)}.png")
    self.rect = self.image.get_rect()
    self.side = random.choice(['left','right'])
    if self.side == 'left':
      self.rect.x = width/2 - 450 - random.randint(10,170)
      self.rect.y = height - random.randint(0, 450)
    elif self.side == 'right':
      self.rect.x = width/2 + 380 + random.randint(10,100)
      self.rect.y = height - random.randint(0,450)
    self.max_speed = 50
    self.min_speed = 0
    self.speed = 0

  
  def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and self.speed < self.max_speed:
            self.speed += 1
        elif keystate[pygame.K_DOWN] and self.speed > self.min_speed:
            self.speed -= 1
        self.rect.y += self.speed
        if self.rect.top > height:
            self.rect.y = random.randrange(-height, 0, 50)
            self.side = random.choice(['left', 'right'])
            if self.side == 'left':
                self.rect.x = width // 2 - 450 - random.randint(10, 350)
            elif self.side == 'right':
                self.rect.x = width // 2 + 380 + random.randint(10, 350)