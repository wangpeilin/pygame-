# 子弹类，分敌我飞船两种
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, plane, is_enemy=False):
        super(Bullet, self).__init__()
        self.screen = screen
        self.is_enemy = is_enemy
        if self.is_enemy:
            self.image = pygame.image.load("images/bullet_1.png")
        else:
            self.image = pygame.image.load("images/bullet_11.png")
        self.rect = self.image.get_rect()
        if self.is_enemy:
            self.rect.centerx = plane.rect.centerx
            self.rect.top = plane.rect.bottom
        else:
            self.rect.centerx = plane.rect.centerx
            self.rect.bottom = plane.rect.top

    # 开火，判断子弹运动方向
    def fire(self, setting):
        if self.is_enemy:
            self.rect.y += setting.enemy_bullet_speed
        else:
            self.rect.y -= setting.ship_bullet_speed

    # 将子弹绘制在屏幕上
    def draw(self):
        self.screen.blit(self.image, self.rect)




