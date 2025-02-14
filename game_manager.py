class GameManager:
    def __init__(self):
        self.score = 0
        self.missed_enemies = 0
        self.game_state = "playing"
    def increase_score(self, points):
        """Increase the score by the given number of points."""
        self.score += points
    def increment_missed_enemies(self):
        """Increment the missed enemies counter."""
        self.missed_enemies += 1
    def reset_game(self):
        """Reset the game state."""
        self.score = 0
        self.missed_enemies = 0
        self.game_state = "playing"
game_manager = GameManager()