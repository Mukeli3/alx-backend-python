#!/usr/bin/env python3
from typing import Tuple, Union

"""
This module defines a type-annotated function that takes a string and an int
OR float as args and returns a tuple.
The first element of the tuple is a str and the second is the int/float sq
and should be annotated as a float
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key-value pair to a tuple.

  Args:
    k: The key as a string.
    v: The value as an integer or float.

  Returns:
    A tuple containing the key and the square of the value as a float.
  """
    return k, v ** 2
