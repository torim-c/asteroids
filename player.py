import pygame
from circleshape import CircleShape
from constants import *
from shot import *


class Player(CircleShape): #for hitboxes
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    def triangle(self): #draw a triangle - used for player model // hitbox is still a circle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): #draws player
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate (self, dt): #rotates player
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt): #updates player actions on key press
        self.shoot_cooldown -= dt
#        if self.shoot_cooldown < 0: FOR REFACTORING A CLAMP LATER
#            self.shoot_cooldown = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: #turn left
            self.rotate(-dt)

        if keys[pygame.K_d]: #turn right #adding minus infront of -dt inverses the result becuase dt is passed as negative
            self.rotate(dt)
        
        if keys[pygame.K_w]: #go forwards
            self.move(dt)

        if keys[pygame.K_s]: #go backwards
            self.move(-dt * 0.75)

        if keys[pygame.K_SPACE]:
            self.shoot()


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        bullet = shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED   #very cool circular pattern in a snail like fashio when constant
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN