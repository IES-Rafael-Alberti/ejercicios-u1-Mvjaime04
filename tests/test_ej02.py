import pytest 
from src.ej02_def import genera_importe

def test_genera_importe():
    assert genera_importe(100) == "importe total: 100"
    assert genera_importe(0) == "importe total: 0"
    assert genera_importe(50) == "importe total: 50"
    assert genera_importe(1234.56) =="importe total: 1234.56"