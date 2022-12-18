import pygame
import random
from pygame.math import Vector2
width = 1366
height = 768

snd_dir = 'media/snd/'
img_dir = 'media/img/'


class Enemy_bottom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir+ 'enemy_bottom/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)
        self.rect.y = height - 100

        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0

        self.speedx = random.randint(1, 5)
        self.speedy = random.randint(-5, 5)

        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl.mp3")
        self.snd_expl.set_volume(0.1)

    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed
        self.image = pygame.transform.rotate(self.copy, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.rotate(5)
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.bottom < 0 or self.rect.left > width or self.rect.top > height:
            self.rect.x = 0
            self.rect.y = random.randint(0, height)
            self.speedx = random.randint(1, 5)
            self.speedy = random.randint(-5, 5)