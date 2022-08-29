from apis.base.base_api import BaseApi
from apis.management_center.organization_apis import Organization
from utils.mock import Mock
from apis.management_center.account_apis import Account
from case_data.management_center_data.account_data import AccountData


class OrganizationData(BaseApi):
    def __init__(self, **kwargs):
        self.org = Organization(**kwargs)
        self.account = Account(**kwargs)
        self.account_data = AccountData(**kwargs)

    def get_organization_list_ask(self, organization_id=None, flag=True):
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
        args=list()
        variables_temp = self.get_variables(module_name="organization", variables_name="create_organization")
        if org_id is None:
            org_id = self.org.get_organization_tree_nodes()[0]["id"]
        # account_list_filter = self.account_data.account_list_filter([{"id": org_id}])
        # org_user = self.account.get_account_list(account_list_filter).data[0].id
        args.append(("name", self.mock.mock_data("organization")))
        # args.append(("manager", {"id": org_user}))
        args.append(("code", self.faker.msisdn()))
        args.append(("parent", {"id": org_id}))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_organization_ask(self, org_id):
        """
        生成更新组织的请求数据
        @param org_id: 组织id [{"id":id}] 注意该组织必须有user存在
        @return:返回
        """
        args=list()
        variables_temp = self.get_variables(module_name="organization", variables_name="update_organization")
        # org_gen_id = self.org.get_organization_tree_nodes()[0]["id"]
        # account_list_filter = self.account_data.account_list_filter(org_ids=[{"id": org_gen_id}])
        # org_account = self.account.get_account_list(account_list_filter).data[0].id
        args.append(("name", self.mock.mock_data("organization")))
        # args.append(("manager", {"id": org_account}))
        args.append(("code", self.faker.msisdn()))
        args.append(("id", org_id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    org = Organization()
    a = OrganizationData()
    # a = OrganizationData().update_organization_ask()
    # a.
    # Organization().update_organization_api(a)

    # # res = org.get_organization_tree_nodes()
    data = a.update_organization_ask("8c93996f-7a9f-4d0f-b663-50ea4fb92421")
    print(data)
    res = org.update_organization_api({'code': '9449796571756', 'id': '8c93996f-7a9f-4d0f-b663-50ea4fb92421', 'manager': None, 'name': 'organization_CVGIAd'})
    print(res)
