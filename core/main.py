import sys
from random import choice, randint

import pygame

pygame.init()


class MainRun:
    def __init__(self, dw, dh):
        self.dw = dw  # Display width
        self.dh = dh  # Display height
        self.window = pygame.display.set_mode((self.dw, self.dh))
        self.grid_size = 50
        self.main()

    def main(self):
        window_clock = pygame.time.Clock()
        entity = Entity(self.dw, self.dh, self.grid_size)
        while True:
            self.window.fill((220, 220, 220))
            self.draw_grid()

            entity.draw_entity(self.window)
            entity.move_entity()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            window_clock.tick(2)

    def draw_grid(self):
        for x in range(0, self.dw, self.grid_size):
            for y in range(0, self.dh, self.grid_size):
                grid_block = pygame.Rect(x, y, self.grid_size, self.grid_size)
                pygame.draw.rect(self.window, (150, 150, 150), grid_block, 1)


class Entity:
    def __init__(self, dw, dh, grid_size):
        self.color = (200, 0, 0)
        self.grid_size = grid_size
        self.screen_xend = (dw - self.grid_size) // self.grid_size
        self.screen_yend = (dh - self.grid_size) // self.grid_size
        self.xpos = randint(0, self.screen_xend)
        self.ypos = randint(0, self.screen_yend)
        # self.direction = choice([0, 1, 2, 3])  # 0: north, 1: west, 2: south, 3: east
        self.direction = randint(0, 4)

    def draw_entity(self, window):
        body = pygame.Rect(
            self.xpos * self.grid_size,
            self.ypos * self.grid_size,
            self.grid_size,
            self.grid_size,
        )
        pygame.draw.rect(window, self.color, body)
        centerx = self.xpos * self.grid_size + self.grid_size / 2
        centery = self.ypos * self.grid_size + self.grid_size / 2
        pygame.draw.circle(window, (0, 0, 0), (centerx, centery), self.grid_size // 5)

    def move_entity(self):
        state = choice([0, 1, 1, 1])
        if state:
            if self.direction == 0:
                self.ypos += -1
            elif self.direction == 1:
                self.xpos += 1
            elif self.direction == 2:
                self.ypos += 1
            elif self.direction == 3:
                self.xpos += -1
        else:
            self.direction += choice([-1, 1])
            if self.direction < 0:
                self.direction = 3
            if self.direction > 3:
                self.direction = 0

        if self.xpos < 0:
            self.xpos = self.screen_xend
        if self.xpos > self.screen_xend:
            self.xpos = 0
        if self.ypos < 0:
            self.ypos = self.screen_yend
        if self.ypos > self.screen_yend:
            self.ypos = 0


if __name__ == "__main__":
    MainRun(800, 600)
