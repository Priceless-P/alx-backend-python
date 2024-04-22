#!/usr/bin/python3
"""Multiple coroutines at the same time with async"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns `wait_random` n times with the specified max_delay"""
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for _ in range(n):
            task = tg.create_task(task_wait_random(max_delay))
            tasks.append(task)

    return [task.result() for task in tasks]
