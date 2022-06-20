from apis.base.base_api import BaseApi
from apis.management_center.user_apis import User
from apis.message_service.media_management_api import MediaManagement
from utils.mock import Mock


class MediaManagementData(BaseApi):

    def update_meta_channel_ask(self, meta_id):
        variables_temp = self.get_variables(module_name="meta_management", variables_name="update_meta_management")
        args = [("description", self.faker.text()),
                ("id", meta_id)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    md = MediaManagementData()
    data = md.update_meta_management_ask("email")
    print(data)
