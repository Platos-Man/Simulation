import sys
from random import choice, randint
from pygame.math import Vector2

import pygame


class Snake:
    def __init__(self):
        self.body = [Vector2(20, 15), Vector2(20, 16), Vector2(20, 17), Vector2(19, 17)]
        self.directon = Vector2(0, 0)

        self.head_up = pygame.image.load("sprites/snake_head.png")

        self.tail_up = pygame.image.load("sprites/snake_tail.png")
        self.tail_down = pygame.transform.rotate(self.tail_up, 180)
        self.tail_left = pygame.transform.rotate(self.tail_up, 90)
        self.tail_right = pygame.transform.rotate(self.tail_up, -90)

        self.body_vertical = pygame.image.load("sprites/snake_body.png")

        self.body_tl = pygame.image.load("sprites/snake_body_turn.png")

    def draw_snake(self):
        for idx, block in enumerate(self.body):
            block_rect = pygame.Rect(block.x * grid_size, block.y * grid_size, grid_size, grid_size)
            if idx == 0:
                screen.blit(self.head_up, block_rect)
            # placeholder for logic
            elif idx == 1:
                screen.blit(self.body_vertical, block_rect)
            elif idx == 2:
                screen.blit(self.body_tl, block_rect)
            elif idx == 3:
                screen.blit(self.tail_right, block_rect)


class Main:
    def __init__(self):
        self.screen_w = grid_size * cells_in_row
        self.screen_h = grid_size * cells_in_col

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
        for x in range(0, self.screen_w, grid_size):
            for y in range(0, self.screen_h, grid_size):
                grid_block = pygame.Rect(x, y, grid_size, grid_size)
                pygame.draw.rect(screen, (150, 150, 150), grid_block, 1)

    def draw_elements(self):
        self.draw_grid()
        self.snake.draw_snake()

    def update(self):
        pass


pygame.init()

grid_size = 20
cells_in_row = 40  # X
cells_in_col = 30  # Y

main = Main()
screen = pygame.display.set_mode((main.screen_w, main.screen_h))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main.run()
