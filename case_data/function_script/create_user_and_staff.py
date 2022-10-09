from apis.management_center.staff_apis import Staff
from case_data.management_center_data.staff_data import StaffData

# 创建人员总数
num = 60
tenant_code = "1234"
account = "eam1234"
password = "teletraan"

# 创建用户和账号
def create_staff_and_user(**kwargs):
    staff = Staff(**kwargs)
    sd = StaffData(**kwargs)
    staff_data = sd.create_staff_data()
    staff_id = staff.create_staff_apis(staff_data)
    account_data = sd.create_account_data(staff_id)
    res = staff.create_account_apis(account_data)
    print(res)


if __name__ == '__main__':
    for i in range(num):
        print("正在创建第" + str(i + 1) + "个用户")
        create_staff_and_user(account=account, tenant_code=tenant_code, password=password)
    print(str(num) + "个用户创建完成。")
