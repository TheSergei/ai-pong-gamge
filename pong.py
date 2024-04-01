import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [6, 6]
paddle_speed = 5
player_pos = [50, HEIGHT // 2 - 50]
opponent_pos = [WIDTH - 50, HEIGHT // 2 - 50]
paddle_width = 10
paddle_height = 100
score_player = 0
score_opponent = 0

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += paddle_speed

    # Basic AI for opponent's paddle
    if ball_speed[0] > 0:
        if ball_pos[1] < opponent_pos[1] + paddle_height // 2:
            opponent_pos[1] -= paddle_speed
        elif ball_pos[1] > opponent_pos[1] + paddle_height // 2:
            opponent_pos[1] += paddle_speed

    # Ball movement
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with walls
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT:
        ball_speed[1] *= -1

    # Ball collision with paddles
    if ball_pos[0] <= player_pos[0] + paddle_width and player_pos[1] <= ball_pos[1] <= player_pos[1] + paddle_height:
        ball_speed[0] *= -1
    if ball_pos[0] >= opponent_pos[0] - paddle_width and opponent_pos[1] <= ball_pos[1] <= opponent_pos[1] + paddle_height:
        ball_speed[0] *= -1

    # Ball out of bounds
    if ball_pos[0] <= 0:
        score_opponent += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
    elif ball_pos[0] >= WIDTH:
        score_player += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (opponent_pos[0], opponent_pos[1], paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_pos[0] - 10, ball_pos[1] - 10, 20, 20))

    # Display scores
    font = pygame.font.Font(None, 36)
    player_score_text = font.render(str(score_player), True, WHITE)
    opponent_score_text = font.render(str(score_opponent), True, WHITE)
    screen.blit(player_score_text, (WIDTH // 2 - 50, 20))
    screen.blit(opponent_score_text, (WIDTH // 2 + 30, 20))

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
