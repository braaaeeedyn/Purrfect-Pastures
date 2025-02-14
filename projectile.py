import pygame
from settings import SCREEN_WIDTH

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, frames):
        super().__init__()
        
        self.frames = frames

        self.current_frame = 0
        self.animation_speed = 0.1
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > SCREEN_WIDTH:
            self.kill()
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[int(self.current_frame)]