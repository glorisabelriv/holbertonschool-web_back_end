#!/usr/bin/env python3
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio Task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
