from constants import *
import pygame
from circleshape import CircleShape

class shot (CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS) #from constants modify size
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) #the method to draw the instance

    def update(self, dt):
        self.position += self.velocity * dt   #how its trajectory speed is calculated