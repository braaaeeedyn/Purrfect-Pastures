from game_manager import GameManager

# Singleton instance of GameManager
game_manager = GameManager()
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

MAX_MISSED_ENEMIES = 5

BACKGROUND_IMAGE_PATH = "assets/background.png"
PLAYER_IMAGE_PATH = "assets/player.png"
PLAYER_FIRING_IMAGE_PATH = "assets/player_firing.png"
SLOW_ENEMY_ANIMATION_PATH = "assets/slow_enemy_animation/"
MEDIUM_ENEMY_ANIMATION_PATH = "assets/medium_enemy_animation/"
FAST_ENEMY_ANIMATION_PATH = "assets/fast_enemy_animation/"
PROJECTILE_ANIMATION_PATH = "assets/projectile_animation/"
BACKGROUND_MUSIC_PATH = "assets/background_music.mp3" 
PRELOADED_PROJECTILE_FRAMES = None
NUM_ANIMATION_FRAMES = 3
NUM_PROJECTILE_FRAMES = 4
PLAYER_SIZE = (100, 100)
ENEMY_SIZE = (75, 75)
PROJECTILE_SIZE = (50, 50)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_TOP_LIMIT = SCREEN_HEIGHT // 3
PLAYER_BOTTOM_LIMIT = SCREEN_HEIGHT * 2 // 3