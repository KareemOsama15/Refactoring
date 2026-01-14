from abc import ABC, abstractmethod
from item import Item


class ItemUpdaterInterface(ABC):
    """Item updater interface."""

    @abstractmethod
    def update(self, item: Item) -> None:
        """Update the quality or sell_in of the item."""
        raise NotImplementedError("Subclasses must implement this method")
