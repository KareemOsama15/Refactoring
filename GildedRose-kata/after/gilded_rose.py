# -*- coding: utf-8 -*-
from typing import List, Dict
from abc import ABC, abstractmethod
from item import Item


class ItemUpdaterInterface(ABC):
    """Item updater interface."""

    @abstractmethod
    def update(self, item: Item) -> None:
        """Update the quality or sell_in of the item."""
        raise NotImplementedError("Subclasses must implement this method")


class SulfurasUpdater(ItemUpdaterInterface):
    """Sulfuras, Hand of Ragnaros updater class."""

    def update(self, item: Item) -> None:
        """Update the quality of the item."""
        pass


class AgedBrieUpdater(ItemUpdaterInterface):
    """Aged Brie updater class."""

    def update(self, item: Item) -> None:
        """Update the quality of the item."""
        self._update_sell_in(item)
        self._update_quality(item)

    def _update_quality(self, item: Item) -> None:
        """Update the quality of the item."""
        if item.quality < 50:
            item.quality += 1

    def _update_sell_in(self, item: Item) -> None:
        """Update the sell_in of the item."""
        item.sell_in -= 1


class BackstagePassesUpdater(ItemUpdaterInterface):
    """Backstage passes updater class."""

    def update(self, item: Item) -> None:
        self._update_sell_in(item)
        self._update_quality(item)

    def _update_quality(self, item: Item) -> None:
        """Update the quality of the item."""
        # Quality Increase when: quality can't be greater than 50 and sell_in is greater than 0
        if item.quality < 50 and item.sell_in > 0:
            if item.sell_in <= 5:
                item.quality += 3
            elif item.sell_in <= 10:
                item.quality += 2
            else:
                item.quality += 1
        # sell_in is less than or equal to 0, quality is set to 0
        elif item.sell_in <= 0:
            item.quality = 0

    def _update_sell_in(self, item: Item) -> None:
        """Update the sell_in of the item."""
        item.sell_in -= 1


class StandardItemsUpdater(ItemUpdaterInterface):
    """Normal item updater class."""

    def update(self, item: Item) -> None:
        """Update the quality of the item."""
        self._update_sell_in(item)
        self._update_quality(item)

    def _update_quality(self, item: Item) -> None:
        """Update the quality of the item."""
        if item.sell_in <= 0:
            item.quality -= 2
        elif item.quality > 0:
            item.quality -= 1

    def _update_sell_in(self, item: Item) -> None:
        """Update the sell_in of the item."""
        item.sell_in -= 1


class ConjuredUpdater(ItemUpdaterInterface):
    """Conjured item updater class."""

    def update(self, item: Item) -> None:
        self._update_sell_in(item)
        self._update_quality(item)

    def _update_quality(self, item: Item) -> None:
        """Update the quality of the item."""
        if item.sell_in <= 0:
            item.quality -= 4

        elif item.quality > 0:
            item.quality -= 2

    def _update_sell_in(self, item: Item) -> None:
        """Update the sell_in of the item."""
        item.sell_in -= 1


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
