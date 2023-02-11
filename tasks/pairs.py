from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    short_len = min(len(arr1), len(arr2))
    res = []
    for i in range(short_len):
        res.append((arr1[i], arr2[i]))
    return res

