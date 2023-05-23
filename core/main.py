import sys
from random import choice, randint

import pygame


class Snake:
    def __init__(self):
        pass


class Main:
    def __init__(self):
        self.grid_size = 20
        self.cells_in_row = 40
        self.cells_in_col = 30
        self.screen_w = self.grid_size * self.cells_in_row
        self.screen_h = self.grid_size * self.cells_in_col

        self.snake = Snake()

    def run(self):
        while True:
            screen.fill((220, 220, 220))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    main.update()
            main.draw_elements()
            pygame.display.update()
            clock.tick(60)

    def draw_grid(self):
        for x in range(0, self.screen_w, self.grid_size):
            for y in range(0, self.screen_h, self.grid_size):
                grid_block = pygame.Rect(x, y, self.grid_size, self.grid_size)
                pygame.draw.rect(screen, (150, 150, 150), grid_block, 1)

    def draw_elements(self):
        self.draw_grid()

    def update(self):
        pass


pygame.init()

main = Main()
screen = pygame.display.set_mode((main.screen_w, main.screen_h))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main.run()
