from apis.base.base_api import BaseApi
from apis.management_center.organization_apis import Organization
from utils.mock import Mock
from apis.management_center.user_apis import User
from case_data.user_data import UserData

class OrganizationData(BaseApi):
    org = Organization()
    user = User()
    mock = Mock()
    user_data=UserData()

    def get_organization_list_ask(self, flag=True):
        """
        获得organizationList的请求参数(根节点)
        @param flag:是否需要显示子组织下的组织
        @return:{"id":organization_id,"isChildrenIncluded":true or false}
        """
        organization_id = self.org.get_organization_tree_nodes()[0]["id"]
        variables = {"id": organization_id, "isChildrenIncluded": flag}
        return variables



    def create_organization_ask(self, org_id=None):
        """
        生成创建组织的请求数据
        @param org_id: 组织id [{"id":id}]
        @return:返回
        """
        variables_temp = self.get_variables(module_name="organization", variables_name="create_organization")
        if org_id is None:
            org_id = org.get_organization_tree_nodes()[0]["id"]
        user_list_filter=self.user_data.user_list_filter([{"id": org_id}])
        org_user = self.user.get_user_list(kwargs=user_list_filter).data[0].id
        args = [
            ("name", self.mock.mock_data("organization")),
            ("manager", {"id": org_user}),
            ("code", self.faker.msisdn()),
            ("parent", {"id": org_id})
        ]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_organization_ask(self, org_id):
        """
        生成更新组织的请求数据
        @param org_id: 组织id [{"id":id}]
        @return:返回
        """
        variables_temp = self.get_variables(module_name="organization", variables_name="update_organization")
        if org_id is None:
            org_id = org.get_organization_tree_nodes()[0]["id"]
        user_list_filter=self.user_data.user_list_filter([{"id": org_id}])
        org_user = self.user.get_user_list(kwargs=user_list_filter).data[0].id
        args = [
            ("name", self.mock.mock_data("organization")),
            ("manager", {"id": org_user}),
            ("code", self.faker.msisdn()),
            ("id", org_id)
        ]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

if __name__ == '__main__':
    org = Organization()
    a = OrganizationData().update_organization_ask("a1c97533-4149-4a13-bf73-e4a3bf08a25a")
    # res = org.get_organization_tree_nodes()
    print(a)
