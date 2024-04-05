"""
Shooter game where player moves on an infinity
Makes aiming and stuff harder

also if you let any past you you lose 1 of your 10 lives (or if you touch it).

hanzi!!
"""

import pygame

pygame.init()
pygame.font.init()

from random import randint
from config import WIDTH, HEIGHT, ENEMY_FREQ
from util import circle_col

from player import Player
from enemy import Enemy
from bullet import Bullet
from stars import draw_stars

from typing import Literal


pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

running = True
dt = 0
lose_menu_pause = 1

player = Player()
enemies: list[Enemy] = []
bullets: list[Bullet] = []

game_font = pygame.font.SysFont("Kaiti", 25)
title_font = pygame.font.SysFont("Consolas", 50)
title_font2 = pygame.font.SysFont("Consolas", 30)
title_font3 = pygame.font.SysFont("Kaiti", 40)


mouse_pressed = False

scene = "menu"


def menu():
    global scene, running

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            scene = "game"

    screen.fill((1, 0, 51))
    draw_stars(screen)

    title = title_font.render("NUMBER SHOOTER", True, (255, 255, 255))
    titlew = title.get_width()
    screen.blit(title, (WIDTH / 2 - titlew / 2, 50))

    title_cn = title_font3.render("数字射击游戏", True, (105, 152, 255))
    title_cnw = title_cn.get_width()
    screen.blit(title_cn, (WIDTH / 2 - title_cnw / 2, 100))

    explain = title_font2.render("Click to begin", True, (189, 207, 217))
    explainw = explain.get_width()
    explainh = explain.get_height()
    screen.blit(explain, (WIDTH / 2 - explainw / 2, HEIGHT - explainh - 20))


def game():
    global scene, running, mouse_pressed

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

    # Drawing
    screen.fill((1, 0, 51))
    draw_stars(screen)

    player.draw(dt, screen)

    if mouse_pressed:
        player.shoot(bullets)

    # Bullet Draw
    for i in range(len(bullets) - 1, 0, -1):
        bullet = bullets[i]
        if (
            bullet.x > WIDTH + 5
            or bullet.x < -5
            or bullet.y > HEIGHT + 5
            or bullet.y < -5
        ):
            del bullets[i]
        bullet.draw(dt, screen)

    # Enemy Add
    if randint(1, ENEMY_FREQ) == 1:
        enemies.append(Enemy())

    for i in range(len(enemies) - 1, 0, -1):
        enemy = enemies[i]

        if enemy.y > HEIGHT + 50:
            player.lives -= 1
            del enemies[i]

        if circle_col(player.get_pos(), 25, (enemy.x, enemy.y), enemy.get_rad()):
            player.hurt()
            del enemies[i]

        for b in range(len(bullets) - 1, 0, -1):
            bullet = bullets[b]
            if circle_col((bullet.x, bullet.y), 5, (enemy.x, enemy.y), enemy.get_rad()):
                if enemy.sides > 3:
                    enemy.sides -= 1
                else:
                    del enemies[i]

                player.score += 1
                del bullets[b]

        enemy.draw(dt, screen)

    if player.lives <= 0:
        scene = "lose"

    score = game_font.render(f"分：{player.score}", True, (255, 255, 255))
    screen.blit(score, (0, 0))

    lives = game_font.render(f"命：", True, (255, 255, 255))
    screen.blit(lives, (0, 25))

    for i in range(min(player.lives, 5)):
        pygame.draw.rect(
            screen, (255, 255, 255, 125), (lives.get_width() + i * 10, 25, 8, 10)
        )

    if player.lives > 5:
        for i in range(player.lives - 5):
            pygame.draw.rect(
                screen,
                (255, 255, 255, 125),
                (lives.get_width() + i * 10, 25 + 12, 8, 10),
            )


def lose():
    global running, scene, player, enemies, bullets, lose_menu_pause
    screen.fill((1, 0, 51))
    draw_stars(screen)

    title = title_font.render("GAME OVER!!", True, (255, 255, 255))
    titlew = title.get_width()
    screen.blit(title, (WIDTH / 2 - titlew / 2, 50))

    title_cn = title_font3.render("游戏结束了！", True, (105, 152, 255))
    title_cnw = title_cn.get_width()
    screen.blit(title_cn, (WIDTH / 2 - title_cnw / 2, 100))

    score_display = title_font.render(f"Score: {player.score}", True, (255, 205, 97))
    score_displayw = score_display.get_width()
    screen.blit(score_display, (WIDTH / 2 - score_displayw / 2, 300))

    explain = title_font2.render("Click to go to menu", True, (189, 207, 217))
    explainw = explain.get_width()
    explainh = explain.get_height()
    screen.blit(explain, (WIDTH / 2 - explainw / 2, HEIGHT - explainh - 20))

    lose_menu_pause -= dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP and lose_menu_pause <= 0:
            player = Player()
            enemies = []
            bullets = []
            scene = "menu"
            lose_menu_pause = 1


while running:
    if scene == "menu":
        menu()

    if scene == "game":
        game()

    if scene == "lose":
        lose()

    # Updating
    pygame.display.flip()
    dt = clock.tick(0) / 1000

pygame.quit()
