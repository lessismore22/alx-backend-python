#!/usr/bin/env python3
"""Task 9's module
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(1st: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the length of a list of sequences.
    """

    return [(i, len(i)) for i in 1st]
