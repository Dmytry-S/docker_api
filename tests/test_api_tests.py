import os
from source.services import UserService


class TestApiTest:

    def test_read_user(self, user_id):
        end_point = os.environ['END_POINT']
        response = UserService().read_user(end_point, user_id)
        assert response.status_code(404)

    def test_delete_user(self, user_id):
        end_point = os.environ['END_POINT']
        response = UserService().delete_user(end_point, user_id)
        assert response.status_code(204)
