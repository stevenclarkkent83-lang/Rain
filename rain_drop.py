import pygame
from pygame.sprite import Sprite

class RainDrop(Sprite):

    def __init__(self, rd):
        super().__init__()
        self.settings = rd.settings
        self.screen = rd.screen
        self.image = pygame.image.load("images/drop_image.xcf")
        self.rect = self.image.get_rect()
        self.screen_rect = rd.screen.get_rect()
        self.y_val = 0



    def update(self):
        self.rect.y += self.settings.rain_fall_speed * self.y_val


    def blitme(self):
        self.screen.blit(self.image, self.rect)