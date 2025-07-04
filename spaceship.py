# import pygame
# from laser import Laser 
# import os
# #Sprites represent game objects like players, 
# #enemies, bullets, etc., and are used to organize and manage them efficiently.
# class Spaceship(pygame.sprite.Sprite):
#     def __init__(self,Screen_width,Screen_height,offset):
#         super().__init__()
#         self.offset = offset
#         self.Screen_width = Screen_width
#         self.Screen_height = Screen_height        
#         import os
#         # self.image = pygame.image.load(os.path.join("gallery", "spaceship.png"))
#         # original = pygame.image.load(os.path.join("gallery", "spaceship.png"))   
#         import os
#         image_path = os.path.join("gallery", "spaceship.png")
#         self.image = pygame.image.load(image_path).convert_alpha()
#         self.image = pygame.transform.scale(self.image, (80, 80))
#         self.image = pygame.transform.scale(original,(80,80))
#         self.rect = self.image.get_rect(midbottom = ((Screen_width+self.offset)/2,Screen_height))  # --- getting the dimension
#         self.speed = 6
#         self.lasers_group = pygame.sprite.Group()
#         self.laser_ready = True
#         self.laser_time = 0
#         self.laser_delay = 130
#         self.laser_sound = pygame.mixer.Sound("sound/laser.ogg.mp3")
#     def get_user_input(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_RIGHT]:
#             self.rect.x +=self.speed
#         if keys[pygame.K_LEFT]:
#             self.rect.x -= self.speed
#         if keys[pygame.K_SPACE] and self.laser_ready:
#             self.laser_ready = False
#             laser = Laser(self.rect.center,5,self.Screen_height)
#             self.lasers_group.add(laser)
#             self.laser_time =pygame.time.get_ticks()
#             self.laser_sound.play()
#     def update(self):
#         self.get_user_input()
#         self.constrain_movement()
#         self.lasers_group.update()
#         self.recharge_laser()
#     def constrain_movement(self):
#         if self.rect.right > self.Screen_width:
#             self.rect.right = self.Screen_width
#         if self.rect.left < self.offset:
#             self.rect.left = self.offset
#     def recharge_laser(self):
#         if not self.laser_ready:
#             current_time = pygame.time.get_ticks()
#             if current_time - self.laser_time >=  self.laser_delay:
#                 self.laser_ready = True
#     def reset(self):
#         self.rect = self.image.get_rect(midbottom = ((self.Screen_width+self.offset)/2,self.Screen_height))
#         self.lasers_group.empty()
        
import pygame
import os
from laser import Laser 

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, Screen_width, Screen_height, offset):
        super().__init__()
        self.offset = offset
        self.Screen_width = Screen_width
        self.Screen_height = Screen_height        

        # Get absolute path of current file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "gallery", "spaceship.png")
        sound_path = os.path.join(base_dir, "sound", "laser.ogg.mp3")

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(midbottom=((Screen_width + self.offset) / 2, Screen_height))

        self.speed = 6
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 130
        self.laser_sound = pygame.mixer.Sound(sound_path)

    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.laser_ready = False
            laser = Laser(self.rect.center, 5, self.Screen_height)
            self.lasers_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()

    def constrain_movement(self):
        if self.rect.right > self.Screen_width:
            self.rect.right = self.Screen_width
        if self.rect.left < self.offset:
            self.rect.left = self.offset

    def recharge_laser(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def reset(self):
        self.rect = self.image.get_rect(midbottom=((self.Screen_width + self.offset) / 2, self.Screen_height))
        self.lasers_group.empty()
