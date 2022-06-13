from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Log(GetTokenHeader):
    def log_list(self, log_filter):
        """
        获取操作日志
        @param log_filter: filter请求参数
        @return:查询出的所有log详情
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.log_list(filter=log_filter)
        data = endpoint(op)
        res = (op + data).log_list
        return res
