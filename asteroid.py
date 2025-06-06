import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    random_angle = random.uniform(20, 50)
    new_roid_a = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
    new_roid_b = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

    new_roid_a.velocity = self.velocity.rotate(random_angle) * 1.2
    new_roid_b.velocity = self.velocity.rotate(-random_angle) * 1.2
