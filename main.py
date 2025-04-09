import pygame as pyg
from constants import *
from player import *

screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pyg.time.Clock()
dt = 0

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize the clock
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return

        # Update dt at the beginning of each iteration
        dt = clock.tick(60) / 1000

        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pyg.display.flip()

if __name__ == "__main__":
    main()
