# 20250730

First read. Confusing. Structure unclear. Currently no metrics what needs to be done, what is off, what is good.

Starting with uv and pre-commit to get coverage and a few metrics

pre-commit
- ruff: 44 errors
- whitespaces and end of files: a few
- pytest


radon cc:
- C 1:0 GildedRose - C (11)
- C 34:0 Item - A (2)

Main function has bad maintainability

Average complexity: A (4.3)
- could be better

Tests:
- fail, of course


## Reading task

- Items property stays fixed. No change allowed
- Quality changes depending on the item type, completely item related
  - Delta Quality may depend on SellIn value
- new item needs to be added
- 0 <= Quality <= 50

Mypy: 25 errors in all files

- basically no typing
- many string literals, no constants

First time I see [approvaltests](https://pypi.org/project/approvaltests/)
Copying what is approved in approved_files folder solves both tests for now

tests import fixture from root and execute the main function.

coverage: 100% for gilded_rose.py - at least that is good. But: the test is inunderstandable.

## Restructuring

created src and moved files around
- updated imports

found: "from gilded_rose import *"
- removed and replaced by explicit call

approvaltests kind of flaky: a single new line caused it to fail

How to go about?
1. Extract constants for clarity
2. Refactor too many if's in update_quality
3. Update test function, mostly the fixture, that confuses a lot

- Why this order?
  - Tests run and cover the current function
  - That includes the wicked ... ups*
  - helps me find clarity for 3.

*ups: noticed, the test itself is wrong, e.g., no handling for **Conjured** items -_-

Approval test generates 2 newline - but ruff removes 1 -_-

update_quality checks only what something is NOT, confuses, logic bizarre

Refactoring shows double logic, confusing structure.
update_quality checks value based, not type based, i.e., it decides depending on sell_in and quality, not depending on name, which == type/item class


quality = quality(name, sell_in)
- sell_in normally set BEFORE quality

Have the idea something must be mutated or chained
- e.g. all items are reduced in sell_in, depending on name a multiplier to the reduction of quality, quality floored