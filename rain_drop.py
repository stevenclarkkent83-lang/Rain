import pygame
import random
from pygame.sprite import Sprite
from settings import Settings

class RainDrop(Sprite):

    def __init__(self, rd):
        super().__init__()
        self.settings = Settings()
        self.screen = rd.screen
        self.image = pygame.image.load("images/drop_image.xcf")
        self.rect = self.image.get_rect()
        self.screen_rect = rd.screen.get_rect()



    def update(self):
        self.rect.y += self.settings.rain_fall_speed
        self.blitme()


    def blitme(self):
        self.screen.blit(self.image, self.rect)