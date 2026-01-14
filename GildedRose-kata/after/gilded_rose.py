# -*- coding: utf-8 -*-
from typing import List, Dict
from item import Item
from item_update_interface import ItemUpdaterInterface
from item_updater_stratigies import (
    SulfurasUpdater,
    AgedBrieUpdater,
    BackstagePassesUpdater,
    ConjuredUpdater,
    StandardItemsUpdater,
)


class GildedRose(object):
    """Gilded Rose class."""

    def __init__(self, items: List[Item]) -> None:
        """Initialize the Gilded Rose class."""
        self.items: List[Item] = items
        self.updaters: Dict[str, ItemUpdaterInterface] = {
            "Sulfuras, Hand of Ragnaros": SulfurasUpdater(),
            "Aged Brie": AgedBrieUpdater(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesUpdater(),
            "Conjured Mana Cake": ConjuredUpdater(),
        }

    def update_quality(self) -> None:
        """
        Update the quality of the items.
        """
        for item in self.items:
            updater = self.updaters.get(item.name)
            if updater:
                updater.update(item)
            else:
                StandardItemsUpdater().update(item)
