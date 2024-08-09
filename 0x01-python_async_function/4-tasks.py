#!/usr/bin/env python3
"""
This module defines a function defined by altering wait_n code
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ function returns the task """
    result = await asyncio.gather(
         *[task_wait_random(max_delay) for _ in range(n)]
         )
    return sorted(result)
