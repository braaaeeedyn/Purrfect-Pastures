import pygame
import random
from settings import *
from player import Player
from projectile import Projectile
from enemy import Enemy
from utils import render_outlined_text, spawn_wave, reset_game, draw_game_over_message
from game_manager import game_manager

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Purrfect Pastures")
fullscreen = False
background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

PRELOADED_PROJECTILE_FRAMES = [
    pygame.image.load(f"{PROJECTILE_ANIMATION_PATH}frame{i}.png").convert_alpha()
    for i in range(1, NUM_PROJECTILE_FRAMES + 1)
]
PRELOADED_PROJECTILE_FRAMES = [pygame.transform.scale(frame, PROJECTILE_SIZE) for frame in PRELOADED_PROJECTILE_FRAMES]

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
SPAWN_INTERVAL = 1500
spawn_timer = SPAWN_INTERVAL
last_spawn_time = pygame.time.get_ticks()


pygame.mixer.init()

BACKGROUND_MUSIC_FILES = {
    "assets/background_music1.mp3": 800,
    "assets/background_music2.mp3": 814,
}


def play_random_background_music():
    selected_music, music_length = random.choice(list(BACKGROUND_MUSIC_FILES.items()))  # Randomly choose a music file and its length
    pygame.mixer.music.load(selected_music)
    
    pygame.mixer.music.play() 
    pygame.mixer.music.stop()
    random_start_time = random.uniform(0, music_length)
    pygame.mixer.music.play(-1, start=random_start_time)  
    pygame.mixer.music.set_volume(0.1) 

play_random_background_music()

def game_loop():
    global fullscreen, screen, spawn_timer, last_spawn_time

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                if event.key == pygame.K_SPACE and game_manager.game_state == "playing":
                    player.start_firing()
                    projectile = Projectile(player.rect.centerx, player.rect.centery, PRELOADED_PROJECTILE_FRAMES)
                    all_sprites.add(projectile)
                    projectiles.add(projectile)
                if event.key == pygame.K_r and game_manager.game_state == "game_over":
                    game_manager.reset_game()
                    reset_game(all_sprites, enemies, player)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.stop_firing()
        if current_time - last_spawn_time >= 10000:
            spawn_timer = max(500, spawn_timer * 0.8)
            last_spawn_time = current_time

        if current_time - last_spawn_time >= spawn_timer and game_manager.game_state == "playing":
            spawn_wave(all_sprites, enemies)
            last_spawn_time = current_time 

        all_sprites.update()

        for projectile in projectiles:
            enemy_hits = pygame.sprite.spritecollide(projectile, enemies, False)
            for enemy in enemy_hits:
                enemy.take_damage()
                projectile.kill()
        
        if game_manager.missed_enemies >= MAX_MISSED_ENEMIES:
            game_manager.game_state = "game_over"
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        render_outlined_text(f"Score: {game_manager.score}", font, WHITE, BLACK, (10, 10), screen)
        render_outlined_text(f"Missed: {game_manager.missed_enemies}/{MAX_MISSED_ENEMIES}", font, RED, BLACK, (10, 50), screen)
        if game_manager.game_state == "game_over":
            render_outlined_text("Game Over!", font, WHITE, BLACK, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20), screen)
            render_outlined_text("Press R to Restart", font, WHITE, BLACK, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 20), screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    game_loop()