#!/usr/bin/env python3
import asyncio
import random


async def async_generator():
    """
    Corrutina asincrónica que genera 10 números aleatorios entre 0 y 10,
    esperando 1 segundo entre cada generación.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
