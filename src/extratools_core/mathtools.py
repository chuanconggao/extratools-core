from collections import Counter
from collections.abc import Iterable
from math import inf, log2


def safediv(a: float, b: float) -> float:
    """
    Safely divide float even when by 0, by returning infinity with proper sign.

    Parameters
    ----------
    a : float
    b : float

    Returns
    -------
    float
        Result of `a / b`
    """

    return inf * a if b == 0 else a / b


def entropy[T](data: Iterable[T]) -> float:
    """
    Compute the entropy of data (as collection of items).

    Parameters
    ----------
    data : float
        Collection (as `Iterable`) of items

    Returns
    -------
    float
        Value of entropy
    """

    counter: Counter[T] = Counter(data)
    total: int = sum(counter.values())

    return -sum(
        p * log2(p)
        for p in (
            curr / total
            for curr in counter.values()
        )
    )
