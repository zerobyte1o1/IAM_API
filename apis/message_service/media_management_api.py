from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class MediaManagement(GetTokenHeader):
    def get_meta_channels(self):
        """
        获取所有媒介
        @return: 返回所有媒介信息
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.meta_channels()
        data = endpoint(op)
        res = (op + data).meta_channels
        return res

    def update_meta_channel_api(self, variables):
        """
        更新一个媒介的介绍
        @param variables:
        @return:True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_meta_channel(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_meta_channel
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    mm = MediaManagement()
    res = mm.get_meta_channels()
    print(res[1].id)
