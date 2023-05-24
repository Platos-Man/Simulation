import sys
from random import choice, randint

import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [
            Vector2(20, 15),
            Vector2(20, 16),
            Vector2(20, 17),
            Vector2(19, 17),
            Vector2(18, 17),
            Vector2(17, 17),
            Vector2(16, 17),
            Vector2(15, 17),
            Vector2(14, 17),
        ]
        self.direction = Vector2(0, -1)
        self.new_block = False

        self.head_up = pygame.image.load("sprites/snake_head.png")
        self.head_down = pygame.transform.rotate(self.head_up, 180)
        self.head_left = pygame.transform.rotate(self.head_up, 90)
        self.head_right = pygame.transform.rotate(self.head_up, -90)

        self.tail_up = pygame.image.load("sprites/snake_tail.png")
        self.tail_down = pygame.transform.rotate(self.tail_up, 180)
        self.tail_left = pygame.transform.rotate(self.tail_up, 90)
        self.tail_right = pygame.transform.rotate(self.tail_up, -90)

        self.body_vertical = pygame.image.load("sprites/snake_body.png")
        self.body_horizontal = pygame.transform.rotate(self.body_vertical, 90)

        self.body_tl = pygame.image.load("sprites/snake_body_turn.png")
        self.body_tr = pygame.transform.flip(self.body_tl, True, False)
        self.body_bl = pygame.transform.flip(self.body_tl, False, True)
        self.body_br = pygame.transform.rotate(self.body_tl, 180)

    def draw_snake(self):
        for idx, block in enumerate(self.body):
            block_rect = pygame.Rect(block.x * grid_size, block.y * grid_size, grid_size, grid_size)
            if idx == 0:
                self.update_head_graphics()
                screen.blit(self.head, block_rect)
            elif idx == len(self.body) - 1:
                self.update_tail_graphics()
                screen.blit(self.tail, block_rect)
            else:
                self.update_body_graphics(idx)
                screen.blit(self.body_block, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[0] - self.body[1]
        if head_relation == Vector2(-1, 0):  # left
            self.head = self.head_left
        elif head_relation == Vector2(1, 0):  # right
            self.head = self.head_right
        elif head_relation == Vector2(0, -1):  # up
            self.head = self.head_up
        elif head_relation == Vector2(0, 1):  # down
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(-1, 0):  # left
            self.tail = self.tail_left
        elif tail_relation == Vector2(1, 0):  # right
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, -1):  # up
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, 1):  # down
            self.tail = self.tail_down

    def update_body_graphics(self, i):
        following = self.body[i + 1] - self.body[i]
        previous = self.body[i - 1] - self.body[i]
        if following.y == previous.y:
            self.body_block = self.body_horizontal
        elif following.x == previous.x:
            self.body_block = self.body_vertical
        else:
            if previous.x == -1 and following.y == -1 or previous.y == -1 and following.x == -1:
                self.body_block = self.body_tl
            elif previous.x == 1 and following.y == -1 or previous.y == -1 and following.x == 1:
                self.body_block = self.body_tr
            elif previous.x == -1 and following.y == 1 or previous.y == 1 and following.x == -1:
                self.body_block = self.body_bl
            elif previous.x == 1 and following.y == 1 or previous.y == 1 and following.x == 1:
                self.body_block = self.body_br

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
        else:
            body_copy = self.body[:-1]
        self.new_block = False
        next_block = body_copy[0] + self.direction
        if next_block.x > cells_in_row - 1:
            next_block.x = 0
        elif next_block.x < 0:
            next_block.x = cells_in_row - 1
        if next_block.y > cells_in_col - 1:
            next_block.y = 0
        elif next_block.y < 0:
            next_block.y = cells_in_col - 1
        body_copy.insert(0, next_block)
        self.body = body_copy[:]

    def grow_snake(self):
        self.new_block = True


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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0, -1)
                    elif event.key == pygame.K_RIGHT:
                        if self.snake.direction.x != -1:
                            self.snake.direction = Vector2(1, 0)
                    elif event.key == pygame.K_DOWN:
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0, 1)
                    elif event.key == pygame.K_LEFT:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1, 0)
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
        self.snake.move_snake()


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
