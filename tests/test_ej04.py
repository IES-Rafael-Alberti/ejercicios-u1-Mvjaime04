import pytest
from src.ej04_def2 import grados_celsius

def test_grados_celsius():
    assert grados_celsius(32) == 0.0  
    assert grados_celsius(212) == 100.0  
    assert grados_celsius(98.6) == 37.0  
    assert grados_celsius(0) == -17.77777777777778  
    assert grados_celsius(-40) == -40.0