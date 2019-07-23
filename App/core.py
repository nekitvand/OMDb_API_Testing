import requests
from App.response import AssertableResponse
import pytest
import os

class ApiCore(object):
    def __init__(self):
        self.api_key = "285a9f81"
        self._base_url = os.environ["BASE_URL"]

    def get(self,query):
        return requests.get(url=f'{self._base_url}?apikey={self.api_key}', params=query)

class CinemaApi(ApiCore):

    def __init__(self):
        super().__init__()

    def get_movie(self,query):
        return AssertableResponse(self.get(query))