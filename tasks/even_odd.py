__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    chet = 0
    nechet = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            nechet += arr[i]
        else:
            chet += arr[i]
    return float(chet / nechet)

