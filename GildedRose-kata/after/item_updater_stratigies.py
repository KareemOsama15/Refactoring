from item_update_interface import ItemUpdaterInterface
from item import Item


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
