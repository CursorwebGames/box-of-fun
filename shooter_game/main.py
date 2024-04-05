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


pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

running = True
dt = 0

player = Player()
enemies: list[Enemy] = []
bullets: list[Bullet] = []

game_font = pygame.font.SysFont("Kaiti", 25)

mouse_pressed = False

while running:
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

    # Updating
    pygame.display.flip()
    dt = clock.tick(0) / 1000

pygame.quit()
