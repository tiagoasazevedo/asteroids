import pygame   # this allows us to use code from the open-source pygame library throughout this file

from circleshape import * # import all classes and functions from the circleshape module
from constants import *  # import all constants from the constants module

# Player class
class Player (CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS) # Use the PLAYER_RADIUS constant
        self.rotation = 0
    
    def triangle(self): # Returns the vertices of the triangle representing the player
        # Calculate the vertices of the triangle based on the player's position and rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # Forward direction based on rotation
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # Right direction perpendicular to forward
        a = self.position + forward * self.radius # Forward vertex
        b = self.position - forward * self.radius - right # Backward vertex
        c = self.position - forward * self.radius + right # Right vertex
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)  # Draw the player as a triangle on the screen

    def rotate(self, dt): # Rotate the player based on the time delta
        self.rotation += PLAYER_TURN_SPEED * dt  # Use the PLAYER_TURN_SPEED constant
