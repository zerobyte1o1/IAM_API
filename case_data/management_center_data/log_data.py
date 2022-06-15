from apis.base.base_api import BaseApi
from apis.management_center.log_apis import Log
from apis.management_center.user_apis import User
import time
import datetime


class LogData(BaseApi):
    user = User()

    def get_log_list_filter(self, end=None, search=None, start=None):
        """
        生成loglist的filter
        @param end: 结束时间，默认为今天结束
        @param search: 用户名查询，默认为当前操作账号的用户名
        @param start: 开始时间，默认为7天前
        @return:生成loglist的filter
        """
        account = self.user.get_me().account
        if start is None:
            start = int(
                time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=-6)), '%Y-%m-%d'))) * 1000
        if end is None:
            end = int(time.mktime(
                time.strptime(str(datetime.date.today() + datetime.timedelta(days=1)), '%Y-%m-%d'))) * 1000 - 1
        if search is None:
            search = account
        variables_temp = self.get_variables(module_name="log", variables_name="role_list_filter")
        args = [("end", end), ("start", start), ("search", search)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    a = LogData()
    res = a.get_log_list_filter()
    print(res)
    b = Log()
    res2 = b.get_log_list(res)
    print(res2)
