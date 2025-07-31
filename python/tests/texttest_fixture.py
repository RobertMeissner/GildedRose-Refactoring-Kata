from constants import ITEMS
from gilded_rose import GildedRose, Item


def main(days: int = 2):
    print("OMGHAI!")
    items = inventory()
    gilded_rose = GildedRose(items)
    import sys

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1

    for day in range(days + 1):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in gilded_rose.items:
            print(item)
        print()
        gilded_rose.update_quality()


def inventory() -> list[Item]:
    return [
        Item(name=ITEMS.DEXTERITY_VEST, sell_in=10, quality=20),
        Item(name=ITEMS.AGED_BRIE, sell_in=2, quality=0),
        Item(name=ITEMS.ELIXIR_OF_THE_MONGOOSE, sell_in=5, quality=7),
        Item(name=ITEMS.RAGNAROS, sell_in=0, quality=80),
        Item(name=ITEMS.RAGNAROS, sell_in=-1, quality=80),
        Item(name=ITEMS.TAFKAL_ETC_CONCERT, sell_in=15, quality=20),
        Item(name=ITEMS.TAFKAL_ETC_CONCERT, sell_in=10, quality=49),
        Item(name=ITEMS.TAFKAL_ETC_CONCERT, sell_in=5, quality=49),
        Item(name=ITEMS.CONJURED_MANA_CAKE, sell_in=3, quality=6),  # <-- :O
    ]


if __name__ == "__main__":
    main(2)
