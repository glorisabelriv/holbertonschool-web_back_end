#!/usr/bin/env python3
"""
Este módulo proporciona una función para sumar una lista de números flotantes.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Suma todos los números flotantes en una lista y devuelve el resultado.

    :param input_list: Lista de números flotantes
    :return: La suma de todos los números en la lista como un flotante
    """
    return sum(input_list)
