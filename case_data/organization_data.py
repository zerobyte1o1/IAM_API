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

    def get_organization_list_ask(self,organization_id=None, flag=True):
        """
        获得organizationList的请求参数(根节点)
        @param organization_id: 组织id
        @param flag:是否需要显示子组织下的组织
        @return:{"id":organization_id,"isChildrenIncluded":true or false}
        """
        if organization_id is None:
            organization_id = self.org.get_organization_tree_nodes()[0]["id"]
        variables = {"id": organization_id, "isChildrenIncluded": flag}
        return variables



    def create_organization_ask(self, org_id=None):
        """
        生成创建组织的请求数据
        @param org_id: 组织id [{"id":id}] None时为默认创建在根节点下
        @return:返回
        """
        variables_temp = self.get_variables(module_name="organization", variables_name="create_organization")
        if org_id is None:
            org_id = self.org.get_organization_tree_nodes()[0]["id"]
        user_list_filter=self.user_data.user_list_filter([{"id": org_id}])
        org_user = self.user.get_user_list(user_list_filter).data[0].id
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
            org_id = org.get_organization_tree_nodes()[-1]["id"]
        user_list_filter=self.user_data.user_list_filter(org_ids=[{"id": org_id}])
        org_user = self.user.get_user_list(user_list_filter).data[0].id
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
    # a = OrganizationData().update_organization_ask()
    # a.
    # Organization().update_organization_api(a)

    # # res = org.get_organization_tree_nodes()
    b=OrganizationData().get_organization_list_ask()
    print(b)
