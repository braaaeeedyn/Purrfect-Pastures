import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_IMAGE_PATH, PLAYER_FIRING_IMAGE_PATH, PLAYER_SIZE, PLAYER_TOP_LIMIT, PLAYER_BOTTOM_LIMIT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.default_image = pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha()
        self.default_image = pygame.transform.scale(self.default_image, PLAYER_SIZE)
        
        self.firing_image = pygame.image.load(PLAYER_FIRING_IMAGE_PATH).convert_alpha()
        self.firing_image = pygame.transform.scale(self.firing_image, PLAYER_SIZE)
        
        self.image = self.default_image
        self.rect = self.image.get_rect()
        
        self.rect.midleft = (50, SCREEN_HEIGHT // 2)
        self.speed = 7

        self.is_firing = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > PLAYER_TOP_LIMIT:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < PLAYER_BOTTOM_LIMIT:
            self.rect.y += self.speed

    def start_firing(self):
        self.image = self.firing_image
        self.is_firing = True

    def stop_firing(self):
        self.image = self.default_image
        self.is_firing = False