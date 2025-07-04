import pygame
import os

pygame.init()

font_path = os.path.join("gallery", "font", "PublicPixel.ttf")
if not os.path.exists(font_path):
    print("❌ Font path does not exist:", font_path)
else:
    print("✅ Font path exists:", font_path)

try:
    font = pygame.font.Font(font_path, 20)
    surface = font.render("Font Test OK", True, (255, 255, 0))
    print("✅ Font loaded and rendered successfully.")
except Exception as e:
    print("❌ Error loading font:", e)
