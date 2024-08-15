#!/usr/bin/env python3
import asyncio
import random

async def esperar_aleatorio(max_delay: int = 10) -> float:
    """
    Corrutina asincrónica que espera un tiempo aleatorio entre 0 y max_delay segundos
    y devuelve ese tiempo.

    :param max_delay: Tiempo máximo de espera (en segundos)
    :return: El tiempo que se esperó, como un número flotante
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
