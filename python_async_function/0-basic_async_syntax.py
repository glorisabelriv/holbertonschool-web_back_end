#!/usr/bin/env python3

"""
    Asynchronous coroutine that waits for a random time between
    0 and max_delay seconds
    and returns that time.

    :param max_delay: Maximum wait time (in seconds), default is 10
    :return: The time waited, as a float
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait random """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
