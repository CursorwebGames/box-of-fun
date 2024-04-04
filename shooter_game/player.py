import math
import pygame

from bullet import Bullet

from config import WIDTH, HEIGHT, PLAYER_SPEED


font = pygame.font.SysFont("Kaiti", 30)


class Player:
    def __init__(self) -> None:
        self.score = 0
        self.lives = 5
        self.t = 0

    def get_pos(self):
        return (
            WIDTH / 2 + (WIDTH / 2 - 50) * math.cos(PLAYER_SPEED * self.t / 2),
            HEIGHT - 100 + 50 * math.sin(PLAYER_SPEED * self.t),
        )

    def shoot(self, bullets: list[Bullet]):
        mx, my = pygame.mouse.get_pos()

        px, py = self.get_pos()

        x = px - mx
        y = -(py - my)
        # why is this negative?
        angle = -(math.atan2(y, x) + math.pi)

        bullets.append(
            Bullet(px + 50 * math.cos(angle), py + 50 * math.sin(angle), angle)
        )

    def draw(self, dt: float, screen: pygame.Surface):
        self.t += dt
        px, py = self.get_pos()
        os = self.draw_player()

        mx, my = pygame.mouse.get_pos()

        x = px - mx
        y = -(py - my)  # neg because pygame y incr down

        # i can't explain it but maybe 0 is at the left instead of right?
        angle = math.degrees(math.atan2(y, x)) + 180
        s = pygame.transform.rotate(os, angle)

        screen.blit(s, s.get_rect(center=(px, py)))

    def draw_player(self) -> pygame.Surface:
        surface = pygame.Surface((100, 100)).convert_alpha()
        surface.fill((0, 0, 0, 0))
        pygame.draw.polygon(surface, (191, 69, 69), [(60, 30), (90, 50), (60, 70)])
        pygame.draw.rect(surface, (204, 212, 144), (50, 50 - 5, 50, 10))
        pygame.draw.circle(surface, (211, 221, 232), (50, 50), 25)
        pygame.draw.circle(surface, (64, 130, 201), (50, 50), 10)

        text = font.render("兵", True, (0, 0, 0))
        text = pygame.transform.rotate(text, -90)
        surface.blit(text, (50 - 15, 50 - 15))

        return surface
