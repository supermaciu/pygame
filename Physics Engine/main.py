import pygame

from particle import Particle

# Constants
BACKGROUND_COLOR = pygame.Color(100, 100, 100)
PARTICLE_COLOR = pygame.Color(230, 230, 230)

def main() -> None:
    pygame.init()

    info = pygame.display.Info()
    display_width = info.current_w
    display_height = info.current_h

    screen = pygame.display.set_mode((display_width * 0.75, display_height * 0.75))

    clock = pygame.time.Clock()
    running = True
    dt = 0

    # Setup
    particles = []
    
    for i in range(1):
        p = Particle(40, screen.get_height()/10*i+screen.get_height()/10/2)
        p.force.x = 1000
        particles.append(p)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Drawing
        for p in particles:
            pygame.draw.circle(screen, PARTICLE_COLOR, p.position, 10)

        # Updating
        for p in particles:
            p.update(dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()   


if __name__ == "__main__":
    main()