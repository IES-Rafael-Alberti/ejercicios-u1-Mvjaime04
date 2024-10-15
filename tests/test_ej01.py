import pytest 
from src.ej01_def import generar_cadena

def test_generar_cadena():
    assert generar_cadena("Juan")== "hola Juan"
    assert generar_cadena("Maria")== "hola Maria"
    assert generar_cadena("")== "hola "
    assert generar_cadena("123")== "hola 123"


