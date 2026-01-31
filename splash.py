import pygame
import random

class Splash(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.life = 8  # frames
        self.radius = random.randint(2, 4)

        self.image = pygame.Surface((24, 12), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.life -= 1
        if self.life <= 0:
            self.kill()
            return

        self.image.fill((0, 0, 0, 0))

        # expanding arc
        alpha = int(180 * (self.life / 8))
        color = (180, 180, 200, alpha)

        pygame.draw.arc(
            self.image,
            color,
            self.image.get_rect(),
            3.14,  # left
            6.28,  # right
            3
        )
