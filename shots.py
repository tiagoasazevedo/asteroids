import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS

# Class for player shots
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, -300)  # shots move upwards

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.y < 0:
            self.kill()  # remove shot if it goes off screen

    def draw(self, screen): # Draw the shot on the screen
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)