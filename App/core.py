import requests
from App.response import AssertableResponse


class ApiCore(object):
    def __init__(self):
        self.api_key = "285a9f81"

    def get(self,query,url):
        return requests.get(url=f'{url}?apikey={self.api_key}', params=query)

class CinemaApi(ApiCore):

    def __init__(self):
        super().__init__()

    def get_movie(self,query,url):
        return AssertableResponse(self.get(query,url))


