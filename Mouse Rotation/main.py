import pygame, math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

PLAYER_STARTING_X = SCREEN_WIDTH / 2
PLAYER_STARTING_Y = SCREEN_HEIGHT / 2

pygame.init()
screen = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()
running = True
dt = 0

class Player:
    MOVEMENT_SPEED = 200
    ROTATION_SPEED = 1
    
    def __init__(self):
        self.points = [
            (PLAYER_STARTING_X, PLAYER_STARTING_Y), 
            (PLAYER_STARTING_X-30, PLAYER_STARTING_Y-30),
            (PLAYER_STARTING_X+30, PLAYER_STARTING_Y-30)
        ]
    
    def move(self, axis, speed, dt):
        for i in range(len(self.points)):
            px, py = self.points[i]
            if axis == 0:
                px += speed * dt
            elif axis == 1:
                py += speed * dt
            self.points[i] = (px, py)

    def rotate(self, mouse, dt):

        # Calculating the angle
        ox, oy = self.points[0] # origin
        mx, my = mouse

        angle = math.atan((my - oy)/(mx - ox))
        print(f"{(mx - ox)=} {(my - oy)=} {(my - oy)/(mx - ox)=} {(angle)=}")
        
        for i in range(1, len(self.points)): # without origin point
            px, py = self.points[i]

            new_px = (px - ox) * math.cos(angle) - (py - oy) * math.sin(angle) + ox
            new_py = (py - oy) * math.cos(angle) + (px - ox) * math.sin(angle) + oy

            self.points[i] = (new_px, new_py)

    def update(self, dt):
        pass

    def draw(self):
        # for point in self.points:
        #     pygame.draw.circle(screen, WHITE, point, 5)
        pygame.draw.polygon(screen, WHITE, self.points)
        pygame.draw.circle(screen, RED, self.points[0], 10)

player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # One pressed event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                player.rotate(pygame.mouse.get_pos(), 0)

    keys = pygame.key.get_pressed()

    # Holding pressed event
    if keys[pygame.K_w]:
        player.move(1, -Player.MOVEMENT_SPEED, dt)
    if keys[pygame.K_s]:
        player.move(1, Player.MOVEMENT_SPEED, dt)
    if keys[pygame.K_a]:
        player.move(0, -Player.MOVEMENT_SPEED, dt)
    if keys[pygame.K_d]:
        player.move(0, Player.MOVEMENT_SPEED, dt)

    screen.fill(BLACK)

    player.update(dt)
    player.draw()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()