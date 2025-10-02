import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'healthy'}

def test_predict(client):
    data = {'features': [1.0, 2.0, 3.0, 4.0]}
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'id' in json_data
    assert 'prediction' in json_data
    assert 'shape' in json_data
    assert json_data['shape'] == [1, 4]