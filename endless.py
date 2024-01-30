import pygame
import sys
import random
from datetime import datetime, timedelta
from highscore import record_score

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size * 2]
player_speed = 5

# Enemies
enemy_size = 50
enemy_speed = 3
enemies = []

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw the player
def draw_player(pos):
    pygame.draw.rect(screen, WHITE, (pos[0], pos[1], player_size, player_size))

# Function to draw an enemy
def draw_enemy(pos):
    # cleprint(f'x={pos.x}, y={pos.y}, color={pos.color}')
    pygame.draw.rect(screen, pos.color, (pos.x, pos.y, enemy_size, enemy_size))

class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice([RED, GREEN, BLUE])

start = datetime.now()
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
    if player_pos[0] < 0:
        player_pos[0] = 0
    if player_pos[0] + player_size > WIDTH:
        player_pos[0] = WIDTH - player_size

    # Spawn enemies
    if random.randint(0, 100) < 5:
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemy_y = -enemy_size
        enemies.append(Enemy(enemy_x, enemy_y))

    # Update enemy positions
    for enemy in enemies:
        enemy.y += enemy_speed

    # Remove enemies that are off the screen
    enemies = [enemy for enemy in enemies if enemy.y < HEIGHT]

    # Check for collisions with enemies
    for enemy in enemies:
        if (
            player_pos[0] < enemy.x + enemy_size
            and player_pos[0] + player_size > enemy.x
            and player_pos[1] < enemy.y + enemy_size
            and player_pos[1] + player_size > enemy.y
        ):
            end = datetime.now()
            print("Game Over!")
            score = (end-start).total_seconds()
            print(f"You survived for {score} seconds!")
            record_score(score)
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    draw_player(player_pos)

    # Draw the enemies
    for enemy in enemies:
        draw_enemy(enemy)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)
