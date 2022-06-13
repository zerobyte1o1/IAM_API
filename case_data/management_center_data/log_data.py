from apis.base.base_api import BaseApi
from apis.management_center.log_apis import Log
import time
import datetime


class LogData(BaseApi):
    def get_log_list_filter(self, end=None, search=None, start=None):
        if start is None:
            start = int(
                time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=-6)), '%Y-%m-%d'))) * 1000
        if end is None:
            end = int(time.mktime(
                time.strptime(str(datetime.date.today() + datetime.timedelta(days=1)), '%Y-%m-%d'))) * 1000 - 1
        variables_temp = self.get_variables(module_name="log", variables_name="role_list_filter")
        args = [("end", end), ("start", start), ("search", search)]
        variables = self.modify_variables(target_json=variables_temp,args=args)
        return variables


if __name__ == '__main__':
    a = LogData()
    res = a.get_log_list_filter()
    print(res)
