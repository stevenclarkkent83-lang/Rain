import pygame

class Rain:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.get_rect()
        pygame.display.set_caption("RainDrops")
        self.raining = True

    def running(self):

        while self.raining:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()






if __name__ == "__main__":
    rd = Rain()
    rd.running()
