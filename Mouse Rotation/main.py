import pygame, math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
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
    MOVEMENT_SPEED = 150
    BULLET_SPEED = 10
    
    def __init__(self):
        self.points = [
            (PLAYER_STARTING_X, PLAYER_STARTING_Y), 
            (PLAYER_STARTING_X-40, PLAYER_STARTING_Y+10),
            (PLAYER_STARTING_X-40, PLAYER_STARTING_Y-10)
        ]
        self.playerCentroid = Player.calculate_centroid(self.points)
        self.oldAngle = 0

        self.bullet = [
            (0, 0), 
            (-20, 5),
            (-20, -5)
        ]
        self.bulletCentroid = Player.calculate_centroid(self.bullet)
        self.bullets = list()

    @classmethod
    def calculate_centroid(cls, points):
        return (
            sum(list(point)[0] for point in points) / len(points),
            sum(list(point)[1] for point in points) / len(points),
        )
    
    def move(self, axis, speed, dt):
        for i in range(len(self.points)):
            px, py = self.points[i]
            if axis == 0:
                px += speed * dt
            elif axis == 1:
                py += speed * dt
            self.points[i] = (px, py)

        cx, cy = self.playerCentroid
        if axis == 0:
            cx += speed * dt
        elif axis == 1:
            cy += speed * dt
        self.playerCentroid = (cx, cy)

    def rotate(self, mouse):

        # Calculating the angle
        ox, oy = self.playerCentroid
        mx, my = mouse

        if (mx - ox) != 0:
            angle = math.atan((my - oy)/(mx - ox))
        else:
            angle = 0

        # Angle converted to full angle
        if (mx - ox) > 0 and (my - oy) > 0:
            pass
        elif (mx - ox) < 0 and (my - oy) > 0:
            angle += math.pi
        elif (mx - ox) < 0 and (my - oy) < 0:
            angle += math.pi
        elif (mx - ox) > 0 and (my - oy) < 0:
            angle += 2 * math.pi

        # Tangens angle excepitons
        if (mx - ox) > 0 and (my - oy) == 0:
            pass
        elif (mx - ox) == 0 and (my - oy) < 0:
            angle += math.pi * 3/2
        elif (mx - ox) < 0 and (my - oy) == 0:
            angle += math.pi
        elif (mx - ox) == 0 and (my - oy) > 0:
            angle += math.pi / 2

        temp = angle
        angle -= self.oldAngle # new angle - old angle = difference/delta
        self.oldAngle = temp
        
        for i in range(len(self.points)): # without origin point
            px, py = self.points[i]

            # normal coordinate system
            # new_px = (px - ox) * math.cos(angle) - (py - oy) * math.sin(angle) + ox
            # new_py = (py - oy) * math.cos(angle) + (px - ox) * math.sin(angle) + oy
            
            # x increasing from left to right and y increasing from top to bottom
            new_px = (px - ox) * math.cos(angle) - (py - oy) * math.sin(angle) + ox
            new_py = (px - ox) * math.sin(angle) + (py - oy) * math.cos(angle) + oy

            self.points[i] = (new_px, new_py)
        
    def fire(self, speed):
        # bullet = Bullet()

        # cx, cy = self.playerCentroid
        # bullet = self.bullet
        # bx, by = bullet
        # bullet = (bx + cx, by + cy)

        pass



    def update(self, dt):
        self.rotate(pygame.mouse.get_pos())

    def draw(self):
        # player
        pygame.draw.polygon(screen, WHITE, self.points)
        pygame.draw.circle(screen, GRAY, self.playerCentroid, 2)

        # bullets


player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # One pressed event keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                print("test")

        # One pressed event mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                # player.fire()
                pass

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

    dt = clock.tick(120) / 1000

pygame.quit()