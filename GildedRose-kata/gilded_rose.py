# -*- coding: utf-8 -*-
from typing import List


class Item:
    """Item class."""

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name: str = name
        self.sell_in: int = sell_in
        self.quality: int = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def _update_field(self, field_name: str, value: int, operator: str) -> None:
        """Update the value of a field based on the operator."""
        if operator == "+":
            setattr(self, field_name, getattr(self, field_name) + value)
        elif operator == "-":
            setattr(self, field_name, getattr(self, field_name) - value)


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
                        item._update_field("quality", 1, "-")
            else:
                if item.quality < 50:
                    item._update_field("quality", 1, "+")
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item._update_field("quality", 1, "+")
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item._update_field("quality", 1, "+")
            if item.name != "Sulfuras, Hand of Ragnaros":
                item._update_field("sell_in", 1, "-")
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item._update_field("quality", 1, "-")
                    else:
                        item._update_field("quality", 1, "-")
                else:
                    if item.quality < 50:
                        item._update_field("quality", 1, "+")
