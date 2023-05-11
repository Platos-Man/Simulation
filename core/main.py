import pygame

pygame.init()

display_width = 800
display_height = 600
window = pygame.display.set_mode((display_width, display_height))

window_clock = pygame.time.Clock()

class MainRun():
    def __init__(self):
        self.main()

    def main(self):
        
        while True:
            window.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
            window_clock.tick(60)

    def grid(self):
        pass


if __name__ == "__main__":
    MainRun()