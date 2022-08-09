from apis.base.base_api import BaseApi
from apis.platform_management.feature_pack import FeaturePack
from utils.mock import Mock


class FeaturePackData(BaseApi):
    mock = Mock()
    feature_pack = FeaturePack()
    industry = feature_pack.tenant_industry_tree_nodes_api()

    def create_feature_pack_data(self):
        variables_temp = self.get_variables(module_name="feature_pack", variables_name="create_feature_pack")
        args = [("applicableIndustries", [{"id": self.industry[1]["id"]}]),
                ("name", self.mock.mock_data("feature_pack"))]

        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_feature_pack_data(self):
        variables_temp = self.get_variables(module_name="feature_pack", variables_name="update_feature_pack")
        args = [("applicableIndustries", [{"id": self.industry[2]["id"]}]),
                ("name", self.mock.mock_data("feature_pack"))]

        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def set_permissions_to_feature_pack_data(self, tenant_id):
        variables_temp = self.get_variables(module_name="feature_pack",
                                            variables_name="set_permissions_to_feature_pack")
        args = [("featurePack",{"id":tenant_id})]

        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    fp = FeaturePack()
    fd = FeaturePackData()
    # for i in range(10):
    #     data = fd.create_feature_pack_data()
    #     res = fp.create_feature_pack_api(data)
    #     print(res)
    # res = fp.assignable_permissions_of_tenant_api("74b021d0-11db-4269-959e-3c0f2856489b")
    data = fd.set_permissions_to_feature_pack_data("b0136279-1338-4e20-aada-42b58f6d903f")
    res=fp.set_permissions_to_feature_pack_api(data)
    print(res)
