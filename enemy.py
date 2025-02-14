import pygame
import random
from game_manager import game_manager
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SLOW_ENEMY_ANIMATION_PATH, MEDIUM_ENEMY_ANIMATION_PATH, FAST_ENEMY_ANIMATION_PATH, NUM_ANIMATION_FRAMES, ENEMY_SIZE

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = random.uniform(2, 4)
        if self.speed <= 2.5:
            self.enemy_type = "slow"
            self.health = 3
            animation_path = SLOW_ENEMY_ANIMATION_PATH
        elif self.speed <= 3.5:
            self.enemy_type = "medium"
            self.health = 2
            animation_path = MEDIUM_ENEMY_ANIMATION_PATH
        else:
            self.enemy_type = "fast"
            self.health = 1
            animation_path = FAST_ENEMY_ANIMATION_PATH

        self.frames = [
            pygame.image.load(f"{animation_path}frame{i}.png").convert_alpha()
            for i in range(1, NUM_ANIMATION_FRAMES + 1)
        ]
        self.frames = [pygame.transform.scale(frame, ENEMY_SIZE) for frame in self.frames] 
        self.current_frame = 0
        self.animation_speed = 0.1
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        top_limit = SCREEN_HEIGHT // 3
        bottom_limit = SCREEN_HEIGHT * 2 // 3 - ENEMY_SIZE[1]
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)
        self.rect.y = random.randint(top_limit, bottom_limit)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
            game_manager.increment_missed_enemies()
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[int(self.current_frame)]

    def take_damage(self):
        global score
        self.health -= 1
        if self.health <= 0:
            if self.enemy_type == "slow":
                game_manager.increase_score(50)
            elif self.enemy_type == "medium":
                game_manager.increase_score(75)
            elif self.enemy_type == "fast":
                game_manager.increase_score(100)
            self.kill()