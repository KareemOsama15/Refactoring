from .tennis_interface import TennisGameInterface
from typing import Dict, Callable


class TennisGame2(TennisGameInterface):
    def __init__(self, player1_name, player2_name):
        super().__init__(player1_name, player2_name)

    def won_point(self, player_name) -> None:
        """
        Updates the score for the player who won the point.
        """
        score_updaters: Dict[str, Callable] = {
            "player1": self._increase_player1_score,
            "player2": self._increase_player2_score,
        }
        run_update_score = score_updaters.get(player_name)
        if not run_update_score:
            raise ValueError(f"Invalid player name: {player_name}")

        run_update_score()

    def score(self):
        result = ""
        if self._are_players_tied():
            if self._is_score_higher_than_3():
                result = self._get_tied_score_result(self.player1_score)
            
            elif self._is_deuce():
                result = self._get_deuce_result()

        p1res = ""
        p2res = ""
        if self.player1_score > 0 and self.player2_score == 0:
            if self.player1_score == 1:
                p1res = "Fifteen"
            if self.player1_score == 2:
                p1res = "Thirty"
            if self.player1_score == 3:
                p1res = "Forty"

            p2res = "Love"
            result = p1res + "-" + p2res
        if self.player2_score > 0 and self.player1_score == 0:
            if self.player2_score == 1:
                p2res = "Fifteen"
            if self.player2_score == 2:
                p2res = "Thirty"
            if self.player2_score == 3:
                p2res = "Forty"

            p1res = "Love"
            result = p1res + "-" + p2res

        if self.player1_score > self.player2_score and self.player1_score < 4:
            if self.player1_score == 2:
                p1res = "Thirty"
            if self.player1_score == 3:
                p1res = "Forty"
            if self.player2_score == 1:
                p2res = "Fifteen"
            if self.player2_score == 2:
                p2res = "Thirty"
            result = p1res + "-" + p2res
        if self.player2_score > self.player1_score and self.player2_score < 4:
            if self.player2_score == 2:
                p2res = "Thirty"
            if self.player2_score == 3:
                p2res = "Forty"
            if self.player1_score == 1:
                p1res = "Fifteen"
            if self.player1_score == 2:
                p1res = "Thirty"
            result = p1res + "-" + p2res

        if self.player1_score > self.player2_score and self.player2_score >= 3:
            result = "Advantage player1"

        if self.player2_score > self.player1_score and self.player1_score >= 3:
            result = "Advantage player2"

        if (
            self.player1_score >= 4
            and self.player2_score >= 0
            and (self.player1_score - self.player2_score) >= 2
        ):
            result = "Win for player1"
        if (
            self.player2_score >= 4
            and self.player1_score >= 0
            and (self.player2_score - self.player1_score) >= 2
        ):
            result = "Win for player2"
        return result

    def set_p1_score(self, number):
        for _ in range(number):
            self._increase_player1_score()

    def set_p2_score(self, number):
        for _ in range(number):
            self._increase_player2_score()

    def _increase_player1_score(self):
        self.player1_score += 1

    def _increase_player2_score(self):
        self.player2_score += 1

    def _are_players_tied(self):
        return self.player1_score == self.player2_score

    def _is_deuce(self) -> bool:
        return self.player1_score > 2 and self.player1_score == self.player2_score

    def _get_deuce_result(self) -> str:
        return "Deuce"

    def _is_score_higher_than_3(self) -> bool:
        return self.player1_score < 3

    def _get_tied_score_result(self, score: int) -> str:
        result = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
        }.get(score)
        return result + "-All"
