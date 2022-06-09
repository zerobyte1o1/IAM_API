import pytest

from apis.management_center.user_apis import User
from case_data.management_center_data.user_data import UserData


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


data = UserData()
user = User()
user_count = data.user_count()
role_count = data.role_count()


# 创建一下用户、角色
@pytest.fixture(scope="session", autouse=True)
def pre_condition_for_the_satiation():
    if role_count >= 2:
        pass
    elif role_count < 2:
        for i in range(2-role_count):
            v_create_role = data.create_role()
            user.create_role(variables=v_create_role)
    if user_count >= 5:
        pass
    elif user_count < 5:
        for i in range(5-user_count):
            v_create_user = data.create_user()
            user.create_user(variables=v_create_user)

