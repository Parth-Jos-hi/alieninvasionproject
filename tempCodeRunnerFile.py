import pygame, sys, random, os
from game import Game

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
OFFSET = 30
WHITE = (250, 250, 250)
YELLOW = (243, 216, 63)

# Load font with error handling
font_path = os.path.join("gallery", "font", "PublicPixel.ttf")
if not os.path.exists(font_path):
    print(f"❌ Font file not found at: {font_path}")
    sys.exit()

font = pygame.font.Font(font_path, 15)
# font = pygame.font.SysFont("Arial", 15)  # fallback option

# Pre-rendered UI texts
level_surface = font.render("LEVEL 01", False, YELLOW)
game_over_surface = font.render("GAME OVER", False, YELLOW)
score_text_surface = font.render("SCORE", False, YELLOW)
highscore_text_surface = font.render("HIGHSCORE", False, YELLOW)

# Setup display
screen = pygame.display.set_mode((SCREEN_HEIGHT + OFFSET, SCREEN_WIDTH + 2 * OFFSET))
pygame.display.set_caption("Antriksh ke Lutere")
clock = pygame.time.Clock()

# Game object
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

# Custom events
SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()

        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not game.run:
        game.reset()

    # Update game logic
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_laser_group.update()
        game.mystery_ship_group.update()
        game.check_with_collisions()

    # Draw background
    screen.fill(WHITE)

    # UI Border & line
    pygame.draw.rect(screen, YELLOW, (10, 10, 760, 760), 2, 0, 50, 50, 50, 50)
    pygame.draw.line(screen, YELLOW, (25, 730), (762, 730), 2)

    # Draw Level Text
    text_surface = font.render("Level 1", True, (255, 255, 255))
    screen.blit(text_surface, (100, 100))

    # Draw status: level or game over
    if game.run:
        screen.blit(level_surface, (570, 740))
    else:
        screen.blit(game_over_surface, (570, 740))

    # Draw Lives
    for life in range(game.lives):
        x = 50 + life * 50
        screen.blit(game.spaceship_group.sprite.image, (x, 700))

    # Draw Score
    screen.blit(score_text_surface, (50, 15))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, (50, 40))

    # Draw Highscore
    screen.blit(highscore_text_surface, (550, 15))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, YELLOW)
    screen.blit(highscore_surface, (625, 40))

    # Draw Game Elements
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    game.alien_laser_group.draw(screen)

    for obstacle in game.obstacles:
        obstacle.blocks_groups.draw(screen)

    game.alien_group.draw(screen)            
    game.mystery_ship_group.draw(screen)

    # Update the display
    pygame.display.update()
    clock.tick(60)  # Maintain 60 FPS
