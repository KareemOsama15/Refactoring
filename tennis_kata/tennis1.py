from tennis_interface import TennisGameInterface
from typing import Dict, Callable


class TennisGame1(TennisGameInterface):
    def __init__(self, player1_name: str, player2_name: str) -> None:
        super().__init__(player1_name, player2_name)

    def won_point(self, player_name):
        """
        Increments the score of the player based on the player_name.
        """
        score_updaters: Dict[str, Callable[[], None]] = {
            "player1": lambda: setattr(self, "player1_score", self.player1_score + 1),
            "player2": lambda: setattr(self, "player2_score", self.player2_score + 1),
        }
        player_score_updater = score_updaters.get(player_name)
        if player_score_updater is None:
            raise ValueError(f"Invalid player name: {player_name}")
        player_score_updater()

    def score(self):
        result = ""
        temp_score = 0
        if self.player1_score == self.player2_score:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1_score, "Deuce")
        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result = self.player1_score - self.player2_score
            if minus_result == 1:
                result = "Advantage player1"
            elif minus_result == -1:
                result = "Advantage player2"
            elif minus_result >= 2:
                result = "Win for player1"
            else:
                result = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    result += "-"
                    temp_score = self.player2_score
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result
