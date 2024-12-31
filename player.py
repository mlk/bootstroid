from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame

class Player(CircleShape):
    rotation = 0
    shoot_cooldown = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle())

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt
        if keys[pygame.K_a]:
            self.rotateLeft(dt)
        if keys[pygame.K_d]:
            self.rotateRight(dt)
        if keys[pygame.K_w]:
            self.moveForward(dt)
        if keys[pygame.K_s]:
            self.moveBackwards(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotateLeft(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
        #self.rotation %= 360

    def rotateRight(self, dt):
        self.rotation += -dt * PLAYER_TURN_SPEED
        #self.rotation %= 360

    def moveForward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def moveBackwards(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = forward * SHOT_SPEED