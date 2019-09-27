# 敌方飞船，生成于屏幕顶端的随机位置
import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, setting):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/img-plane_1.png")
        self.rect = self.image.get_rect()
        self.scr_rect = self.screen.get_rect()
        self.rect.x = random.randint(0, self.scr_rect.width - self.rect.width)
        self.rect.bottom = 0
        self.speed = random.randint(1, 2) * setting.enemy_factor

    # 敌机向下移动
    def update(self):
        self.rect.y += self.speed

    # 将其绘制在屏幕上
    def draw(self):
        self.screen.blit(self.image, self.rect)
