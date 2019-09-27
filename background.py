# 游戏背景地图，两张相同的图片持续滚动
import pygame


class Background():
    def __init__(self, screen, screen_size, setting):
        self.image1 = pygame.image.load("images/img_bg_level_1.jpg")
        self.image2 = pygame.image.load("images/img_bg_level_1.jpg")

        self.screen = screen
        self.size = screen_size

        self.y1 = 0
        self.y2 = -self.size[1]

    def action(self):
        self.y1 += 0.5
        self.y2 += 0.5
        if self.y1 >= self.size[1]:
            self.y1 = 0
        if self.y2 >= 0:
            self.y2 = -self.size[1]

    def draw(self):
        self.screen.blit(self.image1, (0, self.y1))
        self.screen.blit(self.image2, (0, self.y2))

    def refresh(self, setting):
        self.image1 = pygame.image.load("images/img_bg_level_" + str(setting.level) + ".jpg")
        self.image2 = pygame.image.load("images/img_bg_level_" + str(setting.level) + ".jpg")
