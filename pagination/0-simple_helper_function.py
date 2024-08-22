#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calcula el rango de índices para una paginación dada.

    :param page: Número de la página (comenzando en 1)
    :param page_size: Tamaño de la página
    :return: Una tupla que contiene el índice de inicio y el índice de fin
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
