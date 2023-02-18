import pygame
import random

width = 1200 # ширина игрового окна
height = 600 # высота игрового окна

img_dir = 'media/img/' # папка с картинками
snd_dir = 'media/snd/' # папка со звуками

class Auto_forward(pygame.sprite.Sprite):
    def __init__(self):   #Функция, где указываем что будет у игрока
        pygame.sprite.Sprite.__init__(self)
        self.type = 'forward'
        self.points = [(width // 2 + 50),
                      (width // 2 + 130),
                      (width // 2 + 210),
                      (width // 2 + 290)]
        self.image = pygame.image.load(img_dir + f"/auto/{random.randrange(5)}.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(self.points)
        self.min_speed = 5            # Минимальная скорость движения
        self.max_speed = 20           # Максимальная скорость движения
        self.speed = -random.randint(self.min_speed , self.max_speed)

        self.global_speed = 0          # Общая скорость движения
        self.global_min_speed = 0      # Общая минимальная скорость движения
        self.global_max_speed = 50     # Общая максимальная скорость движения

        self.sound = pygame.mixer.Sound(snd_dir + 'explosion_car.mp3')

        self.rect.y = random.randrange(-height, 0, 300)

    def update(self):  # Функция, действия которой будут выполняться каждый тик

        keystate = pygame.key.get_pressed()  # Сохраняем нажатие на кнопку
        if keystate[pygame.K_UP] and self.global_speed < self.global_max_speed:
            self.global_speed += 1
        elif keystate[pygame.K_DOWN] and self.global_speed > self.global_min_speed:
            self.global_speed -= 1


        self.rect.y += self.speed + self.global_speed

        if self.rect.top > height*2:      # Если осталась далеко позади
            self.speed = -random.randint(self.min_speed, self.max_speed)
            self.rect.center = (random.choice(self.points), random.randrange(-height, 0, 300))