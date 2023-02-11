from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    regul = re.split(r'\W+', text.lstrip().rstrip())
    lens = []
    for i in range(len(regul)):
        if regul[i].isalpha():
            lens.append(len(regul[i]))
    if len(lens) != 0:
        return regul[lens.index(min(lens))], regul[lens.index(max(lens))], lens, regul
    else:
        return None, None

