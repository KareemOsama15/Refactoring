# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class ItemTest(unittest.TestCase):

    def test_item_quality(self):
        item = Item("Aged Brie", 2, 0)
        self.assertEqual(0, item.quality)

    def test_item_sell_in(self):
        item = Item("Aged Brie", 2, 0)
        self.assertEqual(2, item.sell_in)

    def test_item_name(self):
        item = Item("Aged Brie", 2, 0)
        self.assertEqual("Aged Brie", item.name)

    def test_item_quality_is_negative(self):
        with self.assertRaises(ValueError, msg="Quality cannot be negative"):
            item = Item("Aged Brie", 2, -1)

    def test_item_quality_is_50(self):
        item = Item("Aged Brie", 2, 50)
        with self.assertRaises(ValueError, msg="Quality cannot be greater than 50"):
            item.quality = 51

    def test_sulfras_quality_more_than_50(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        self.assertEqual(80, item.quality)

    def test_item_quality_more_than_50_in_instantiation(self):
        with self.assertRaises(ValueError, msg="Quality cannot be greater than 50"):
            item = Item("Aged Brie", 2, 51)

    def test_normal_item_quality_more_than_50(self):
        item = Item("Elixir of the Mongoose", 2, 50)
        with self.assertRaises(ValueError, msg="Quality cannot be greater than 50"):
            item.quality = 55


class GildedRoseTest(unittest.TestCase):

    def test_aged_brie_quality_decreased_by_1(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_sell_in_decreased_by_1(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)

    def test_aged_brie_quality_equal_to_50(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_aged_brie_quality_when_sell_in_less_than_0(self):
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_quality_not_changed(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_sell_in_not_changed(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)

    def test_backstage_passes_quality_increased_by_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_quality_increased_by_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_quality_increased_by_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_quality_when_sell_in_is_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_passes_quality_when_sell_in_is_negative(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_passes_sell_in_decreased_by_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_backstage_passes_quality_equal_to_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_standard_items_quality_decreased_by_1(self):
        items = [Item("Elixir of the Mongoose", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_standard_items_sell_in_decreased_by_1(self):
        items = [Item("Elixir of the Mongoose", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)


if __name__ == "__main__":
    unittest.main()
