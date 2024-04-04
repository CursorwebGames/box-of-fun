"""
Shooter game where player moves on an infinity
Makes aiming and stuff harder

also if you let any past you you lose 1 of your 5 lives (or if you touch it).

hanzi!!
"""

import pygame

pygame.init()
pygame.font.init()

from random import randint
from config import WIDTH, HEIGHT, ENEMY_FREQ

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

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            player.shoot(bullets)

    # Drawing
    screen.fill((1, 0, 51))
    draw_stars(screen)

    player.draw(dt, screen)

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
        enemy.draw(dt, screen)

    # Updating
    pygame.display.flip()
    dt = clock.tick(0) / 1000

pygame.quit()
