from src.constants import AGED_BRIE, CONJURED_MANA_CAKE, DEXTERITY_VEST, ELIXIR_OF_THE_MONGOOSE, RAGNAROS, TAFKAL_ETC_CONCERT


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == RAGNAROS:
                pass
            elif item.name == AGED_BRIE:
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality += 2
                else:
                    item.quality += 1
                item.quality = min(50, item.quality)
            elif item.name == TAFKAL_ETC_CONCERT:
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
            elif item.name == DEXTERITY_VEST:
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality -= 2
                else:
                    item.quality -= 1

            elif item.name == CONJURED_MANA_CAKE:
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality -= 4
                else:
                    item.quality -= 2
            elif item.name == ELIXIR_OF_THE_MONGOOSE:
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality = 0
                else:
                    item.quality -= 1
            else:
                item.quality -= 1
                item.sell_in -= 1

            item.quality = max(0, item.quality)

    def update_quality_old(self):
        for item in self.items:
            # shelf life not passed yet
            if item.name != AGED_BRIE and item.name != TAFKAL_ETC_CONCERT:
                if item.quality > 0 and item.name != RAGNAROS:
                    item.quality = item.quality - 1
            elif item.quality < 50:
                item.quality = item.quality + 1
                if item.name == TAFKAL_ETC_CONCERT:
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                    if item.sell_in < 6:
                        item.quality = item.quality + 1

            # legendary items have no shelf life
            if item.name != RAGNAROS:
                item.sell_in = item.sell_in - 1

            # shelf life passed
            if item.sell_in < 0:
                if item.name != AGED_BRIE:
                    if item.name != TAFKAL_ETC_CONCERT:
                        if item.quality > 0 and item.name != RAGNAROS:
                            item.quality = item.quality - 1
                    else:
                        item.quality = 0
                elif item.quality < 50:
                    item.quality = item.quality + 1

            # legendary items have higher quality
            if item.name == RAGNAROS:
                item.quality = min(80, item.quality)
            else:
                item.quality = min(50, item.quality)


# DO NOT ALTER!
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
