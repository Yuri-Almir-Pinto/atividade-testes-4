import pytest
import geometria as geo

def test_calc_area_circulo():
    assert geo.calc_area_circulo(0) == pytest.approx(0)
    assert geo.calc_area_circulo(1) == pytest.approx(3.14159)
    # assert geo.calc_area_circulo(1) == pytest.approx(3.1416) # fail - baixa precisao
    assert geo.calc_area_circulo(2) == pytest.approx(12.56637061)
