import sys
import pygame
from background import Background
from ship import Ship
from enemy import Enemy
from bullets import Bullet
from bomb import Bomb
from settings import Settings
from button import Button
from score import Score

# 控制对按空格键的持续响应
global pretime
pretime = pygame.time.get_ticks()
# 控制敌机产生的时间间隔
create_enemy = pygame.USEREVENT + 1
pygame.time.set_timer(create_enemy, 2500)
# 控制关卡的刷新时间
refresh_level = pygame.USEREVENT + 2
pygame.time.set_timer(refresh_level, 60000)


def update_ship(screen, ship, ship_bullets):
    # 按下空格键时持续开火
    if pygame.key.get_pressed()[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            global pretime
            interval = current_time - pretime
            if interval >= 300 and len(ship_bullets) < ship.bullet_num:
                new_bullet = Bullet(screen, ship)
                ship_bullets.add(new_bullet)
                pretime = current_time


def detect_collision(screen, ship, ship_bullets, enemys, enemys_bullets, bombs, setting, score):
    # 爆炸时播放音效
    music = "images/bomb.wav"
    pygame.mixer.Sound(music)
    pygame.mixer.Sound(music).set_volume(0.1)
    # 检测到击中敌机
    hit = pygame.sprite.groupcollide(enemys, ship_bullets, True, True)
    if hit:
        for enemy in hit:
            pygame.mixer.Sound(music).play()
            # 加分并检测是否刷新最高分
            setting.score += setting.points
            score.render_score()
            if setting.score > setting.high_score:
                setting.high_score = setting.score
                score.render_high_score()
            # 播放爆炸动画
            enemy_rect = enemy.rect
            bomb = Bomb(screen)
            bomb.set_pos(enemy_rect.x, enemy_rect.y)
            bombs.add(bomb)
            bomb.visible = True

    # 检测到我方飞机被击中就清空屏幕，减少一条命，判断游戏状态
    if pygame.sprite.spritecollideany(ship, enemys) \
            or pygame.sprite.spritecollideany(ship, enemys_bullets):
        enemys.empty()
        enemys_bullets.empty()
        pygame.mixer.Sound(music).play()

        bomb = Bomb(screen)
        bomb.set_pos(ship.rect.x, ship.rect.y)
        bombs.add(bomb)
        bomb.visible = True

        setting.live -= 1
        if setting.live > 0:
            ship.put()
        else:
            setting.game_active = False


def update_screen(setting, background, ship, ship_bullets, enemys, enemys_bullets, bombs, play_button, score):
    # 地图滚动
    background.action()
    background.draw()

    # 绘制我方飞机，更新我方飞机子弹，删除消失的子弹
    ship.draw()
    for bullet in ship_bullets.sprites():
        bullet.fire(setting)
        bullet.draw()
    for bullet in ship_bullets.copy():
        if bullet.rect.bottom <= 0:
            ship_bullets.remove(bullet)

    # 更新敌方飞机和子弹，删除消失的敌机和子弹
    for enemy in enemys.sprites():
        enemy.update()
        enemy.draw()
    for enemy in enemys.copy():
        if enemy.rect.y >= enemy.scr_rect.height:
            enemys.remove(enemy)

    for bullet in enemys_bullets.sprites():
        bullet.fire(setting)
        bullet.draw()
    for bullet in enemys_bullets.copy():
        if bullet.rect.bottom >= background.size[1]:
            enemys_bullets.remove(bullet)

    # 播放爆炸效果
    for bomb in bombs.sprites():
        bomb.action()
        bomb.draw()

    # 刷新得分和生命次数
    score.show_score()
    score.show_live()

    # 死亡后停止游戏，绘制play按钮
    if not setting.game_active:
        play_button.draw_button()

    pygame.display.update()


def run_game():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("images/bg2.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1, 0)

    icon = pygame.image.load("images/app.ico")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Aircraft war")
    screen_size = (512, 768)
    screen = pygame.display.set_mode(screen_size)

    setting = Settings()
    score = Score(setting, screen)
    background = Background(screen, screen_size, setting)
    play_button = Button(screen, 'Play', 48)
    ship = Ship(screen)
    ship_bullets = pygame.sprite.Group()
    enemys = pygame.sprite.Group()
    enemys_bullets = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

    while True:
        for event in pygame.event.get():      # 这句话只能有一个
            if event.type == pygame.QUIT:
                sys.exit()

            if not setting.game_active:
                # 按Play键重置并开始游戏
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = pygame.mouse.get_pos()
                    if play_button.rect.collidepoint(click):
                        setting.reset()
                        score.render_score()
                        background.refresh(setting)
                        enemys.empty()
                        enemys_bullets.empty()
                        ship.put()
                        setting.game_active = True

            if setting.game_active:
                # 更新我方飞机位置
                update_ship(screen, ship, ship_bullets)
                # 鼠标拖动飞机
                if event.type == pygame.MOUSEMOTION:
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0]:
                        position = pygame.mouse.get_pos()
                        ship.rect.centerx = position[0]
                        ship.rect.centery = position[1]
                # 每隔2.5秒飞下来4架敌机并发射子弹
                if event.type == create_enemy:
                    enemy = [Enemy(screen, setting) for _ in range(4)]
                    enemys.add(enemy)
                    for i in enemys.sprites():
                        enemy_bullet = Bullet(screen, i, is_enemy=True)
                        enemys_bullets.add(enemy_bullet)
                # 每隔60秒更新关卡
                if event.type == refresh_level:
                    setting.refresh_level()
                    background.refresh(setting)

        detect_collision(screen, ship, ship_bullets, enemys, enemys_bullets, bombs, setting, score)
        update_screen(setting, background, ship, ship_bullets, enemys, enemys_bullets, bombs, play_button, score)


if __name__ == "__main__":
    run_game()


