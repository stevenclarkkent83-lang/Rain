import pygame

import random

from rain_drop import RainDrop
from splash import Splash
from splash_drop import SplashDrop
from settings import Settings


class Rain:

    def __init__(self):
        pygame.mixer.pre_init(
            frequency=44100,
            size=-16,
            channels=2,
            buffer=1024  # try 1024, 2048, or 4096
        )
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("RainDrops")

        #Sprite Groups
        self.drops = pygame.sprite.Group()
        self.splashes = pygame.sprite.Group()
        self.splash_drops = pygame.sprite.Group()

        self.screen_rect = self.screen.get_rect()
        self.settings.rain_sound.play(loops=-1)

        self.last_drop = pygame.time.get_ticks()
        self.clock = pygame.time.Clock()
        self.raining = True


    def running(self):

        while self.raining:
            self.clock.tick(60)
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill("black")
        self.hits_bottom()
        self.create_storm()
        self.drops.draw(self.screen)
        self.drops.update()
        self.splash_drops.update()
        self.splash_drops.draw(self.screen)
        self.splashes.update()
        self.splashes.draw(self.screen)
        pygame.display.flip()

    def create_storm(self):
        now = pygame.time.get_ticks()
        if self.settings.max_rain > len(self.drops):
            if now - self.last_drop >= self.settings.rain_drop_delay:
                a_drop = RainDrop(self)
                a_drop.rect.x = random.randint(
                    0, self.screen_rect.width - a_drop.rect.width)
                a_drop.y_val = random.randint(1, 3)
                self.drops.add(a_drop) # type: ignore[arg-type]
                self.last_drop = now

    def hits_bottom(self):
        for drop in self.drops.sprites():
            if drop.rect.bottom >= self.screen_rect.height:
                splash = Splash(drop.rect.centerx, self.screen_rect.bottom - 20)
                self.splashes.add(splash) # type: ignore[arg-type]

                for _ in range(2):
                    sd = SplashDrop(drop.rect.centerx, self.screen_rect.bottom - 20)
                    self.splash_drops.add(sd) # type: ignore[arg-type]
                drop.kill()

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
