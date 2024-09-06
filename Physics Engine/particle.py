from pygame import Vector2

class Particle:
    FRICTION_COEFFICIENT = 0.5
    DYNAMIC_FRICTION_THRESHOLD = 0.01

    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.acceleration = Vector2(0.0, 0.0)

        self.mass = 1.0
        self.force = Vector2(0.0, 0.0)

    def update(self, dt):
        friction_force = Vector2(
            -1 * self.force.x * Particle.FRICTION_COEFFICIENT,
            -1 * self.force.y * Particle.FRICTION_COEFFICIENT
        )

        if self.acceleration.x < Particle.DYNAMIC_FRICTION_THRESHOLD or self.acceleration.y < Particle.DYNAMIC_FRICTION_THRESHOLD:
            self.acceleration.x = 0.0
            self.acceleration.y = 0.0
        
        if self.force.x < 0.01 or self.force.y < 0.01:
            self.force = friction_force


        print(f"{self.velocity=}")
        print(f"{self.acceleration=}")
        print(f"{self.force=}")
        print()

        self.force.x += friction_force.x
        self.force.y += friction_force.y

        self.acceleration.x = self.force.x / self.mass
        self.acceleration.y = self.force.y / self.mass

        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt

        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
