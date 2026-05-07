import pygame
from circleshape import CircleShape
import constants
from shot import Shot
import sys
from scoring_system import ScoringSystem

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.lives = constants.STARTING_LIVES
        self.visible = True
        self.respawn_timer = 0
        
        # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        if self.visible:
            pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
        return self.rotation
    
    def update(self, dt):
        if self.respawn_timer > 0:
            self.respawn_timer -= dt
            if self.respawn_timer <= 0:
                self.visible = True
            return
        
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shot_cooldown_timer -= dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        self.shot_cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOT_SPEED

    def respawn(self, x, y): # With the help of Boots the ai from Boot.Dev
        self.lives -= 1
        
        if self.lives <= 0:
            print("GAME OVER")
            ScoringSystem.print_score()
            sys.exit()
        self.visible = False
        self.respawn_timer = constants.RESPAWN_TIMER_SECONDS
        print(f"You've been hit! Respawning... Lives remaining: {self.lives}")
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0