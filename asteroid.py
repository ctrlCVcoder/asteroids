from circleshape import CircleShape
from constants import *
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    def draw(self, screen):
        draw_pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", draw_pos, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Split the asteroid into two smaller asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            log_event("asteroid_split")
            rand_angle1 = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(rand_angle1)
            velocity2 = self.velocity.rotate(-rand_angle1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2
            return [asteroid1, asteroid2]
