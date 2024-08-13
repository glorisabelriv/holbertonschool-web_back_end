#!/usr/bin/env python3
"""
Este módulo proporciona una función que crea un multiplicador.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Toma un número flotante `multiplier` y retorna una función que
    multiplica cualquier número flotante por ese `multiplier`.

    :param multiplier: El número flotante por el cual se
    multiplicará otro número flotante
    :return: Una función que toma un flotante y
    retorna el producto del flotante y `multiplier`
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
