# ########################################
# File: countries_test.py
# ########################################
import pytest
from countries_api import app

@pytest.fixture
def client():
    """ 
    - fixture: inicializa dependências de contexto do teste (framework flask)
    - gera uma instancia do flask para ser usada nas 
     requisições feitas em cada teste do backend (api) """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_country_name_valid(client):
    """ test 200 - retorno com sucesso """
    """ client: funcao inicializada em @pytest.fixture """
    response = client.get('/get_country_name?iso_code=CA')
    assert response.status_code == 200 # == sucesso
    data = response.get_json()
    assert 'country_name' in data
    assert data['country_name'] == 'Canada'

def test_get_country_name_invalid(client):
    # Assuming 'ZZ' is an invalid ISO code
    response = client.get('/get_country_name?iso_code=ZZ')  
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Country not found'

def test_get_country_name_missing_iso_code(client):
    response = client.get('/get_country_name')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'ISO code not provided'

def test_api_rest_countries():
    """ TODO: implementar teste da rota """
    ...
