from settings import MAX_MISSED_ENEMIES
from enemy import Enemy

def spawn_wave(all_sprites, enemies):
    for _ in range(3):  # Spawn 3 enemies per wave
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

def reset_game(all_sprites, enemies, player):
    global score, missed_enemies, game_state
    score = 0
    missed_enemies = 0
    game_state = "playing"

    # Clear all enemies and projectiles
    enemies.empty()
    all_sprites.empty()

    # Re-add the player to the sprite group
    all_sprites.add(player)

def draw_game_over_message(screen, font):
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    restart_text = font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - 20))
    screen.blit(restart_text, (screen.get_width() // 2 - restart_text.get_width() // 2, screen.get_height() // 2 + 20))
def render_outlined_text(text, font, color, outline_color, position, screen):
    """
    Renders text with a black outline.
    :param text: The text to render.
    :param font: The font object.
    :param color: The main text color (e.g., WHITE).
    :param outline_color: The outline color (e.g., BLACK).
    :param position: The (x, y) position of the text.
    :param screen: The screen surface to blit the text onto.
    """
    x, y = position

    # Render the outline by drawing the text at slight offsets
    outline_offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
    for offset in outline_offsets:
        outline_surface = font.render(text, True, outline_color)
        screen.blit(outline_surface, (x + offset[0], y + offset[1]))

    # Render the main text
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))