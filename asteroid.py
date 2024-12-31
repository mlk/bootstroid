from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        direction = random.uniform(20, 50)
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = self.velocity.rotate(direction)
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = self.velocity.rotate(-direction)