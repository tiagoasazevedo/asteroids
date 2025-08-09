import pygame  # import the pygame module for game development

from circleshape import CircleShape

class Asteroid(CircleShape): # Inherit from CircleShape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen): # Override draw method
        super().draw(screen) # Call the parent class's draw method
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2) # Draw a white asteroid outline using its position and radius and a width of 2

    def update(self, dt): # Override update method
        self.position.x += self.velocity.x * dt  # Update x position based on velocity
        self.position.y += self.velocity.y * dt  # Update y position based on velocity