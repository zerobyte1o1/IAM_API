from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
import requests
from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Log(GetTokenHeader):
    def get_log_list(self,filter):
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
        request = requests.post(self.url, headers=self.get_headers(),json={'query': query,'variables':{'filter':filter}},verify=False)
        return request.json()


if __name__ == '__main__':
    a = Log()
    res = a.get_log_list( {
    "end": 1655222399999,
    "search":'admin',
    "start": 1654617600000
  })
    print(res)
