import sys

import pygame

pygame.init()


class MainRun:
    def __init__(self, dw, dh):
        self.dw = dw  # Display width
        self.dh = dh  # Display height
        self.window = pygame.display.set_mode((self.dw, self.dh))
        self.main()

    def main(self):
        window_clock = pygame.time.Clock()
        while True:
            self.window.fill((220, 220, 220))
            self.draw_grid()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            window_clock.tick(60)

    def draw_grid(self):
        grid_size = 20
        for x in range(0, self.dw, grid_size):
            for y in range(0, self.dh, grid_size):
                grid_block = pygame.Rect(x, y, grid_size, grid_size)
                pygame.draw.rect(self.window, (150, 150, 150), grid_block, 1)


if __name__ == "__main__":
    MainRun(800, 600)
