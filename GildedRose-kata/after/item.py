"""Module that contains the Item class."""


class Item:
    """Item class."""

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name: str = name
        self.sell_in: int = sell_in
        self.quality: int = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @property
    def quality(self) -> int:
        return self._quality

    @quality.setter
    def quality(self, value: int) -> None:
        if value < 0:
            raise ValueError("Quality cannot be negative")
        if value > 50 and self.name not in [
            "Sulfuras, Hand of Ragnaros",
        ]:
            raise ValueError("Quality cannot be greater than 50")
        self._quality = value
