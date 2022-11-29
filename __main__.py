from itertools import count
import pygame
from src.view import View
from src.world import World, upsample
from src.simulator import game_of_life
from src.pattern import get_patterns


WIDTH = 500
HEIGHT = 500
PIXEL_SIZE = 1
FPS = -1
N_PATTERNS = 500


def main():
    pygame.init()
    pygame.display.set_caption("Game of life")
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 12)
    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    patterns = get_patterns(n_patterns=N_PATTERNS, proba=[.1, .1, .8])
    world = World(int(HEIGHT/PIXEL_SIZE), int(WIDTH/PIXEL_SIZE))
    world.populate_world(patterns)
    simulator = game_of_life(world.array)
    view = View()

    terminate = False
    i = count(1)

    while not terminate:
        terminate = view.process_events()
        frame = upsample(next(simulator), PIXEL_SIZE).T * 255
        fps = font.render(
            f'frame {next(i)} | fps: {str(int(clock.get_fps()))}',
            1, pygame.Color("coral")
        )
        view.display_frame(screen, frame, fps)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
