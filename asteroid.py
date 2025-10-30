import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        self.new_angle = random.uniform(20, 50)

        a = self.velocity.rotate(self.new_angle)
        b = self.velocity.rotate(-self.new_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # new_velocity = random.uniform(self) REFACTOR for different velocities LATER

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2

        


    

