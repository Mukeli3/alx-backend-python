#!/usr/bin/env python3
from typing import List
"""
This module defines a type-annotated function, sum_list which takes a
list of floats, input_list as argument and returns their sum as float
"""


def sum_list(input_list: List[float]) -> float:
    """ Returns list sum as a float
    Args:
        input_list - the list
    Returns:
        the list sum as a float
    """
    return sum(input_list)
