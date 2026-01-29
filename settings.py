import pygame

class Settings:

    def __init__(self):

        #Rain Settings
        self.max_rain = 50
        self.rain_fall_speed = 3
        self.rain_drop_delay = 60

        #Sound Settings
        self.rain_sound = pygame.mixer.Sound("sounds/rain.ogg")
        self.rain_sound.set_volume(0.6)  # start lower, heavy rain is loud

