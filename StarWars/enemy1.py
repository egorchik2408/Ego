import pygame

width = 1366
height = 768

snd_dir = 'media/snd/'
img_dir = 'media/img/'


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir+ 'player/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = width/2
        self.rect.y = height/2
