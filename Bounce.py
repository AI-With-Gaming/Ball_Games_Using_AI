import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GROWTH_RATE = 2
BALL_INITIAL_RADIUS = 5
CIRCLE_RADIUS = 150
SPEED_INCREASE = 0.5
GRAVITY = 0.5  # Gravity constant
ELASTICITY = 0.9  # Elasticity for bounce

# Colors
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Ball Simulation")

# Load background GIF frames
background_frames = []
for i in range(1, 6):  # Assuming the GIF has 5 frames, you can adjust this based on your GIF
    frame = pygame.image.load(f'hacker_background_frame{i}.png.gif')
    frame = pygame.transform.scale(frame, (WIDTH, HEIGHT))
    background_frames.append(frame)

# Ball class
class Ball:
    def __init__(self):
        self.radius = BALL_INITIAL_RADIUS
        self.color = random.choice(COLORS)
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)

    def move(self):
        # Apply gravity
        self.dy += GRAVITY

        self.x += self.dx
        self.y += self.dy

        # Bounce off the bottom of the window
        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.dy = -abs(self.dy) * ELASTICITY
            self.dx *= ELASTICITY

        # Bounce off the boundary of the middle circle
        dist = math.hypot(self.x - WIDTH // 2, self.y - HEIGHT // 2)
        if dist + self.radius > CIRCLE_RADIUS:
            angle = math.atan2(self.y - HEIGHT // 2, self.x - WIDTH // 2)
            speed = math.sqrt(self.dx ** 2 + self.dy ** 2) + SPEED_INCREASE
            self.dx = -math.cos(angle) * speed + random.uniform(-0.5, 0.5)
            self.dy = -math.sin(angle) * speed + random.uniform(-0.5, 0.5)
            self.color = random.choice(COLORS)
            self.radius += GROWTH_RATE

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))

# Main game loop
def main():
    clock = pygame.time.Clock()
    ball = Ball()
    trail = []
    game_over = False
    frame_index = 0
    game_over_counter = 0
    alpha = 0
    fade_speed = 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            ball.move()

            # Check if the ball completely fills the circle
            if ball.radius >= CIRCLE_RADIUS:
                game_over = True

        # Draw the background with smooth transition
        next_frame_index = (frame_index + 1) % len(background_frames)
        screen.blit(background_frames[frame_index], (0, 0))
        next_frame = background_frames[next_frame_index].copy()
        next_frame.set_alpha(alpha)
        screen.blit(next_frame, (0, 0))

        # Update alpha for fade effect
        alpha += fade_speed
        if alpha >= 255:
            alpha = 0
            frame_index = next_frame_index

        # Draw the outer circle
        pygame.draw.circle(screen, (255, 255, 255), (WIDTH // 2, HEIGHT // 2), CIRCLE_RADIUS, 1)

        if game_over:
            font = pygame.font.SysFont(None, 74)
            game_over_counter += 1
            scale_factor = 1 + 0.05 * math.sin(game_over_counter * 0.1)  # Sinusoidal scaling for animation
            text = font.render("Game Over", True, (255, 255, 255))
            text = pygame.transform.scale(text, (int(text.get_width() * scale_factor), int(text.get_height() * scale_factor)))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        else:
            # Draw the ball and its trail
            trail.append((ball.x, ball.y, ball.color, ball.radius))
            if len(trail) > 50:
                trail.pop(0)

            for position in trail:
                pygame.draw.circle(screen, position[2], (int(position[0]), int(position[1])), int(position[3] / 2))

            ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
