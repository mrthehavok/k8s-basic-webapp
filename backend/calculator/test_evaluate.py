import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_evaluate_valid_simple(client):
    """Test valid simple expression: 2+3*4"""
    response = client.get('/api/evaluate?expr=2%2B3*4')
    assert response.status_code == 200
    assert response.json == {'result': 14.0}

def test_evaluate_valid_functions(client):
    """Test valid expression with functions: sqrt(16)+log(100,10)"""
    response = client.get('/api/evaluate?expr=sqrt(16)%2Blog(100,10)')
    assert response.status_code == 200
    assert response.json['result'] == 6.0

def test_evaluate_valid_parentheses(client):
    """Test valid expression with parentheses: (3+2)^2"""
    response = client.get('/api/evaluate?expr=(3%2B2)**2')
    assert response.status_code == 200
    assert response.json == {'result': 25.0}

def test_evaluate_division_by_zero(client):
    """Test division by zero: 5/0"""
    response = client.get('/api/evaluate?expr=5/0')
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Division by zero'

def test_evaluate_invalid_syntax(client):
    """Test invalid syntax: 2*(3+())"""
    response = client.get('/api/evaluate?expr=2*(3%2B())')
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid expression syntax'

def test_evaluate_invalid_function(client):
    """Test calling an undefined function"""
    response = client.get('/api/evaluate?expr=undefined(5)')
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid expression syntax'

def test_evaluate_no_expr(client):
    """Test request with no expression"""
    response = client.get('/api/evaluate')
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == "Missing 'expr' parameter"

def test_evaluate_disallowed_symbols(client):
    """Test expression with disallowed symbols"""
    response = client.get('/api/evaluate?expr=x%2B5')
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid expression syntax'