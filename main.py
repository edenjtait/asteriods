import pygame as pyg
from constants import *

class CircleShape(pyg.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self, containers)
        else:
            super().__init__()

        self.position = pyg.Vector2(x, y)
        self.velocity - pyg.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

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
