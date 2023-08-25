import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Reaction Time Test")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up game variables
start_time = None
reaction_time = None
click_before_green = False
game_over = False

def restart_game():
    global start_time, reaction_time, click_before_green, game_over
    start_time = None
    reaction_time = None
    click_before_green = False
    game_over = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
                if start_time is not None and not click_before_green:
                    end_time = time.time()
                    reaction_time = end_time - start_time - 5
                    if reaction_time < 0:
                        click_before_green = True
                    else:
                        game_over = True
                else:
                    restart_game()
        elif event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                restart_game()

    display.fill(WHITE)

    if click_before_green:
        reaction_text = font.render("Clicked before green!", True, RED)
        display.blit(reaction_text, (width // 2 - reaction_text.get_width() // 2, height // 2 + 70))
    elif not game_over and (start_time is None or (time.time() - start_time) < 5):
        pygame.draw.rect(display, RED, (width // 2 - 50, height // 2 - 50, 100, 100))
        if start_time is None:
            start_time = time.time()
    elif not game_over:
        pygame.draw.rect(display, GREEN, (width // 2 - 50, height // 2 - 50, 100, 100))
    elif game_over:
        game_over_text = font.render("Game Over", True, RED)
        display.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 30))
        if reaction_time is not None and not click_before_green:
            reaction_text = font.render(f"Your reaction time: {reaction_time:.3f}  seconds", True, GREEN)
            display.blit(reaction_text, (width // 2 - reaction_text.get_width() // 2, height // 2 + 10))
        restart_text = font.render("Press SPACE to restart", True, GREEN)
        display.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 50))

    pygame.display.flip()

pygame.quit()
