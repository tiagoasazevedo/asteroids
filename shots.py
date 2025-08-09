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

    def shoot(self): # Create a new shot and add it to the game
        shot = Shot(self.position.x, self.position.y) # Create a new shot at the player's position
        shot.velocity = self.velocity.rotate(self.rotation) # Set the shot's velocity based on the player's rotation
        return shot # Return the created shot
