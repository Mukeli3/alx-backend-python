#!/usr/bin/env python3
import asyncio
from typing import List
async_generator = import('0-async_generator').async_generator
"""
This module defines a coroutine that imports async_generator, takes no args
Collects 10 random numbers using an async comprehensing over async_generator
and returns the random numbers
"""

async def async_comprehension() -> List[float]:
    return [n async for n in async_generator()]
