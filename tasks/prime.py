__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    return len([i for i in range(1, number + 1) if number % i == 0]) == 2
