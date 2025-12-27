from tennis_interface import TennisGameInterface
from typing import Dict, Callable


class TennisGame1(TennisGameInterface):
    def __init__(self, player1_name: str, player2_name: str) -> None:
        super().__init__(player1_name, player2_name)

    def won_point(self, player_name: str):
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
        if self._is_deuce():
            result = self._handle_deuce(self.player1_score)
        elif self._has_advantage():
            result = self._handle_player_has_advantage()
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

    def _is_deuce(self) -> bool:
        """
        Returns True if the players are tied, False otherwise.
        """
        return self.player1_score == self.player2_score

    def _handle_deuce(self, score: int) -> str:
        """
        Returns the score for the players if they are tied.
        """
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(score, "Deuce")

    def _has_advantage(self) -> bool:
        """
        Returns True if the player has advantage, False otherwise.
        """
        return self.player1_score >= 4 or self.player2_score >= 4

    def _handle_player_has_advantage(self) -> str:
        """
        Returns the result based on the score for the player who has advantage.
        """
        diff_score: int = self.player1_score - self.player2_score
        if diff_score == 1:
            return "Advantage player1"
        elif diff_score == -1:
            return "Advantage player2"
        elif diff_score >= 2:
            return "Win for player1"

        return "Win for player2"