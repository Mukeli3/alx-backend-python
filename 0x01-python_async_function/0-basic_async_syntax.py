#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that takes in an integer
argument, with a default value of 10, that waits for a random delay between
0 and the int argument secs and eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Coroutine waits for a random delay and returns the actual delay

    Args:
        max_delay: max delay in secs (10 - default value)

    Returns:
        The actual delay, in sec
    """
    #  generate random delay
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)  # wait for delay
    return delay  # return delay value
