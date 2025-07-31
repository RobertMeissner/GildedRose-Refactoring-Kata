# from src.constants import AGED_BRIE, CONJURED_MANA_CAKE, DEXTERITY_VEST, ELIXIR_OF_THE_MONGOOSE, RAGNAROS, TAFKAL_ETC_CONCERT

from constants import ITEMS


# DO NOT ALTER!
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemManipulator(Item):
    @classmethod
    def from_item(cls, item: Item, max_quality: int = 50) -> "ItemManipulator":
        return cls(name=item.name, sell_in=item.sell_in, quality=item.quality, max_quality=max_quality)

    def __init__(self, name, sell_in, quality, max_quality: int = 50):
        super().__init__(name, sell_in, quality)
        self._max_quality: int = max_quality

    @property
    def max_quality(self) -> int:
        return self._max_quality

    @max_quality.setter
    def max_quality(self, value: int) -> None:
        if value < 0:
            raise ValueError("max_quality cannot be negative")
        self._max_quality = value

    def update(self):
        # cycles through manipulators, e.g.,
        pass

    def reduce_sell_in(self, amount: int = 1) -> "ItemManipulator":
        self.sell_in -= amount
        return self

    def __repr__(self):
        return super().__repr__()


class GildedRose:
    def __init__(self, items):
        self.items = [ItemManipulator.from_item(item) for item in items]

    @property
    def items(self) -> list[Item]:
        return self._items

    @items.setter
    def items(self, value: list[Item]) -> None:
        self._items = value

    def change_quality(self, item, value) -> Item:
        item.quality += value
        return item

    def update_quality(self):
        for item in self.items:
            # print(item.name, item.name == ITEMS.AGED_BRIE)
            match item.name:
                case ITEMS.RAGNAROS:
                    pass
                case ITEMS.AGED_BRIE:
                    # print(item.sell_in)
                    item.sell_in -= 1
                    # print(item.sell_in)
                    if item.sell_in < 0:
                        item.quality += 2
                    else:
                        item.quality += 1
                    item.quality = min(50, item.quality)
                case ITEMS.TAFKAL_ETC_CONCERT:
                    item.sell_in -= 1
                    if item.sell_in < 0:
                        item.quality = 0
                    elif item.sell_in < 10:
                        if item.sell_in < 5:
                            item.quality += 3
                        else:
                            item.quality += 2
                    else:
                        item.quality += 1

                    item.quality = min(50, item.quality)
                case ITEMS.DEXTERITY_VEST:
                    item.sell_in -= 1
                    if item.sell_in < 0:
                        item.quality -= 2
                    else:
                        item.quality -= 1

                case ITEMS.CONJURED_MANA_CAKE:
                    item.sell_in -= 1
                    if item.sell_in < 0:
                        item.quality -= 4
                    else:
                        item.quality -= 2
                case ITEMS.ELIXIR_OF_THE_MONGOOSE:
                    item.sell_in -= 1
                    if item.sell_in < 0:
                        item.quality = 0
                    else:
                        item.quality -= 1
                case _:
                    item.quality -= 1
                    item.sell_in -= 1

            item.quality = max(0, item.quality)

    def update_quality_old(self):
        for item in self.items:
            # shelf life not passed yet
            if item.name != ITEMS.AGED_BRIE and item.name != ITEMS.TAFKAL_ETC_CONCERT:
                if item.quality > 0 and item.name != ITEMS.RAGNAROS:
                    item.quality = item.quality - 1
            elif item.quality < 50:
                item.quality = item.quality + 1
                if item.name == ITEMS.TAFKAL_ETC_CONCERT:
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                    if item.sell_in < 6:
                        item.quality = item.quality + 1

            # legendary items have no shelf life
            if item.name != ITEMS.RAGNAROS:
                item.sell_in = item.sell_in - 1

            # shelf life passed
            if item.sell_in < 0:
                if item.name != ITEMS.AGED_BRIE:
                    if item.name != ITEMS.TAFKAL_ETC_CONCERT:
                        if item.quality > 0 and item.name != ITEMS.RAGNAROS:
                            item.quality = item.quality - 1
                    else:
                        item.quality = 0
                elif item.quality < 50:
                    item.quality = item.quality + 1

            # legendary items have higher quality
            if item.name == ITEMS.RAGNAROS:
                item.quality = min(80, item.quality)
            else:
                item.quality = min(50, item.quality)
