import json
import os
import requests
from source.response import AssertResponse


class ApiTestService(object):

    def __init__(self):
        self.base_url = os.environ['BASE_URL']
        self.end_point = os.environ['END_POINT']

    def post(self, body):
        return requests.post(self.base_url + self.end_point, data=json.dumps(body),
                             headers={'content-type': 'application/json'})

    def get(self, user_id):
        return requests.get(self.base_url + self.end_point + user_id)

    def delete(self, user_id):
        return requests.delete(self.base_url + self.end_point + user_id)


class UserService(ApiTestService):

    def __init__(self):
        super().__init__()

    def create_user(self, user):
        return AssertResponse(self.post(user))

    def read_user(self, end_point, user_id):
        return AssertResponse(self.get(end_point))

    def delete_user(self, end_point, user_id):
        return AssertResponse(self.delete(end_point))