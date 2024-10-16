import pytest
from src.ej05_def2 import calcula_precio, calcula_importe  
def test_calcula_precio():
    assert calcula_precio(21, 100) == "El importe del articulo con IVA=21.00 es de 100.00 ."
    assert calcula_precio(10, 50) == "El importe del articulo con IVA=10.00 es de 50.00 ."

def test_calcula_importe():
    assert calcula_importe(100, 0.21) == 21.0
    assert calcula_importe(50, 0.10) == 5.0
    assert calcula_importe(200, 0.0) == 0.0