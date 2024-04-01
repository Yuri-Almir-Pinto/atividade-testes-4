# ########################################
# File: countries_test.py
# ########################################


import pytest
from countries_api import app

# fixture: inicializa dependências de contexto do teste (framework flask)
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_country_name_valid(client):
    """ client: funcao inicializada em @pytest.fixture """
    response = client.get('/get_country_name?iso_code=US')
    assert response.status_code == 200
    data = response.get_json()
    assert 'country_name' in data
    assert data['country_name'] == 'United States'

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
