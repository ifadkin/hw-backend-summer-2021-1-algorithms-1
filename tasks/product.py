from typing import Any
import itertools

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    total = arr1 + arr2
    res = list(itertools.combinations(total, 2))
    del res[res.index(tuple(arr1))]
    del res[res.index(tuple(arr2))]
    return res

