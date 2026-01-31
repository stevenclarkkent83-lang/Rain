import pygame
import random

class SplashDrop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.radius = 8
        self.image = pygame.Surface((6, 6), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (190, 190, 210), (3, 3), self.radius)

        self.rect = self.image.get_rect(center=(x, y))

        # physics
        self.vel_x = random.uniform(-1.2, 1.2)
        self.vel_y = random.uniform(-4.0, -2.5)
        self.gravity = 0.35

        self.life = 18

    def update(self):
        self.vel_y += self.gravity
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        self.life -= 1
        if self.life <= 0:
            self.kill()
