import random
import sys

import pygame

pygame.init()


class MainRun:
    def __init__(self, dw, dh):
        self.dw = dw  # Display width
        self.dh = dh  # Display height
        self.window = pygame.display.set_mode((self.dw, self.dh))
        self.grid_size = 20
        self.main()

    def main(self):
        window_clock = pygame.time.Clock()
        while True:
            self.window.fill((220, 220, 220))
            self.draw_grid()
            entity = Entity()
            entity.draw_entity(self.window, self.grid_size)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            window_clock.tick(60)

    def draw_grid(self):
        for x in range(0, self.dw, self.grid_size):
            for y in range(0, self.dh, self.grid_size):
                grid_block = pygame.Rect(x, y, self.grid_size, self.grid_size)
                pygame.draw.rect(self.window, (150, 150, 150), grid_block, 1)


class Entity:
    def __init__(self):
        self.color = (200, 0, 0)
        self.xpos = 0
        self.ypos = 0

    def draw_entity(self, window, grid_size):
        body = pygame.Rect(self.xpos, self.ypos, grid_size, grid_size)
        pygame.draw.rect(window, self.color, body)


if __name__ == "__main__":
    MainRun(800, 600)
