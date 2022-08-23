from apis.base.base_api import BaseApi
from apis.management_center.account_apis import User
from apis.message_service.meta_template_apis import MetaTemplate


class MetaTemplateData(BaseApi):
    def __init__(self, **kwargs):
        self.meta_template = MetaTemplate(**kwargs)
        self.user = User(**kwargs)

    def create_meta_template_ask(self):
        apps = self.meta_template.get_app_list()
        app_id = [i["id"] for i in apps if i["name"] == "管理中心"][0]
        variables_temp = self.get_variables(module_name="meta_template", variables_name="create_meta_template")
        args = [("app", app_id),
                ("name", self.mock.mock_data("meta_template")),
                ("event", self.mock.mock_data("trigger_event"))]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_meta_template_ask(self, template_id):
        tenant_id=self.user.get_me().tenant.id
        variables_temp = self.get_variables(module_name="meta_template", variables_name="update_meta_template")
        args = [("id", template_id),
                ("name", self.mock.mock_data("meta_template")),
                ("event", self.mock.mock_data("trigger_event")),
                ("tenantId",tenant_id)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    mtd = MetaTemplateData()
    mt = MetaTemplate()
    for i in range(800):
        data = mtd.create_meta_template_ask()
        res = mt.create_meta_template_api(data)
        print(res)
