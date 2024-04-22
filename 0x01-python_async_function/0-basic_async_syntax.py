#!/usr/bin/env python3
"""Basic Async function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float | int:
    """Waits for a random delay between 0 and max_delay"""
    delay_num = random.uniform(0, max_delay)
    await asyncio.sleep(delay_num)
    return delay_num
