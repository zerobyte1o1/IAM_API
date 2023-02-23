from apis.platform_management.feature_pack import FeaturePack
from apis.platform_management.tenant_apis import Tenant
from apis.management_center.staff_apis import Staff
from case_data.platform_management_data.feature_pack_data import FeaturePackData
from case_data.platform_management_data.tenant_data import TenantData
from case_data.management_center_data.staff_data import StaffData

# def init_tenant(**kwargs)
#     tenant = Tenant(**kwargs)
#     tenant_data = TenantData(**kwargs)
#     feature = FeaturePack(**kwargs)
#     f_data = FeaturePackData(**kwargs)
#     # 创建功能包
#     add_data = f_data.create_feature_pack_data()
#     feature_id = feature.create_feature_pack_api(add_data)
#     add_power_data = f_data.set_permissions_to_feature_pack_data(feature_id)
#     feature.set_permissions_to_feature_pack_api(add_power_data)
#     feature.confirm_feature_pack_api(feature_id)
#     # 创建企业
#     create_data = tenant_data.create_tenant_ask()
#     tenant_id = tenant.create_tenant_api(create_data)
#     data = self.tenant_data.add_feature_pack_to_tenant_data(tenant_id,feature_id)
#     res = self.tenant.add_feature_pack_to_tenant_api(data)