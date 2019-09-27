# 游戏的分数和剩余的生命次数
import pygame.font


class Score():
    def __init__(self, setting, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = setting
        self.bg_color = (210, 210, 210)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.render_score()
        self.render_high_score()

    def render_score(self):
        score_str = "{:,}".format(self.setting.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = self.score_rect.height + 20

    def render_high_score(self):
        high_score_str = "{:,}".format(self.setting.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 10
        self.high_score_rect.top = 10

    def show_live(self):
        live = pygame.image.load("images/heart.png")
        for num in range(self.setting.live):
            x = num * 40
            y = self.screen_rect.bottom - 40
            self.screen.blit(live, (x, y))

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
