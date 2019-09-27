# 爆炸特效
import pygame


class Bomb(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Bomb, self).__init__()
        self.screen = screen
        self.image = [pygame.image.load("images/bomb-" + str(i) + ".png") for i in range(1, 8)]
        self.index = 0
        self.interval = 20
        self.interval_index = 0
        self.position = [0, 0]
        self.visible = False

    def set_pos(self, x, y):
        self.position[0] = x
        self.position[1] = y

    def action(self):
        if self.visible:
            self.interval_index += 1
            if self.interval_index < self.interval:
                return
            else:
                self.interval_index = 0
                self.index += 1
                if self.index >= len(self.image):
                    self.index = 0
                    self.visible = False

    def draw(self):
        if self.visible:
            self.screen.blit(self.image[self.index], self.position)


