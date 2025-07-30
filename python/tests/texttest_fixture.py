from src.constants import ITEMS #AGED_BRIE, CONJURED_MANA_CAKE, DEXTERITY_VEST, ELIXIR_OF_THE_MONGOOSE, RAGNAROS, TAFKAL_ETC_CONCERT
from src.gilded_rose import GildedRose, Item


def main():
    print("OMGHAI!")
    items = [
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
    days = 2
    import sys

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print()
        GildedRose(items).update_quality()


if __name__ == "__main__":
    main()
