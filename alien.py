# # import pygame

# # class Alien(pygame.sprite.Sprite):
# #     def __init__(self,type,x,y):
# #         super().__init__()
# #         self.type = type
# #         path = f"gallery/alien{type}.png"
# #         self.image = pygame.image.load(path)
# #         original = pygame.image.load(path)
# #         self.image = pygame.transform.scale(original,(100,100))
# #         self.rect= self.image.get_rect(topleft = (x,y))
# import pygame,random
# import os

# class Alien(pygame.sprite.Sprite):
#     def __init__(self, type, x, y):
#         super().__init__()
#         self.type = type
#         self.speed = 1
#         # Build the correct relative path
#         # path = os.path.join("gallery", f"alien{type}.png")
#         # try:
#         #     original = pygame.image.load(path)
#         # except pygame.error as e:
#         #     print(f"Could not load image: {path}")
#         #     raise SystemExit(e)
#         import os  # Make sure this is at the top of your file

# # Inside the __init__ method
#         base_dir = os.path.dirname(os.path.abspath(__file__))
#         path = os.path.join(base_dir, "gallery", f"{alien_type}.png")
#         original = pygame.image.load(path).convert_alpha()

#         self.image = pygame.transform.scale(original, (60, 60))
#         self.rect = self.image.get_rect(topleft=(x, y))
#     def update(self,direction):
#         self.rect.x += direction *self.speed
# class Mysteryship(pygame.sprite.Sprite):
#     def __init__(self, screen_width,offset):
#         super().__init__()
#         self.screen_width = screen_width
#         self.offset = offset
#         path = os.path.join("gallery", "mystery.png")
#         try:
#             original = pygame.image.load(path)
#         except pygame.error as e:
#             print(f"Could not load image: {path}")
#             raise SystemExit(e)
#         self.image = pygame.transform.scale(original, (60, 60))
#         x = random.choice([self.offset, self.screen_width + self.offset - self.image.get_width()])
#         if x == self.offset/2:
#             self.speed = 3
#         else:
#             self.speed = -3
#         self.rect = self.image.get_rect(topleft=(x, 90))

#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.right > self.screen_width + self.offset/2 or self.rect.left < self.offset/2:
#             self.kill()
# import pygame
# import os

# class Alien(pygame.sprite.Sprite):
#     def __init__(self, alien_type, x, y):
#         super().__init__()
#         base_dir = os.path.dirname(__file__)
#         image_path = os.path.join(base_dir, "gallery", f"{alien_type}.png")
#         self.image = pygame.image.load(image_path).convert_alpha()
#         self.image = pygame.transform.scale(self.image, (50, 50))
#         self.rect = self.image.get_rect(topleft=(x, y))

#         # Assign type for scoring or collision logic
#         self.type = alien_type

#     def update(self, direction):
#         self.rect.x += direction

# class Mysteryship(pygame.sprite.Sprite):
#     def __init__(self, x, screen_width):
#         super().__init__()
#         base_dir = os.path.dirname(__file__)
#         image_path = os.path.join(base_dir, "gallery", "mystery.png")
#         self.image = pygame.image.load(image_path).convert_alpha()
#         self.image = pygame.transform.scale(self.image, (60, 50))
#         self.rect = self.image.get_rect(topleft=(x, 80))
#         self.speed = 3
#         self.screen_width = screen_width

#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.x > self.screen_width + 100:
#             self.kill()
# import pygame
# import os

# class Alien(pygame.sprite.Sprite):
#     def __init__(self, alien_type, x, y):
#         super().__init__()

#         # Construct full image path
#         base_dir = os.path.dirname(os.path.abspath(__file__))
#         image_path = os.path.join(base_dir, "gallery", f"{alien_type}.png")

#         # Error handling if image is missing
#         if not os.path.exists(image_path):
#             raise FileNotFoundError(f"❌ Alien image not found: {image_path}")

#         self.image = pygame.image.load(image_path).convert_alpha()
#         self.image = pygame.transform.scale(self.image, (50, 50))
#         self.rect = self.image.get_rect(topleft=(x, y))

#         self.type = alien_type  # Useful for scoring/collision logic

#     def update(self, direction):
#         self.rect.x += direction


# class Mysteryship(pygame.sprite.Sprite):
#     def __init__(self, x, screen_width):
#         super().__init__()

#         # Construct image path
#         base_dir = os.path.dirname(os.path.abspath(__file__))
#         image_path = os.path.join(base_dir, "gallery", "mystery.png")

#         if not os.path.exists(image_path):
#             raise FileNotFoundError(f"❌ Mystery ship image not found: {image_path}")

#         self.image = pygame.image.load(image_path).convert_alpha()
#         self.image = pygame.transform.scale(self.image, (60, 50))
#         self.rect = self.image.get_rect(topleft=(x, 80))
#         self.speed = 3
#         self.screen_width = screen_width

#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.x > self.screen_width + 100:
#             self.kill()
import pygame
import os

class Alien(pygame.sprite.Sprite):
    def __init__(self, alien_type, x, y):
        super().__init__()
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, "gallery", f"alien{alien_type}.png")
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"❌ Alien image not found: {image_path}")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.type = alien_type  # Useful for scoring or logic

    def update(self, direction):
        self.rect.x += direction


class Mysteryship(pygame.sprite.Sprite):
    def __init__(self, x, screen_width):
        super().__init__()
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, "gallery", "mystery.png")
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"❌ Mystery ship image not found: {image_path}")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect(topleft=(x, 80))
        self.speed = 3
        self.screen_width = screen_width

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > self.screen_width + 100:
            self.kill()


            
                