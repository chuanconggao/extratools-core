from collections.abc import Callable, Iterable, Sequence
from itertools import chain

from . import iter_to_seq


def best_subseq[T](
    a: Iterable[T],
    score_func: Callable[[Iterable[T]], float],
) -> Sequence[T]:
    s: Sequence = iter_to_seq(a)

    return max(
        chain([[]], (
            s[i:j]
            for i in range(len(s))
            for j in range(i + 1, len(s) + 1)
        )),
        key=score_func,
    )


def best_subseq_with_gaps[T](
    a: Iterable[T],
    score_func: Callable[[Iterable[T]], float],
) -> Sequence[T]:
    def find_rec(alen: int) -> tuple[
        # Score of best subseq
        float,
        # Best subseq
        list[T],
    ]:
        """
        To find the best subseq of `a[:alen]`
        """

        if alen == 0:
            return (score_func([]), [])

        prev_score: float
        prev_seq: list[T]
        prev_score, prev_seq = find_rec(alen - 1)

        curr_seq: list[T] = [*prev_seq, s[alen - 1]]

        return max(
            # Prefers current one which is longer, if it has same score of previous one
            (score_func(curr_seq), curr_seq),
            (prev_score, prev_seq),
            key=lambda x: x[0],
        )

    s: Sequence[T] = iter_to_seq(a)
    return find_rec(len(s))[1]
