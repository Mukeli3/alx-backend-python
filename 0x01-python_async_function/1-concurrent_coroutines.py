#!/usr/bin/env python3
"""
This module defines an async routine written by importing from the previous
file, takes in 2 int args. Previous routine is spawned n times with the
specified delay.
It returns the list of all delays(float values) in ascending order.
sort() is not used due to concurrency
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with specified max_delay.

    Args:
        n: The number of times to call wait_random.
        max_delay: The maximum delay for each wait_random call.

    Returns:
        A list of the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]  # creating async tasks
    # using list comprehension, _ indicates that the loop variable is not used
    res = await asyncio.gather(*tasks)  # start multiple tasks at once and
    # wait for all of them to finish before collecting their outputs
    return sorted(res)  # sorted(), creates a new sorted list from an iterable
    # (lists, tuples nk), doesn't modify original iterable
