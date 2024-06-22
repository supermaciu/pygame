from pygame import Vector2

class Particle:
    FRICTION_COEFFICIENT = 0.2

    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.v = Vector2(0.0, 0.0)
        self.a = Vector2(0.0, 0.0)

        self.m = 1.0
        self.f = Vector2(0.0, 0.0)

    def update(self, dt):
        self.v.x += self.a.x * dt
        self.v.y += self.a.y * dt

        self.pos.x += self.v.x * dt
        self.pos.y += self.v.y * dt
