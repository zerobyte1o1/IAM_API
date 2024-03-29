from apis.base.base_api import BaseApi
from apis.management_center.staff_apis import Staff
from apis.management_center.organization_apis import Organization
from apis.management_center.role_apis import Role


class StaffData(BaseApi):
    def __init__(self, **kwargs):
        self.org = Organization(**kwargs)
        self.role = Role(**kwargs)
        self.staff = Staff(**kwargs)
        self.org_id = self.org.get_organization_tree_nodes()[0]["id"]
        self.org_id_last = self.org.get_organization_tree_nodes()[-1]["id"]

        # self.role_id = self.role.get_role_list().data[0].id

    def staff_list_data(self, **kwargs):
        """

        @param kwargs: includeChildrenOrganizations[boolean],organizations[list],search[strig]
        @return:
        """
        variables_temp = self.get_variables(module_name="staff", variables_name="staff_list")
        args = list()
        args.append(("organizations", [{"id": self.org_id}]))
        if kwargs != {}:
            for search_key in list(kwargs.keys()):
                args_change = (search_key, kwargs[search_key])
                args.append(args_change)
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def create_staff_data(self):
        variables_temp = self.get_variables(module_name="staff", variables_name="create_staff")
        args = list()
        args.append(("email", self.mock.mock_data("email") + self.faker.email()))
        args.append(("name", self.mock.mock_data("staff")))
        args.append(("organizations", [{"id": self.org_id}]))
        args.append(("phoneNumber", self.faker.phone_number()))
        args.append(("jobNumber", self.faker.unix_time()))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_staff_data(self, staff_id):
        variables_temp = self.get_variables(module_name="staff", variables_name="update_staff")
        args = list()
        args.append(("id", staff_id))
        args.append(("email", self.faker.email()))
        args.append(("name", self.mock.mock_data("staff")))
        args.append(("organizations", [{"id": self.org_id}]))
        args.append(("phoneNumber", self.faker.phone_number()))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def create_account_data(self, staff_id):
        variables_temp = self.get_variables(module_name="staff", variables_name="create_staff_account")
        args = list()
        args.append(("staff", {"id": staff_id}))
        args.append(("account", self.mock.mock_data("account")))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def transfer_organization_data(self, staff_id):
        variables_temp = self.get_variables(module_name="staff", variables_name="transfer_organization")
        args = list()
        args.append(("targetOrganizationId", self.org_id_last))
        args.append(("staffIds", [staff_id]))
        args.append(("originOrganizationId", self.org_id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    staff_data = StaffData()
    sd = staff_data.transfer_organization_data(staff_id="1b0df721-6cb7-41c4-aade-274662576fac",
                                               target_organization_id=2)
    s
