from apis.base.get_token_headers import GetTokenHeader
from apis.management_center.user_apis import User
from apis.management_center.staff_apis import Staff
from case_data.management_center_data.user_data import UserData
from case_data.management_center_data.staff_data import StaffData

num = 1
tenant_code = "company01"
account = "company01"
password = "123456"


def create_staff_and_user(**kwargs):
    staff = Staff(**kwargs)
    sd = StaffData(**kwargs)
    staff_data = sd.create_staff_data()
    print(staff_data)
    staff_id = staff.create_staff_apis(staff_data)
    account_data = sd.create_account_data(staff_id)
    print(account_data)
    res = staff.create_account_apis(account_data)
    print(res)


if __name__ == '__main__':
    for i in range(num):
        create_staff_and_user(account=account, tenant_code=tenant_code, password=password)
