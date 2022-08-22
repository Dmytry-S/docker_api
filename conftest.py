import os
import pytest
from source.services import UserService


@pytest.fixture(scope='class', autouse=True)
def user_id():
    user_name = os.environ['USER_NAME']
    user_job = os.environ['USER_JOB']
    user = {"name": user_name, "job": user_job}
    response = UserService().create_user(user)
    assert response.status_code(201)
    json_data = response.parse_response()
    users_id = json_data['id']
    return users_id
