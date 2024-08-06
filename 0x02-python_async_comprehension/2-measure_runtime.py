#!/usr/bin/env python3
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
"""
"""


async def measure_runtime() -> float:
    start = time.time()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )

    time_total = time.time() - start

    return time_total
