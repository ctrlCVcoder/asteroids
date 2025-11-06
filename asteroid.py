from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    def draw(self, screen):
        draw_pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", draw_pos, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt