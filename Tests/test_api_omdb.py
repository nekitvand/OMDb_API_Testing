from App.condition import status_code, body
from App.core import CinemaApi
from hamcrest import has_length,greater_than

def test_search_movie_to_title():
    query = {'t':'Matrix'}
    response = CinemaApi().get_movie(query=query)
    assert response.status_code(200)
    assert len(response.field('Title')) > 0

def test_search_movie_to_id():
    query = {'i': 'tt1285016'}
    response = CinemaApi().get_movie(query=query)
    assert response.status_code(200)
    assert len(response.field('Title')) > 0

def test_search_movie_status_code():
    query = {'t': 'Matrix'}
    response = CinemaApi().get_movie(query=query)
    response.should_have(status_code(200))

def test_search_movie_field():
    query = {'t': 'Matrix'}
    response = CinemaApi().get_movie(query=query)
    response.should_have(body("$.Title",has_length(greater_than(0))))