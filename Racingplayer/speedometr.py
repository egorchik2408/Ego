import pygame
width = 1200 
height = 600 
img_dir = 'media/img/' 
snd_dir = 'media/snd/' 

class Speedometr(pygame.sprite.Sprite):
 def __init__(self): 
  pygame.sprite.Sprite.__init__(self)
  self.image = pygame.image.load(img_dir+"speedometr.png")
  self.image = pygame.transform.scale(self.image, (200, 200))
  self.rect = self.image.get_rect()
  self.rect.center = [width - 1100, height - 70]