# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

#Test-Driving Routes | Exercise One:

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

#Test-Driving Routes | Exercise Two:

"""
When: I make a POST request to /sort-names
And: I send names "Joe,Alice,Zoe,Julia,Kieran" as the body parameter in text
Then: I should get a 200 response and the names returned in alphabetical order 
"""
def test_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"

"""
When: I make a POST request to /sort-names
And: I send names with the same first 3 letters "Aaaa, Aaaz, Aaab" as the body parameter in text
Then: I should get a 200 response and the names returned in alphabetical order
"""
def test_sort_names_all_a(web_client):
    response = web_client.post('/sort-names', data={'names': 'Aaaa,Aaaz,Aaab'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Aaaa,Aaab,Aaaz"

"""
When: I make a POST request to /sort-names
And: I don't submit any names
Then: I should get a 404 error response and message
"""
def test_no_names(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "You didn't submit any names!" 

#Test-Driving Routes | Challenge One:  

"""
When: I make a GET request to add to /names
And: I add one name
Then: I should get a 200 response and the name should be returned along with the pre-defined names
"""
def test_get_added_name(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'  

"""
When: I make a GET request to add a different name to /names
And: I add this name
Then: I should get a 200 response and the name should be returned along with the pre-defined names
"""
def test_get_added_different_name(web_client):
    response = web_client.get('/names?add=John')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, John'         

"""""
When: I make a GET request to /names
And: I don't add any query parameter
Then: I should get a 200 response and the pre-defined list of names should be returned 
"""
def test_no_name_added(web_client):
    response = web_client.get('/names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "You didn't add a name."    




