import pygame
from pygame.math import Vector2
width = 1200
height = 600
img_dir = 'media/img/' 
snd_dir = 'media/snd/'

class Bullet(pygame.sprite.Sprite):
  def __init__(self, player):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(img_dir + 'shell.png')
    self.image = pygame.transform.scale(self.image, (4, 15))
    self.rect = self.image.get_rect()
    self.rect.center = player.rect.center
    self.speed = 50

  def update(self):
    self.rect.y -= self.speed
    if self.rect.bottom < 0:
      self.kill()