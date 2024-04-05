import pygame
from config import BULLET_SPEED
from math import sin, cos


class Bullet:
    def __init__(self, x: float, y: float, angle: float) -> None:
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self, dt: float, screen: pygame.Surface):
        pygame.draw.circle(screen, (207, 159, 183), (self.x, self.y), 5)
        self.x += dt * BULLET_SPEED * cos(self.angle)
        self.y += dt * BULLET_SPEED * sin(self.angle)
