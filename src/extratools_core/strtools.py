from collections.abc import Iterable

from .iter import iter_to_grams
from .seq.subseq import common_subseq


def str_to_grams(
    s: str,
    *,
    n: int,
    pad: str = '',
) -> Iterable[str]:
    if len(pad) > 1:
        raise ValueError

    for c in iter_to_grams(s, n=n, pad=pad or None):
        yield ''.join(c)


def common_substr(a: str, b: str) -> str:
    return ''.join(common_subseq(a, b))
