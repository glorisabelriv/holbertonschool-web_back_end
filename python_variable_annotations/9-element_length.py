#!/usr/bin/env python3
"""
Este módulo proporciona una función que devuelve una lista
de tuplas con elementos y su longitud.
"""

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Toma un iterable de secuencias y retorna una lista de tuplas.
    Cada tupla contiene un elemento del iterable original y
    la longitud de ese elemento.

    :param lst: Un iterable de secuencias (como cadenas, listas, etc.)
    :return: Lista de tuplas donde cada tupla contiene
    una secuencia y su longitud
    """
    return [(i, len(i)) for i in lst]
