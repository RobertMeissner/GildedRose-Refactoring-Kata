import pytest
from gilded_rose import GildedRose, Item


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].name == "foo"


@pytest.mark.parametrize(
    "name,sell_in,quality,expected_name",
    [
        ("foo", 0, 0, "foo"),
        ("Aged Brie", 2, 0, "Aged Brie"),
        ("Elixir of the Mongoose", 5, 7, "Elixir of the Mongoose"),
        ("Sulfuras, Hand of Ragnaros", 0, 80, "Sulfuras, Hand of Ragnaros"),
        ("Backstage passes to a TAFKAL80ETC concert", 15, 20, "Backstage passes to a TAFKAL80ETC concert"),
    ],
)
def test_item_name_unchanged_after_update(name, sell_in, quality, expected_name):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].name == expected_name


@pytest.mark.parametrize(
    "name,sell_in,quality,expected_sell_in",
    [
        #  ("foo", 0, 0, -1),
        ("Aged Brie", 2, 0, 1),
        # ("Elixir of the Mongoose", 5, 7, 4),
        # ("Sulfuras, Hand of Ragnaros", 0, 80, -1),
        # ("Backstage passes to a TAFKAL80ETC concert", 15, 20, 14),
    ],
)
def test_item_sell_in_changed_after_update(name, sell_in, quality, expected_sell_in):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == expected_sell_in
