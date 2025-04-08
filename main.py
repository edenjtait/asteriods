import pygame as pyg
from constants import *

screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pyg.time.Clock()
dt = 0

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while(True):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return

        screen.fill("black")
        pyg.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
