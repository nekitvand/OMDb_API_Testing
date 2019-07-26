import jsonpath_rw
from hamcrest import assert_that
import logging


class Condition(object):

    def __init__(self):
        pass


class StatusCodeCondition(Condition):

    def __init__(self,code):
        super().__init__()
        self._status_code = code

    def match(self,response):
        assert response.status_code == self._status_code
        logging.info(f"Assert: Status code should be {self._status_code}")

    def __repr__(self):
        return f"Status code is {self._status_code}"

status_code = StatusCodeCondition


class BodyFieldCondition(Condition):

    def __init__(self,json_path,matcher):
        super().__init__()
        self._json_path = json_path
        self._matcher = matcher

    def match(self,response):
        json = response.json()
        value = jsonpath_rw.parse(self._json_path).find(json)
        assert_that(value,self._matcher)
        logging.info(f"Request status: {self._json_path}, body: {self._matcher}")

    def __repr__(self):
        return f"Body field {self._json_path} {self._matcher}"

body = BodyFieldCondition