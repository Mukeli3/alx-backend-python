#!/usr/bin/env python3
"""
This module defines a function that takes a float as argument and returns
the float floor
"""


def floor(n: float) -> int:
    """
    Args:
        n (float): A float.

    Returns:
        the floor of the float
    """
    if n >= 0:
        return int(n)

    if int(n) != n:
        return int(n) - 1

    return int(n)
