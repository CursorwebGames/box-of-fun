import math
import pygame

from bullet import Bullet

from config import WIDTH, HEIGHT, PLAYER_SPEED, RELOAD, HURT_TICK


font = pygame.font.SysFont("Kaiti", 30)


class Player:
    def __init__(self) -> None:
        self.score = 0
        self.lives = 10
        self.t = 0
        self.reload = 0
        self.hurt_tick = 0

    def get_pos(self):
        # easy mode
        return (
            WIDTH / 2 + (WIDTH / 2 - 50) * math.cos(PLAYER_SPEED * self.t / 2),
            HEIGHT / 2 + 50 * math.sin(PLAYER_SPEED * self.t),
        )
        # return (
        #     WIDTH / 2 + (WIDTH / 2 - 50) * math.sin(PLAYER_SPEED * 2 * self.t),
        #     HEIGHT / 2 + 100 * math.sin(PLAYER_SPEED * 3 * self.t),
        # )

    def shoot(self, bullets: list[Bullet]):
        if self.reload > 0:
            return

        self.reload = RELOAD

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
        if self.reload > 0:
            self.reload -= dt

        if self.hurt_tick > 0:
            self.hurt_tick -= dt

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

        if self.hurt_tick > 0:
            pygame.draw.circle(surface, (219, 20, 20), (50, 50), 25)

        text = font.render("伤" if self.hurt_tick > 0 else "兵", True, (0, 0, 0))
        text = pygame.transform.rotate(text, -90)
        surface.blit(text, (50 - 15, 50 - 15))

        return surface

    def hurt(self):
        self.hurt_tick = HURT_TICK
        self.lives -= 1
