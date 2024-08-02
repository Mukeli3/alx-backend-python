#!/usr/bin/env python3
from typing import Callable
"""
This module defines a type-annotated function that takes a float as arg
and returns a function that multiplies a float by the arg
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

  Args:
    multiplier: The factor to multiply by.

  Returns:
    A function that multiplies a float by the given multiplier.
    """
    def inner(x: float) -> float:
        return x * multiplier
    return inner
