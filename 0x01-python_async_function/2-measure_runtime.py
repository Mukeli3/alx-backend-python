#!/usr/bin/env python3
"""
This module defines a function with integers as args that measures the total
execution time for a function and returns a float. time module is used to
measure an approximate elapsed time
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    start = time.perf_counter() # start time
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter() #end time

    total_time = stop - start # total time taken
    av_time = total_time / n # average time

    return av_time
