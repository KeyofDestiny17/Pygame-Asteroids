import pygame
from circleshape import CircleShape
import constants
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_asteroid_angle = random.uniform(20, 50)
        getting_smaler = self.radius - constants.ASTEROID_MIN_RADIUS
        
        new_asteroid_one = Asteroid(self.position.x, self.position.y, getting_smaler)
        new_asteroid_one.velocity = (self.velocity * 1.2).rotate(new_asteroid_angle)
        
        new_asteroid_two = Asteroid(self.position.x, self.position.y, getting_smaler)
        new_asteroid_two.velocity = (self.velocity * 1.2).rotate(-new_asteroid_angle)
        