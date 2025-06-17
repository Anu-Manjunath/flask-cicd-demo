# Imports the app object from your main app (app.py).
from app import app

#What’s happening here:
def test_home():
    client = app.test_client() #test_client() creates a fake browser to test the app.
    response = client.get('/') #client.get('/') simulates visiting the home page.
#assert checks two things:
#The status code is 200 (OK)
#The returned data contains the expected text.

    assert response.status_code == 200
#b"Hello, CI/CD!" means you’re comparing bytes (which Flask returns), not plain text.

    assert b"Hello, CI/CD!" in response.data