import pygame

pygame.init()

class MainRun():
    def __init__(self, dw, dh):
        self.dw = dw
        self.dh = dh
        self.main()

    def main(self):
        window = pygame.display.set_mode((self.dw, self.dh))
        window_clock = pygame.time.Clock()
        while True:
            window.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            window_clock.tick(60)

    # def grid(self):
    #     grid_size = 20
    #     for x in range(0)


if __name__ == "__main__":
    MainRun(800,600)