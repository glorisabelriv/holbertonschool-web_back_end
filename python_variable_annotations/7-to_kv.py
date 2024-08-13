#!/usr/bin/env python3
"""
Proporciona una función que retorna una tupla con una cadena
y el cuadrado de un número.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Toma un string y un número (entero o flotante) y retorna una tupla.

    El primer elemento de la tupla es el string `k`.
    El segundo elemento es el cuadrado del número `v`,
    anotado como un flotante.

    :param k: Una cadena de texto
    :param v: Un número entero o flotante
    :return: Una tupla donde el primer elemento es `k` y
    el segundo es `v` al cuadrado
    """
    return (k, float(v ** 2))
