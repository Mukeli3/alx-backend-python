#!/usr/bin/env python3
from typing import List, Tuple, Sequence

"""
This module defines a an appropriately annotated function parameters
and return values
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst (list): A list of sequences (e.g., strings).

    Returns:
        list: A list of tuples where each tuple contains a sequence from
        the input list and its length.
    """
    return [(i, len(i)) for i in lst]
