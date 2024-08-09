#!/usr/bin/env python3
"""
This module defines a coroutine measure_routine that executes
async_comprehension, imported from previous file, four times using
asyncio.gather, it measures and returns the total runtime
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime to execute async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    """
    start = time.time()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )

    time_total = time.time() - start

    return time_total
