#!/usr/bin/env python3

"""
Import async_generator from the previous task and then write
a coroutine called async_comprehension that takes no arguments.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async_comprehension """
    return [n async for n in async_generator()]
