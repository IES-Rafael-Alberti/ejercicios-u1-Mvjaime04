import pytest
from src.ej11_def import sumar_enteros

def test_sumar_enteros():
    assert sumar_enteros(5) == "La suma de los enteros desde 1 hasta 5 es: 15"
    assert sumar_enteros(10) == "La suma de los enteros desde 1 hasta 10 es: 55"
    assert sumar_enteros(1) == "La suma de los enteros desde 1 hasta 1 es: 1"
    assert sumar_enteros(0) == "Por favor, introduce un número entero positivo."
    assert sumar_enteros(-3) == "Por favor, introduce un número entero positivo."