from apis.base.base_api import BaseApi
from apis.management_center.staff_apis import Staff
from apis.management_center.organization_apis import Organization
from apis.management_center.role_apis import Role
from utils.mock import Mock


class StaffData(BaseApi):
    org = Organization()
    role=Role()
    org_id = org.get_organization_tree_nodes()[0]["id"]
    role_id = role.get_role_list().data[0].id
    mock = Mock()

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
        args.append(("email", self.faker.email()))
        args.append(("name", self.mock.mock_data("staff")))
        args.append(("organizations", [{"id": self.org_id}]))
        args.append(("phoneNumber", self.faker.phone_number()))
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

    def create_staff_account_data(self,staff_id):
        variables_temp = self.get_variables(module_name="staff", variables_name="create_staff_account")
        args = list()
        args.append(("id", staff_id))
        args.append(("account",self.mock.mock_data("account")))
        args.append(("roles",[{"id":self.role_id}]))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

if __name__ == '__main__':
    sd = StaffData()
    s = Staff()
    data=sd.staff_list_data()
    res = s.get_staff_list(data).data
    print('9bdff1ff-9bc9-4505-9752-c79bcaaa264f' in str(res))
