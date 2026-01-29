import pygame

import random

from rain_drop import RainDrop
from settings import Settings

class Rain:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.drops = pygame.sprite.Group()
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("RainDrops")
        self.raining = True
        self.clock = pygame.time.Clock()
        self.last_drop = pygame.time.get_ticks()
        self.rain_sound = pygame.mixer.Sound("sounds/rain.ogg")
        self.rain_sound.set_volume(0.4)  # start lower, heavy rain is loud
        self.rain_sound.play(loops=-1)

    def running(self):
        while self.raining:
            self.clock.tick(60)
            self._check_events()
            self.hits_bottom()
            self.create_storm()
            self._update_screen()


    def _update_screen(self):
        self.screen.fill("black")
        self.drops.draw(self.screen)
        self.drops.update()
        pygame.display.flip()

    def create_storm(self):
        now = pygame.time.get_ticks()
        if self.settings.max_rain > len(self.drops):
            if now - self.last_drop >= self.settings.rain_drop_delay:
                a_drop = RainDrop(self)
                a_drop.rect.x = random.randint(
                    0, self.screen_rect.width - a_drop.rect.width)
                self.drops.add(a_drop)
                self.last_drop = now

    def hits_bottom(self):
        for drop in self.drops.sprites():
            if drop.rect.bottom >= self.screen_rect.height:
                drop.kill()
                #self.drops.remove(drop)

    def _check_events(self):
        """Checking for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self._key_down(event)

    def _key_down(self, event):
        """Key down event"""
        if event.key == pygame.K_q:
            self.raining = False

    def _key_up(self, event):
        pass


if __name__ == "__main__":
    rd = Rain()
    rd.running()
