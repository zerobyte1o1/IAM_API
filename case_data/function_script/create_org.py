from apis.management_center.organization_apis import Organization
from case_data.management_center_data.organization_data import OrganizationData

# 创建组织
# 根组织数
num = 1000
# 组织深度
deep = 3
# tenant_code = "comba"
# account = "comba_admin"
# password = "comba_admin"


# 创建组织
def create_org(**kwargs):
    org = Organization(**kwargs)
    org_id = org.get_organization_tree_nodes()[0]["id"]
    if "-" in org_id:
        for i in range(num):
            a = OrganizationData(**kwargs)
            print("正在创建第" + str(i + 1) + "个组织")
            data = a.create_organization_ask(org_id)
            new_org_id = org.create_organization_api(data)
            for j in range(deep):
                data = a.create_organization_ask(new_org_id)
                new_org_id = org.create_organization_api(data)
            print(new_org_id)


if __name__ == '__main__':
    create_org()
    print(str(num) + "个组织创建完成。")
