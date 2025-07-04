import pygame, os
pygame.init()

# Load window
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Font Test")

# Load font
font_path = os.path.join("gallery", "font", "monogram.ttf")
if not os.path.exists(font_path):
    print("❌ Font file not found:", font_path)
    exit()
font = pygame.font.Font(font_path, 25)
text_surface = font.render("✅ Font Loaded Successfully!", True, (255, 255, 0))

# Display loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(text_surface, (50, 80))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

