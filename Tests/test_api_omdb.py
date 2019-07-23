from App.core import CinemaApi


def test_search_movie_to_title():
    query = {'t':'Matrix'}
    response = CinemaApi().get_movie(query=query)
    assert response.status_code(200)
    assert len(response.field('Title')) > 0

def test_search_movie_to_id():
    query = {'i': 'tt1285016'}
    response = CinemaApi().get_movie(query=query)
    assert response.status_code(200)
    assert len(response.field('Title')) > 88