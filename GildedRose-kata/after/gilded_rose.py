# -*- coding: utf-8 -*-
from typing import List


class Item:
    """Item class."""

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name: str = name
        self.sell_in: int = sell_in
        self._quality: int = quality

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


class GildedRose(object):
    """Gilded Rose class."""

    def __init__(self, items: List[Item]) -> None:
        """Initialize the Gilded Rose class."""
        self.items: List[Item] = items

    def update_quality(self) -> None:
        """
        Update the quality of the items.
        """

        for item in self.items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
