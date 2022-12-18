import pygame
import random
from pygame.math import Vector2

width = 1366
height = 768

snd_dir = 'media/snd/'
img_dir = 'media/img/'

class Bullet (pygame.sprite.Sprite):
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir+'bullet.png' )
        self.image = pygame.transform.rotate(self.image,player.angle)
        self.rect = self.image.get_rect()

        self.rect.center = Vector2(player.rect.center)
        self.speed = 30
        self.move = self.speed * player.direction

    def update(self):
        self.rect.center += self.move