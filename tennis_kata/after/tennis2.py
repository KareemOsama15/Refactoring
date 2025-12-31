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
            "player1": self.p1_score,
            "player2": self.p2_score
        } 
        run_update_score = score_updaters.get(player_name)
        if not run_update_score:
            raise ValueError(f"Invalid player name: {player_name}")
        
        run_update_score()
       
    def score(self):
        result = ""
        if self.player1_score == self.player2_score and self.player1_score < 3:
            if self.player1_score == 0:
                result = "Love"
            if self.player1_score == 1:
                result = "Fifteen"
            if self.player1_score == 2:
                result = "Thirty"
            result += "-All"
        if self.player1_score == self.player2_score and self.player1_score > 2:
            result = "Deuce"

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
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.player1_score += 1

    def p2_score(self):
        self.player2_score += 1
