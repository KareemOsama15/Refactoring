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

        # Case 5: A player wins the game (with at least 4 points and 2 points ahead)
        if self._is_player_win():
            return self._get_endgame_score()

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

    def _handle_tied_scores(self, score: int) -> str:
        """Handles the case when players are tied."""
        if score >= 3:
            return "Deuce"
        return TennisGame2.RESULT_MAP.get(score) + "-All"

    def _is_player1_scoring_and_player2_at_love(self) -> bool:
        """Returns True if player 1 is scoring and player 2 is at love, False otherwise."""
        return self.player1_score > 0 and self.player2_score == 0

    def _is_player2_scoring_and_player1_at_love(self) -> bool:
        """Returns True if player 2 is scoring and player 1 is at love, False otherwise."""
        return self.player2_score > 0 and self.player1_score == 0

    def _get_result_for_players_scoring(self, player_score: int) -> tuple[str, str]:
        """Returns the result for the players scoring situation."""
        leading_player_result: str = TennisGame2.RESULT_MAP.get(player_score, "")
        trailing_player_result: str = "Love"
        return leading_player_result, trailing_player_result

    def _is_player1_at_lead(self) -> bool:
        """Returns True if player 1 is leading, False otherwise."""
        return self.player1_score > self.player2_score and self.player1_score < 4

    def _is_player2_at_lead(self) -> bool:
        """Returns True if player 2 is leading, False otherwise."""
        return self.player2_score > self.player1_score and self.player2_score < 4

    def _get_result_for_players_at_lead(
        self, leading_player_score: int, late_player_score: int
    ) -> tuple[str, str]:
        """Returns the result for the players at lead situation."""
        player_at_lead_result: str = TennisGame2.RESULT_MAP.get(
            leading_player_score, ""
        )
        late_player_result: str = TennisGame2.RESULT_MAP.get(late_player_score, "")
        return player_at_lead_result, late_player_result

    def _is_player1_has_advantage(self) -> bool:
        """Returns True if player 1 has advantage, False otherwise."""
        return self.player1_score > self.player2_score and self.player2_score >= 3

    def _is_player2_has_advantage(self) -> bool:
        """Returns True if player 2 has advantage, False otherwise."""
        return self.player2_score > self.player1_score and self.player1_score >= 3

    def _get_player_advantage_result(self, player_name: str) -> str:
        """Returns the result for the player advantage situation."""
        return f"Advantage {player_name}"

    def _is_player_win(self) -> bool:
        """Returns True if a player has won, False otherwise."""
        return self.player1_score >= 4 or self.player2_score >= 4

    def _get_endgame_score(self) -> str:
        """Returns the score for endgame situations."""
        diff_score = self.player1_score - self.player2_score
        if abs(diff_score) >= 2:
            winner = self.player1_name if diff_score > 0 else self.player2_name
            return f"Win for {winner}"

        # Player with higher score has advantage
        leader = (
            self.player1_name
            if self.player1_score > self.player2_score
            else self.player2_name
        )
        return f"Advantage {leader}"

    def _is_player1_has_win(self) -> bool:
        """Returns True if player 1 has win, False otherwise."""
        return (
            self.player1_score >= 4
            and self.player2_score >= 0
            and (self.player1_score - self.player2_score) >= 2
        )

    def _is_player2_has_win(self) -> bool:
        return (
            self.player2_score >= 4
            and self.player1_score >= 0
            and (self.player2_score - self.player1_score) >= 2
        )

    def _get_player_win_result(self, player_name: str) -> str:
        """Returns the result for the player win situation."""
        return f"Win for {player_name}"

    def _get_regular_score(self) -> str:
        """Returns the regular score format."""
        player1_result = ""
        player2_result = ""
        result = ""

        # Case 2: Player 1 is scoring, Player 2 at Love (0) or Player 2 is scoring, Player 1 at Love (0)
        if self._is_player1_scoring_and_player2_at_love():
            player1_result, player2_result = self._get_result_for_players_scoring(
                self.player1_score
            )
            result = player1_result + "-" + player2_result

        if self._is_player2_scoring_and_player1_at_love():
            player2_result, player1_result = self._get_result_for_players_scoring(
                self.player2_score
            )
            result = player2_result + "-" + player1_result

        # Case 3: Both players have scored, Player 1 is leading but no one has won yet or Player 2 is leading but no one has won yet
        if self._is_player1_at_lead():
            player1_result, player2_result = self._get_result_for_players_at_lead(
                self.player1_score, self.player2_score
            )
            result = player1_result + "-" + player2_result

        if self._is_player2_at_lead():
            player1_result, player2_result = self._get_result_for_players_at_lead(
                self.player1_score, self.player2_score
            )
            result = player1_result + "-" + player2_result

        # Case 4: Advantage to Player 1 (deuce situation) or Advantage to Player 2 (deuce situation)
        if self._is_player1_has_advantage():
            result = self._get_player_advantage_result(self.player1_name)

        if self._is_player2_has_advantage():
            result = self._get_player_advantage_result(self.player2_name)

        return result
