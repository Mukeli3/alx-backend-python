#!/usr/bin/env python3
from typing import List, Tuple

"""
This module defines a an appropriately annotated function parameters
and return values
"""


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Args:
        lst (list): A list of sequences (e.g., strings).

    Returns:
        list: A list of tuples where each tuple contains a sequence from
        the input list and its length.
    """
    return [(i, len(i)) for i in lst]
