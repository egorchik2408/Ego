import pygame
from pygame.math import Vector2


width = 1366
height = 768

snd_dir = 'media/snd/'
img_dir = 'media/img/'


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + 'player/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = width/2
        self.rect.y = height/2
        self.speed = 10

        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0

        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl.mp3")
        self.snd_expl.set_volume(0.1)
        self.snd_shoot = pygame.mixer.Sound(snd_dir + "shoot.mp3")
        self.snd_shoot.set_volume(0.1)
        self.snd_scratch = pygame.mixer.Sound(snd_dir + "scratch.mp3")
        self.snd_scratch.set_volume(0.1)

        self.hp = 500

    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed
        self.image = pygame.transform.rotate(self.copy, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.rotate(-5)
        if keystate[pygame.K_LEFT]:
            self.rotate(5)
        if keystate[pygame.K_UP]:
            self.position += self.speed * self.direction
            self.rect.center = self.position
        if keystate[pygame.K_DOWN]:
            self.position -= self.speed * self.direction
            self.rect.center = self.position