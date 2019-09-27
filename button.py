# play按钮，控制着游戏的活跃状态
import pygame.font


class Button():
    def __init__(self, screen, text, size):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(0, 0, 200, 50)
        self.rect.center = self.screen_rect.center

        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, size)

        self.render_text(text)

    def render_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color,
                                           self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
