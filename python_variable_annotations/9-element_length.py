#!/usr/bin/env python3
"""
Este módulo proporciona una función que devuelve una lista
de tuplas con elementos y su longitud.
"""

from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Toma una lista de secuencias y retorna una lista de tuplas.
    Cada tupla contiene un elemento de la lista original y
    la longitud de ese elemento.

    :param lst: Lista de secuencias (como cadenas, listas, etc.)
    :return: Lista de tuplas donde cada tupla contiene
    una secuencia y su longitud
    """
    return [(i, len(i)) for i in lst]
