from apis.base.base_api import BaseApi
from apis.management_center.message_apis import Message
from apis.management_center.account_apis import User
from apis.platform_management.tenant_apis import Tenant


class MessageData(BaseApi):
    def __init__(self, **kwargs):
        self.user = User(**kwargs)
        self.tenant = Tenant(**kwargs)

    def set_channels_of_message_template_data(self):
        args=list()
        tenant_id = self.user.get_me().tenant.id
        message_template_id=self.tenant.get_message_template_list_of_tenant(tenant_id)["data"][0].id
        variables_temp = self.get_variables(module_name="message", variables_name="set_channels_of_message_template")
        args.append(("messageTemplateId",message_template_id))
        args.append(("tenantId", tenant_id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def set_channel_of_message_templates_data(self):
        args=list()
        tenant_id = self.user.get_me().tenant.id
        message_template_id = self.tenant.get_message_template_list_of_tenant(tenant_id)["data"][0].id
        variables_temp = self.get_variables(module_name="message", variables_name="set_channel_of_message_templates")
        args.append(("messageTemplateIds", [message_template_id]))
        args.append(("tenantId", tenant_id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    md = MessageData()
    res=md.set_channel_of_message_templates_data()
    print(res)
