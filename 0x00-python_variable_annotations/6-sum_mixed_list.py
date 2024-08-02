#!/usr/bin/env python3
from typing import List, Union

"""
This module defines a type-annotated function which takes a list of ints
and floats and returns their sum as a float
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_lst (list): A list

    Returns:
        sum of floats
    """
    return sum(mxd_lst)
