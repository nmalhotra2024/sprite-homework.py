import pygame
import sys

# Initialize pygame
pygame.init()

# --- Screen setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = (30, 30, 30)  # dark background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Rectangles Game")

# --- Sprite settings ---
# Controlled player
player_color = (0, 255, 0)
player_size = (60, 60)
player_speed = 5
player_rect = pygame.Rect(100, 100, *player_size)

# Static rectangle
enemy_color = (255, 0, 0)
enemy_size = (80, 80)
enemy_rect = pygame.Rect(400, 250, *enemy_size)

# --- Game loop ---
clock = pygame.time.Clock()

running = True
while running:
    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Player movement ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # Keep player within screen bounds
    player_rect.x = max(0, min(player_rect.x, SCREEN_WIDTH - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, SCREEN_HEIGHT - player_rect.height))

    # --- Drawing ---
    screen.fill(SCREEN_COLOR)
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, enemy_color, enemy_rect)
    pygame.display.flip()

    # --- FPS ---
    clock.tick(60)

# --- Quit pygame ---
pygame.quit()
sys.exit()
