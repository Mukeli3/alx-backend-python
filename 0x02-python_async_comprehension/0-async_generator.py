#!/usr/bin/env python3
import asyncio
import random
from typing import Generator
"""
This module defines a coroutine that takes no args, loops 10 times, each
time asynchronously wait 1 sec, then yields a random number between 0 and 10
using random module
"""


async def async_generator() -> Generator[float, None, None]:
    """ Yields random numbers with delays asynchronously
    Yields:
         A random number between 0 and 10
    """

    for _ in range(10):  # loop 10 times
        await asyncio.sleep(1)  # wait for 1 sec
        yield random.uniform(0, 10)  # yield a random number between 0 and 10
