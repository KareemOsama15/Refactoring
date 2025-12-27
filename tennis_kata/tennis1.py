from tennis_interface import TennisGameInterface

class TennisGame1(TennisGameInterface):
    def __init__(self, player1_name: str, player2_name: str) -> None:
        super().__init__(player1_name, player2_name)

    def won_point(self, player_name):
        """
        Increments the score of the player based on the player_name.
        """
        map_player_name_to_score = {
            "player1": self.player1_score,
            "player2": self.player2_score,
        }
        map_player_name_to_score[player_name] += 1

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
