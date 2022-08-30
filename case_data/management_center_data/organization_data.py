from apis.base.base_api import BaseApi
from apis.management_center.organization_apis import Organization
from utils.mock import Mock
from apis.management_center.staff_apis import Staff
from case_data.management_center_data.staff_data import StaffData


class OrganizationData(BaseApi):
    def __init__(self, **kwargs):
        self.org = Organization(**kwargs)
        self.staff = Staff(**kwargs)
        self.staff_data = StaffData(**kwargs)

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
        data=self.staff_data.staff_list_data()
        staff_id=self.staff.get_staff_list(data).data[0]["id"]
        args.append(("name", self.mock.mock_data("organization")))
        args.append(("manager", {"id": staff_id}))
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
        data = self.staff_data.staff_list_data()
        staff_id = self.staff.get_staff_list(data).data[0]["id"]
        args.append(("name", self.mock.mock_data("organization")))
        args.append(("manager", {"id": staff_id}))
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
    data = a.update_organization_ask("ac277180-c3af-4233-a124-438a18163780")
    print(data)
    res = org.update_organization_api(data)
    print(res)
