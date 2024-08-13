#!/usr/bin/env python3
"""
Proporciona una función para sumar una lista de enteros y flotantes.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Suma todos los números en una lista de enteros y flotantes
    y devuelve el resultado como un flotante.

    :param mxd_lst: Lista que contiene enteros y flotantes
    :return: La suma de todos los números en la lista como un flotante
    """
    return sum(mxd_lst)
