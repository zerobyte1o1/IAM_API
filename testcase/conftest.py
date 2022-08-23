import os
import sys

import pytest

from apis.management_center.account_apis import User
from apis.message_service.meta_template_apis import MetaTemplate
from apis.platform_management.tenant_apis import Tenant
from case_data.management_center_data.account_data import UserData
from case_data.message_service.meta_template_data import MetaTemplateData
from case_data.platform_management_data.tenant_data import TenantData

data = UserData()
user = User()
tenant = Tenant()
t_data = TenantData()
meta_template = MetaTemplate()
mt_data = MetaTemplateData()


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 创建一下用户、角色
@pytest.fixture(scope="session", autouse=True)
def pre_condition_for_the_satiation():
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # if role_count >= 2:
    #     pass
    # elif role_count < 2:
    #     for i in range(2-role_count):
    #         v_create_role = data.create_role()
    #         function_script.create_role(variables=v_create_role)
    # if user_count >= 5:
    #     pass
    # elif user_count < 5:
    #     for i in range(5-user_count):
    #         v_create_user = data.create_user()
    #         function_script.create_user(variables=v_create_user)


@pytest.fixture(scope="session", autouse=True)
def pre_message():
    # template_data = mt_data.create_meta_template_ask()
    # meta_template_id = meta_template.create_meta_template_api(template_data)
    # add_meta_template_data = t_data.add_meta_templates_to_tenant_ask(function_script.get_me().tenant.id)
    # tenant.add_meta_templates_to_tenant_api(add_meta_template_data)
    # yield meta_template_id
    # try:
    #     meta_template.update_status_of_template_api(meta_template_id, "DISABLED")
    #     meta_template.delete_meta_template_api(meta_template_id)
    # except Exception as e:
    #     pass
    pass

if __name__ == '__main__':
    pre_message()
