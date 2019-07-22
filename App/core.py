import requests
from App.response import AssertableResponse
import pytest

class ApiCore(object):
    def __init__(self):
        self.api_key = "285a9f81"

    def get(self,query):
        return requests.get(url=f'http://www.omdbapi.com/?apikey={self.api_key}', params=query)

class CinemaApi(ApiCore):

    def __init__(self):
        super().__init__()

    def get_movie(self,query):
        return AssertableResponse(self.get(query))