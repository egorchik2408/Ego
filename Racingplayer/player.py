import pygame
width = 1200
height = 600
img_dir = 'media/img/' 
snd_dir = 'media/snd/' 

class Player(pygame.sprite.Sprite):
  def __init__(self):
     pygame.sprite.Sprite.__init__(self)
     self.image = pygame.image.load(img_dir+"player.png")
     self.rect = self.image.get_rect()
     self.rect.x = width // 2
     self.rect.y = height - 100
     self.sound_move = pygame.mixer.Sound(snd_dir + 'motor.mp3')
     self.sound_bum=pygame.mixer.Sound(snd_dir+'explosion_player.mp3')
     self.sound_shoot = pygame.mixer.Sound(snd_dir + 'shoot.mp3')
     self.max_speed = 50
     self.min_speed = 0
     self.speed = 0
     self.score = 0
  def update(self):
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT]:
      self.rect.x += 15
    elif keystate[pygame.K_LEFT]:
      self.rect.x -= 15
    elif keystate[pygame.K_UP] and self.speed < self.max_speed:
      self.speed += 1
    elif keystate[pygame.K_DOWN] and self.speed > self.min_speed:
      self.speed -= 1
    if self.speed > 0:
      self.sound_move.play()
    if self.speed > 0 and not pygame.mixer.get_busy():
      self.sound_move.play()
    if self.speed == 0:
      self.sound_move.stop()