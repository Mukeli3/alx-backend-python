#!/usr/bin/env python3
from typing import List
"""
This module defines a function which takes a list of floats as argument
and retuns their sum as float
"""


def sum_list(input_list: List[float]) -> float:
    """
    Args:
       input_list - list
    Return:
       sum as a float
    """
    return sum(input_list)
