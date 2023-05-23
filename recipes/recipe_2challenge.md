# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie

1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters.

GET /names
    add: a string representing a name


2. Create Examples as Tests

# GET /names
# With no parameters
# Expected response (200 OK):
"""
Julia, Alice, Karim
"""

# GET /names
# With add: Eddie
# Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""


3. Test-drive the Route

# GET /names
# With no parameters
# Expected response (200 OK):
def test_return_existing_names(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim'

# GET /names
# With add: Eddie
# Expected response (200 OK):
def test_return_existing_names(web_client):
    response = web_client.get('/names', data={'add': 'Eddie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'    



