# 我方飞船
import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/hero.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.bullet_num = 10

    # 绘制飞机并保证不移出屏幕外
    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.width:
            self.rect.right = self.screen_rect.width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_rect.height:
            self.rect.bottom = self.screen_rect.height

    # 把飞机放置在底部中央
    def put(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

