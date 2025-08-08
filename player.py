from circleshape import CircleShape
import pygame

# Player class
class Player (CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=pygame.constants.PLAYER_RADIUS) # Use the PLAYER_RADIUS constant
        rotation = 0  
    
    def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]