Test-drive a new route POST /sort-names which receives a list of names (as a comma-separated string) and return the same list, sorted in alphabetical order.

# Request:
POST http://localhost:5000/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe

1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters.

POST /sort-names
    names: a string of comma-separated names (no spaces)


2. Create Examples as Tests

# POST /sort-names
# With names=Joe,Alice,Zoe,Julia,Kieran
# Expected response (200 OK):
"""
Alice,Joe,Julia,Kieran,Zoe
"""

# POST /sort-names
# With names=Aaaa,Aaaz,Aaab
# Expected response (200 OK):
"""
Aaaa,Aaab,Aaaz
"""

# POST /sort-names
# With no names
# Expected response Invalid Request code:
"""
You didn't submit any names!
"""

3. Test-drive the Route

# POST /sort-names
# With names=Joe,Alice,Zoe,Julia,Kieran
# Expected response (200 OK):
def test_sort_names(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

# POST /sort-names
# With names=Aaaa,Aaaz,Aaab
# Expected response (200 OK):
def test_sort_names_all_a(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Aaaa,Aaab,Aaaz'

# POST /sort-names
# With no names
# Expected response Invalid Request code:
def test_no_names(web_client):
    response = web_client.post('/')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'You didn't submit any names!'


