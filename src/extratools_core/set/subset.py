from collections.abc import Iterable
from collections.abc import Set as AbstractSet

from ..seq.subseq import enumerate_subseqs_with_gaps


def enumerate_subsets[T](a: AbstractSet[T]) -> Iterable[AbstractSet[T]]:
    return map(frozenset, enumerate_subseqs_with_gaps(a))
