#!/usr/bin/env python3
"""Multiple coroutines at the same time with async"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns `wait_random` n times with the specified max_delay"""
    task = [task_wait_random(max_delay) for _ in range(n)]
    tasks = [await t for t in asyncio.as_completed(task)]
    return tasks
