import pygame
import sys
import random
from datetime import datetime, timedelta
from highscore import record_score, check_score

# Initialize Pygame
pygame.init()

# Fonts
font = pygame.font.Font(None, 36)

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
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


def get_initials():
    initials = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(initials) > 0:
                    return initials
                elif event.key == pygame.K_BACKSPACE:
                    initials = initials[:-1]
                elif event.key <= 127:
                    if len(initials) < 3:  # Limit initials to 3 characters
                        initials += event.unicode.upper()

        screen.fill(BLACK)
        draw_text("Enter Initials: " + initials, font, WHITE, screen, 20, 20)
        pygame.display.update()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice([RED, GREEN, BLUE])


# Main game loop

def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text('Main Menu', font, WHITE, screen, 20, 20)

        draw_text('Press Enter to start or Q to quit.', font, WHITE, screen, 20, 100)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


def game_loop():
    running = True
    score = 0
    start = datetime.now()
    enemies = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
                running = False

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

    if check_score(score):
        initials = get_initials()
        record_score(initials, score)


main_menu()
