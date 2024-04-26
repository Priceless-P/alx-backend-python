#!/usr/bin/env python3
"""Multiple coroutines at the same time with async"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns `wait_random` n times with the specified max_delay"""
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for _ in range(n):
            task = tg.create_task(wait_random(max_delay))
            tasks.append(task)

    return sorted([task.result() for task in tasks])
