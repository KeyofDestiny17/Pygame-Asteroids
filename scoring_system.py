import constants

class ScoringSystem:
    score = 0

    @classmethod
    def update_score(cls, radius):
        if radius == constants.ASTEROID_MIN_RADIUS * 3:
            cls.score += constants.LARGE_ASTEROID_SCORE
        elif radius == constants.ASTEROID_MIN_RADIUS * 2:
            cls.score += constants.MEDIUM_ASTEROID_SCORE
        elif radius == constants.ASTEROID_MIN_RADIUS:
            cls.score += constants.SMALL_ASTEROID_SCORE

    @classmethod
    def print_score(cls):
        print(f"Final Score: {cls.score}")