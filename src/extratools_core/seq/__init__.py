from collections.abc import Callable, Iterable
from itertools import groupby, repeat
from typing import Any

from toolz import itertoolz

from ..typing import Comparable
from .common import iter_to_seq  # noqa: F401


def sorted_by_rank[T](
    data: Iterable[T],
    ranks: Iterable[Comparable],
    *,
    _reverse: bool = False,
) -> list[T]:
    return [
        v
        for v, _ in sorted(
            zip(data, ranks, strict=True),
            key=lambda x: x[1],
            reverse=_reverse,
        )
    ]


def compress[T](
    data: Iterable[T],
    key: Callable[[T], Any] | None = None,
) -> Iterable[tuple[T, int]]:
    for k, g in groupby(data, key=key):
        yield (k, itertoolz.count(g))


def decompress[T](data: Iterable[tuple[T, int]]) -> Iterable[T]:
    for k, n in data:
        yield from repeat(k, n)
