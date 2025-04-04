from collections import defaultdict
from collections.abc import Mapping, Sequence


def invert[KT, VT](d: Mapping[KT, VT]) -> Mapping[VT, KT]:
    return {
        v: k
        for k, v in d.items()
    }


def invert_safe[KT, VT](d: Mapping[KT, VT]) -> Mapping[VT, Sequence[KT]]:
    r: defaultdict[VT, list[KT]] = defaultdict(list)

    for k, v in d.items():
        r[v].append(k)

    return r
