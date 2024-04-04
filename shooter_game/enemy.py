from random import randint
from math import pi, sin, cos
from config import WIDTH
import pygame

names = list("零一二三四五六七八九十千")
big_font = pygame.font.SysFont("Kaiti", 30)
small_font = pygame.font.SysFont("Kaiti", 15)


class Enemy:
    def __init__(self) -> None:
        self.x: float = randint(10, WIDTH - 10)
        self.y: float = randint(-80, -50)

        # more sides = more health
        # todo: make harder
        # todo: qian
        # if sides < 3 die
        self.sides = randint(3, 10)

        self.theta = 0

        self.darkest = pygame.Color(209, 42, 42)
        self.lightest = pygame.Color(248, 255, 156)

        self.rot_speed = randint(20, 200)
        self.speed = randint(20, 50)

    def draw(self, dt: float, screen: pygame.Surface):
        self.theta += self.rot_speed * dt
        self.theta %= 360

        self.y += dt * self.speed

        poly = self.draw_poly(self.sides)
        poly = pygame.transform.rotate(poly, self.theta)
        screen.blit(poly, poly.get_rect(center=(self.x, self.y)))

    def draw_poly(self, sides: int):
        surface = pygame.Surface((101, 101)).convert_alpha()
        surface.fill((0, 0, 0, 0))

        dtheta = 2 * pi / sides

        points = []

        for i in range(0, sides):
            theta = dtheta * i

            # why is it sin, cos ... i have no idea
            # 5 * sides -> 10 * 5 = 50
            x = 50 + (5 * sides) * sin(theta + pi)
            y = 50 + (5 * sides) * cos(theta + pi)

            points.append((x, y))

        pygame.draw.polygon(
            surface, self.darkest.lerp(self.lightest, sides / 10), points
        )

        text = (big_font if sides >= 5 else small_font).render(
            names[sides], True, (0, 0, 0)
        )
        offset = 15 if sides >= 5 else 8
        surface.blit(text, (50 - offset, 50 - offset))

        return surface
