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
        """Returns the score for the players."""
        result = ""
        if self._are_players_tied():
            if self._is_score_higher_than_3():
                result = self._get_tied_score_result(self.player1_score)

            elif self._is_deuce():
                result = self._get_deuce_result()

        p1res = ""
        p2res = ""

        # Case 1: Player 1 is scoring, Player 2 at Love (0)
        if self._is_player1_scoring_and_player2_at_love():
            p1res, p2res = self._get_result_for_player_scoring(self.player1_score)
            result = p1res + "-" + p2res

        # Case 2: Player 2 is scoring, Player 1 at Love (0)
        if self._is_player2_scoring_and_player1_at_love():
            p2res, p1res = self._get_result_for_player_scoring(self.player2_score)
            result = p2res + "-" + p1res

        # Case 3: Both players have scored, Player 1 is leading but no one has won yet
        if self._is_player1_at_lead():
            if self.player1_score == 2:
                p1res = "Thirty"
            if self.player1_score == 3:
                p1res = "Forty"
            if self.player2_score == 1:
                p2res = "Fifteen"
            if self.player2_score == 2:
                p2res = "Thirty"
            result = p1res + "-" + p2res

        # Case 4: Both players have scored, Player 2 is leading but no one has won yet
        if self._is_player2_at_lead():
            if self.player2_score == 2:
                p2res = "Thirty"
            if self.player2_score == 3:
                p2res = "Forty"
            if self.player1_score == 1:
                p1res = "Fifteen"
            if self.player1_score == 2:
                p1res = "Thirty"
            result = p1res + "-" + p2res

        # Case 5: Advantage to Player 1 (deuce situation)
        if self.player1_score > self.player2_score and self.player2_score >= 3:
            result = "Advantage player1"

        # Case 6: Advantage to Player 2 (deuce situation)
        if self.player2_score > self.player1_score and self.player1_score >= 3:
            result = "Advantage player2"

        # Case 7: Player 1 wins the game (with at least 4 points and 2 points ahead)
        if (
            self.player1_score >= 4
            and self.player2_score >= 0
            and (self.player1_score - self.player2_score) >= 2
        ):
            result = "Win for player1"

        # Case 8: Player 2 wins the game (with at least 4 points and 2 points ahead)
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
        """Increases the score for player 1."""
        self.player1_score += 1

    def _increase_player2_score(self):
        """Increases the score for player 2."""
        self.player2_score += 1

    def _are_players_tied(self):
        """Returns True if the scores are tied, False otherwise."""
        return self.player1_score == self.player2_score

    def _is_deuce(self) -> bool:
        """Returns True if the scores are deuce, False otherwise."""
        return self.player1_score > 2 and self.player1_score == self.player2_score

    def _get_deuce_result(self) -> str:
        """Returns the result for the deuce situation."""
        return "Deuce"

    def _is_score_higher_than_3(self) -> bool:
        """Returns True if the score is higher than 3, False otherwise."""
        return self.player1_score < 3

    def _get_tied_score_result(self, score: int) -> str:
        """Returns the result for the tied score situation."""
        result = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
        }.get(score)
        return result + "-All"

    def _is_player1_scoring_and_player2_at_love(self) -> bool:
        """Returns True if player 1 is scoring and player 2 is at love, False otherwise."""
        return self.player1_score > 0 and self.player2_score == 0

    def _is_player2_scoring_and_player1_at_love(self) -> bool:
        """Returns True if player 2 is scoring and player 1 is at love, False otherwise."""
        return self.player2_score > 0 and self.player1_score == 0

    def _get_result_for_player_scoring(self, player_score: int) -> tuple[str, str]:
        """Returns the result for the player scoring situation."""
        result_dict: Dict[int, str] = {
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        leading_player_result: str = result_dict.get(player_score, "")
        trailing_player_result: str = "Love"
        return leading_player_result, trailing_player_result

    def _is_player1_at_lead(self) -> bool:
        """Returns True if player 1 is leading, False otherwise."""
        return self.player1_score > self.player2_score and self.player1_score < 4

    def _is_player2_at_lead(self) -> bool:
        """Returns True if player 2 is leading, False otherwise."""
        return self.player2_score > self.player1_score and self.player2_score < 4

