import requests

from apis.base.get_token_headers import GetTokenHeader


class Log(GetTokenHeader):
    def get_log_list(self, filter):
        """
        获取日志信息
        @param filter: loglist请求的filter
        @return: 返回所有日志详情
        """
        query = """query LogList($filter: LogListFilterInput, $limit: Int, $offset: Int, $orderBy: [String!]) {
                      LogList(filter: $filter, limit: $limit, offset: $offset, orderBy: $orderBy) {
                        totalCount
                        data {
                          account
                          payload
                          tenantId
                          action
                          app {
                            id
                            name
                            __typename
                          }
                          code
                          details {
                            detail
                            target
                            __typename
                          }
                          feature
                          id
                          ip
                          occurredAt
                          __typename
                        }
                        __typename
                      }
                    }"""
        request = requests.post(self.url, headers=self.headers,
                                json={'query': query, 'variables': {'filter': filter}}, verify=False)
        return request.json()


if __name__ == '__main__':
    a = Log()
    res = a.get_log_list({
        "end": 1655222399999,
        "search": 'admin',
        "start": 1654617600000
    })
    print(res)
