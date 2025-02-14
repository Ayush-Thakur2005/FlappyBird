import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird Clone')

# Game constants
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 60
PIPE_HEIGHT = 500
PIPE_GAP = 150
BIRD_WIDTH = 30
BIRD_HEIGHT = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load assets
bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_image.fill(BLUE)

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.vel = 0
    
    def update(self):
        # Apply gravity
        self.vel += GRAVITY
        self.y += self.vel
        
        # Prevent bird from falling off the screen
        if self.y > HEIGHT - BIRD_HEIGHT:
            self.y = HEIGHT - BIRD_HEIGHT
        if self.y < 0:
            self.y = 0
    
    def flap(self):
        self.vel = FLAP_STRENGTH
    
    def draw(self, screen):
        screen.blit(bird_image, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, HEIGHT - PIPE_GAP)
        self.top = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP)

    def update(self):
        self.x -= 5
        self.top.x = self.x
        self.bottom.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.top)
        pygame.draw.rect(screen, GREEN, self.bottom)
    
    def off_screen(self):
        return self.x < -PIPE_WIDTH

    def collide(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, BIRD_WIDTH, BIRD_HEIGHT)
        if bird_rect.colliderect(self.top) or bird_rect.colliderect(self.bottom):
            return True
        return False

# Main game loop
def game():
    bird = Bird()
    pipes = [Pipe()]
    clock = pygame.time.Clock()
    score = 0
    running = True
    game_over = False

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.flap()

        if not game_over:
            bird.update()

            # Update pipes
            for pipe in pipes:
                pipe.update()
                if pipe.off_screen():
                    pipes.remove(pipe)
                    pipes.append(Pipe())
                    score += 1

            # Check for collisions
            for pipe in pipes:
                if pipe.collide(bird):
                    game_over = True

            # Draw everything
            bird.draw(screen)
            for pipe in pipes:
                pipe.draw(screen)
            
            # Draw score
            font = pygame.font.SysFont("Arial", 24)
            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (10, 10))
        else:
            # Game Over screen
            font = pygame.font.SysFont("Arial", 36)
            game_over_text = font.render("GAME OVER", True, BLACK)
            screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 3))

            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (WIDTH // 4, HEIGHT // 2))

            restart_text = font.render("Press R to Restart", True, BLACK)
            screen.blit(restart_text, (WIDTH // 4, HEIGHT // 1.5))

            if pygame.key.get_pressed()[pygame.K_r]:
                game()
                return

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()
