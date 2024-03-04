import pytest
import geometria as geo

# teste parametrizado (recebe uma lista de valores)
@pytest.mark.parametrize("raio,area",[
    (0, 0), (1, 3.14159), (2, 12.56637061)
])
def test_calc_area_circulo_valores(raio, area):
    assert geo.calc_area_circulo(raio) == pytest.approx(area)

def test_calc_area_circulo():
    assert geo.calc_area_circulo(0) == pytest.approx(0)
    assert geo.calc_area_circulo(1) == pytest.approx(3.14159)
    # assert geo.calc_area_circulo(1) == pytest.approx(3.1416) # fail - baixa precisao
    assert geo.calc_area_circulo(2) == pytest.approx(12.56637061)
