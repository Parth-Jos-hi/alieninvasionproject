# import pygame,sys,random
# from game import Game
# # display text ---- create a font --- a surface with the text ---  display  the surface with the blit method
# pygame.init()
# SCREEN_WIDTH = 750
# SCREEN_HEIGHT = 750
# OFFSET = 30 
# White= (250,250,250)
# Yellow = (243,216,63)
# font = pygame.font.Font("Alien Invasion//gallery/font/PublicPixel.ttf", 15)
# # font = pygame.font.SysFont("Arial", 15)   
# level_surface = font.render("LEVEL 01",False , Yellow )
# game_over_surface = font.render("game over", False , Yellow)
# score_text_surface = font.render("SCORE",False,Yellow)
# highscore_text_surface = font.render("HIGHSCORE",False,Yellow)
# screen = pygame.display.set_mode((SCREEN_HEIGHT+OFFSET,SCREEN_WIDTH+ 2*OFFSET))
# pygame.display.set_caption("Antriksh ke lutere")
# clock = pygame.time.Clock() # for setting fps
# game = Game(SCREEN_WIDTH,SCREEN_HEIGHT,OFFSET)
# SHOOT_LASER =pygame.USEREVENT     # USEREVENT ---- used to create custom events
# pygame.time.set_timer(SHOOT_LASER,300)
# MYSTERYSHIP = pygame.USEREVENT + 1
# pygame.time.set_timer(MYSTERYSHIP,random.randint(4000, 8000))
# #setting up the game loop                       
# while True:
#     for event in pygame.event.get(): # --- will get all the events that is happening in the pygame code
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == SHOOT_LASER and game.run:
#             game.alien_shoot_laser()
#         if event.type == MYSTERYSHIP and game.run:
#             game.create_mystery_ship()
#             pygame.time.set_timer(MYSTERYSHIP,random.randint(4000, 8000))
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE] and game.run  == False:
#             game.reset()
        
#     #updating
#     if game.run:
#         game.spaceship_group.update()
#         game.move_aliens()  
#         game.alien_laser_group.update()
#         game.mystery_ship_group.update()
#         game.check_with_collisions()   
    
#     #drawing
#     screen.fill(White)                       
#     # UI
#     pygame.draw.rect(screen,Yellow,(10,10,760,760),2,0,50,50,50,50)
#     pygame.draw.line(screen,Yellow,(25,730),(762,730),2)
#     text_surface = font.render("Level 1", True, (255, 255, 255)) 
#     screen.blit(text_surface, (100, 100))
#     if game.run :
#         screen.blit(level_surface,(570,740,50,50))
#     else :
#         screen.blit(game_over_surface,(570,740,50,50))
#     for life in range(game.lives):
#         x = 50 + life * 50  # Start at 50 and space out each life by 50
#         screen.blit(game.spaceship_group.sprite.image, (x, 700))  # Draw the spaceship image for each life
#     screen.blit(score_text_surface,(50,15,50,50)) 
#     formatted_score = str(game.score).zfill(5)
#     score_surface = font.render(formatted_score,False,Yellow)
#     screen.blit(score_surface,(50,40,50,50))  
#     screen.blit(highscore_text_surface,(550,15,50,50))
#     formatted_highscore = str(game.highscore).zfill(5)
#     highscore_surface = font.render(formatted_highscore,False,Yellow)
#     screen.blit(highscore_surface,(625,40,50,50))
#     game.spaceship_group.draw(screen)
#     game.spaceship_group.sprite.lasers_group.draw(screen)
#     game.alien_laser_group.draw(screen) 
#     for obstacle in game.obstacles:
#         obstacle.blocks_groups.draw(screen)
#     game.alien_group.draw(screen)
#     game.mystery_ship_group.draw(screen)
#     pygame.display.update()
#     clock.tick(60) # --- 60 fps setted for the game
import pygame, sys, random, os
from game import Game

# Ensure the working directory is the same as this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
OFFSET = 30
WHITE = (250, 250, 250)
YELLOW = (243, 216, 63)

# Font path
font_path = os.path.join("gallery", "font", "PublicPixel.ttf")
print("📁 Looking for font at:", os.path.abspath(font_path))

if not os.path.exists(font_path):
    print(f"❌ Font file not found at: {font_path}")
    sys.exit()

# Load font
font = pygame.font.Font(font_path, 15)

# Pre-render UI text surfaces
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

    # Restart game on SPACE if over
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not game.run:
        game.reset()

    # Game logic updates
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_laser_group.update()
        game.mystery_ship_group.update()
        game.check_with_collisions()

    # Clear screen
    screen.fill(WHITE)

    # Draw UI border and level line
    pygame.draw.rect(screen, YELLOW, (10, 10, 760, 760), 2, 0, 50, 50, 50, 50)
    pygame.draw.line(screen, YELLOW, (25, 730), (762, 730), 2)

    # Draw level text
    text_surface = font.render("Level 1", True, (255, 255, 255))
    screen.blit(text_surface, (100, 100))

    # Show current game state
    if game.run:
        screen.blit(level_surface, (570, 740))
    else:
        screen.blit(game_over_surface, (570, 740))

    # Draw player lives
    for life in range(game.lives):
        x = 50 + life * 50
        screen.blit(game.spaceship_group.sprite.image, (x, 700))

    # Score
    screen.blit(score_text_surface, (50, 15))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, (50, 40))

    # Highscore
    screen.blit(highscore_text_surface, (550, 15))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, YELLOW)
    screen.blit(highscore_surface, (625, 40))

    # Draw all game objects
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    game.alien_laser_group.draw(screen)

    for obstacle in game.obstacles:
        obstacle.blocks_groups.draw(screen)

    game.alien_group.draw(screen)
    game.mystery_ship_group.draw(screen)

    # Update display and control frame rate
    pygame.display.update()
    clock.tick(60)
