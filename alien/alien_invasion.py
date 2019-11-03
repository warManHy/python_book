# coding: utf-8
import sys
import pygame
from settings import Settings
from ship import Ship
import game_fuc as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并且创建一个屏幕对象
    pygame.init()
    # screen = pygame.display.set_mode((800, 600))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    pygame.display.set_caption("Alien Invasion")
    #bgcolor
    # bg_color = (230, 230, 230)

    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets)
        # gf.check_events(ai_settings, screen, ship)
        #让最近绘制的屏幕可见
        # screen.fill(bg_color)
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # pygame.display.flip()
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        # gf.update_screen(ai_settings, screen, ship)
        
run_game()
