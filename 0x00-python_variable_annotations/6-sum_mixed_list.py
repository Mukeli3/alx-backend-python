#!/usr/bin/env python3
"""
This module defines a type-annotated function which takes a list of integers
and floats as arguments and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_lst (list): A list of integers and floats

    Returns:
        sum of floats
    """
    return sum(mxd_lst)
