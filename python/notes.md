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
