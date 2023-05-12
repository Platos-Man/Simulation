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
        entity_manager = EntityManager(self.dw, self.dh, self.grid_size, self.window)
        entity_manager.create_entities(5)

        print(entity_manager.entity_list)
        while True:
            self.window.fill((220, 220, 220))
            self.draw_grid()
            entity_manager.draw_entities(self.window)
            entity_manager.move_entities()

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
    def __init__(self, dw, dh, grid_size, color):
        self.color = color
        self.grid_size = grid_size
        self.screen_xend = (dw - self.grid_size) // self.grid_size
        self.screen_yend = (dh - self.grid_size) // self.grid_size
        self.xpos = randint(0, self.screen_xend)
        self.ypos = randint(0, self.screen_yend)
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

        def draw_eyes(x1, x2, y1, y2):
            pygame.draw.circle(
                window, (0, 0, 0), (centerx + x1, centery + y1), self.grid_size // 10
            )
            pygame.draw.circle(
                window, (0, 0, 0), (centerx + x2, centery + y2), self.grid_size // 10
            )

        apart = self.grid_size // 5  # how far eyes are apart from eachother
        offcenter = self.grid_size // 3  # how far from center eyes are
        if self.direction == 0:
            draw_eyes(-apart, apart, -offcenter, -offcenter)
        elif self.direction == 1:
            draw_eyes(offcenter, offcenter, -apart, apart)
        elif self.direction == 2:
            draw_eyes(-apart, apart, offcenter, offcenter)
        elif self.direction == 3:
            draw_eyes(-offcenter, -offcenter, -apart, apart)

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
            elif self.direction > 3:
                self.direction = 0

        if self.xpos < 0:
            self.xpos = self.screen_xend
        elif self.xpos > self.screen_xend:
            self.xpos = 0
        elif self.ypos < 0:
            self.ypos = self.screen_yend
        elif self.ypos > self.screen_yend:
            self.ypos = 0


class EntityManager:
    def __init__(self, dw, dh, grid_size, window):
        self.dw = dw
        self.dh = dh
        self.grid_size = grid_size
        self.window = window
        self.entity_list = []

    def create_entities(self, amount):
        self.entity_list = [
            Entity(
                self.dw,
                self.dh,
                self.grid_size,
                (randint(50, 220), randint(50, 220), randint(50, 220)),
            )
            for _ in range(amount)
        ]

    def draw_entities(self, window):
        for entity in self.entity_list:
            entity.draw_entity(window)

    def move_entities(self):
        for entity in self.entity_list:
            entity.move_entity()


if __name__ == "__main__":
    MainRun(800, 600)
