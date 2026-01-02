from .tennis_interface import TennisGameInterface
from typing import Dict, Callable


class TennisGame2(TennisGameInterface):

    RESULT_MAP = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

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
        # Case 1: Players are tied
        if self._are_players_tied():
            return self._handle_tied_scores(self.player1_score)

        # Case 2: A player has advantage (at least 4 points and 2 points ahead)
        if self._is_player_has_advantage():
            return self._check_endgame_score()

        # Case 3: Regular scoring (neither player has won yet)
        return self._get_regular_score()

    def _increase_player1_score(self):
        """Increases the score for player 1."""
        self.player1_score += 1

    def _increase_player2_score(self):
        """Increases the score for player 2."""
        self.player2_score += 1

    def _are_players_tied(self):
        """Returns True if the scores are tied, False otherwise."""
        return self.player1_score == self.player2_score

    def _is_player_at_lead(self) -> bool:
        """Returns True if a player is at lead, False otherwise."""
        return self.player1_score < 4 or self.player2_score < 4

    def _is_player_has_advantage(self) -> bool:
        """Returns True if a one player has advantage which means 4 points or more, False otherwise."""
        return self.player1_score >= 4 or self.player2_score >= 4

    def _handle_tied_scores(self, score: int) -> str:
        """Handles the case when players are tied."""
        if score >= 3:
            return "Deuce"
        return TennisGame2.RESULT_MAP.get(score) + "-All"

    def _check_endgame_score(self) -> str:
        """Returns the score for endgame situations."""
        diff_score = self.player1_score - self.player2_score
        if abs(diff_score) >= 2:
            winner = self.player1_name if diff_score > 0 else self.player2_name
            return f"Win for {winner}"
        return self._get_regular_score()

    def _get_regular_score(self) -> str:
        """Returns the regular score format."""
        diff_score = self.player1_score - self.player2_score

        # Handle case where Player with higher score has advantage
        if abs(diff_score) > 0 and self._is_player_has_advantage():
            leader = (
                self.player1_name
                if self.player1_score > self.player2_score
                else self.player2_name
            )
            return f"Advantage {leader}"

        # Handle case where one player is ahead but not by enough to win
        if abs(diff_score) > 0 and self._is_player_at_lead():
            return self._handle_player_at_lead()

    def _handle_player_at_lead(self) -> str:
        player1_score_result = TennisGame2.RESULT_MAP.get(self.player1_score, "")
        player2_score_result = TennisGame2.RESULT_MAP.get(self.player2_score, "")
        return f"{player1_score_result}-{player2_score_result}"
