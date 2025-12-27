from abc import ABC, abstractmethod

class TennisGameInterface(ABC):
    """
    This is the interface for the tennis game.
    It defines the methods that must be implemented by the child classes.
    """

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name

    @abstractmethod
    def won_point(self, player_name: str) -> None:
        """
        This method is called when a player wins a point.
        """
        raise NotImplementedError("Child class must implement won_point method")

    @abstractmethod
    def score(self) -> str:
        """
        This method returns the score of the game.
        """
        raise NotImplementedError("Child class must implement score method")
