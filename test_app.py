from app import app

def test_greet():
    tester = app.test_client()
    response = tester.get('/greet?name=Bulls')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Bulls!"}

