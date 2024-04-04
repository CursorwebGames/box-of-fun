from random import randint
from config import WIDTH, HEIGHT, STAR_SIZE
import pygame

stars = []
for _ in range(0, 500):
    stars.append((randint(0, WIDTH), randint(0, HEIGHT), randint(1, STAR_SIZE)))


def draw_stars(screen: pygame.Surface):
    for x, y, r in stars:
        pygame.draw.circle(screen, (133, 133, 143), (x, y), r)
