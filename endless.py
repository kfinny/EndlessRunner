import pygame
import sys
import random
from datetime import datetime, timedelta
from highscore import record_score, check_score
from enemy import Enemy
from player import Player
from globals import *

# Initialize Pygame
pygame.init()

# Fonts
font = pygame.font.Font(None, 36)


# Player
player = Player(WIDTH // 2, HEIGHT - PLAYER_SIZE * 2)
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
def draw_player(pos: Player):
    pygame.draw.polygon(screen, player.color, player.points())


# Function to draw an enemy
def draw_enemy(pos: Enemy):
    # cleprint(f'x={pos.x}, y={pos.y}, color={pos.color}')
    pygame.draw.rect(screen, pos.color, (pos.x, pos.y, pos.xsize, pos.ysize))


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
        player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
        if player.left_boundary() < 0:
            player.x = 0 + (player.size / 2)
        if player.right_boundary() > WIDTH:
            player.x = WIDTH - (player.size / 2)

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
            if (player.collision(enemy)):
                end = datetime.now()
                print("Game Over!")
                score = (end-start).total_seconds()
                print(f"You survived for {score} seconds!")
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the player
        draw_player(player)

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
