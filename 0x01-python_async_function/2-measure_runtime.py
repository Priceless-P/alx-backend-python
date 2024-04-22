#!/usr/bin/python3
"""Measure the runtime"""
import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time
    for wait_n(n, max_delay)"""

    initial_time = time()
    await asyncio.run(wait_n(n, max_delay))
    return (time() - initial_time) / n
