# 游戏的整体设置
import pygame

class Settings():
    def __init__(self):
        self.reset()
        self.speed_acc = 1.2
        self.score_acc = 1.5
        self.game_active = False
        self.high_score = 0

    # 每次点击play按钮重置这些设置
    def reset(self):
        self.live = 3
        self.score = 0
        self.points = 50
        self.level = 1
        self.enemy_factor = 1
        self.enemy_bullet_speed = 2
        self.ship_bullet_speed = 1

    # 每次刷新关卡时加快游戏速度
    def refresh_level(self):
        if self.level < 5:
            self.level += 1
        self.enemy_factor *= self.speed_acc
        self.enemy_bullet_speed *= self.speed_acc
        self.ship_bullet_speed *= self.speed_acc
        self.points = int(self.points * self.score_acc)

    def show_live(self):
        live = pygame.image.load("images/heart2.png")
        for num in range(self.setting.live):
            x = num * 40
            y = self.screen_rect.bottom - 40
            self.screen.blit(live, (x, y))


