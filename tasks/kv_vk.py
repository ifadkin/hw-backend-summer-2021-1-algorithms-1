from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:

    mydict_new = dict(zip(d.values(), d.keys()))
    return  mydict_new

def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    result = {}
    for key, value in d.items():
        if not result.get(value):
            result[value] = key
        else:
            if isinstance(result[value], tuple):
                result[value] += (key,)
            else:
                result[value] = (result[value],) + (ey,)
    return result

