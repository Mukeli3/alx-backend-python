#!/usr/bin/env python3
import asyncio
from typing import List
async_generator = __import__ ('0-async_generator').async_generator
"""
This module defines a coroutine that imports async_generator, takes no args
Collects 10 random numbers using an async comprehensing over async_generator
and returns the random numbers
"""


async def async_comprehension() -> List[float]:
    """
    A Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, and returns the 10 random numbers.

    Returns:
        List[float]: A list of 10 random numbers.
    """

    return [n async for n in async_generator()]
