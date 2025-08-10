import pygame  # import the pygame module for game development
import random  # import the random module for generating random numbers

from circleshape import CircleShape
from constants import *  # import all constants from the constants module

class Asteroid(CircleShape): # Inherit from CircleShape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen): # Override draw method
        super().draw(screen) # Call the parent class's draw method
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2) # Draw a white asteroid outline using its position and radius and a width of 2

    def update(self, dt): # Override update method
        self.position.x += self.velocity.x * dt  # Update x position based on velocity
        self.position.y += self.velocity.y * dt  # Update y position based on velocity

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new velocities, rotated in opposite directions and faster
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2

        # Create two new asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1
        a1.add(*self.containers)

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2
        a2.add(*self.containers)

        self.kill()  # Remove the original asteroid
