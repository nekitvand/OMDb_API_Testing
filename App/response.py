import logging

class AssertableResponse(object):

    def __init__(self, response):
        self._response = response
        logging.info(f"Request url: {response.request.url}, body: {response.request.body}")
        logging.info(f"Request status: {response.status_code}, body: {response.text}")

    def status_code(self, code):
        logging.info(f"Assert: Status code should be {code}")
        return self._response.status_code == code

    def field(self,name):
        logging.info(f"Assert: Name field should be {name}")
        return self._response.json()[name]
