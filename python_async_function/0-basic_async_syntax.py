#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random time between 0 and max_delay seconds
    and returns that time.

    :param max_delay: Maximum wait time (in seconds)
    :return: The time waited, as a float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
