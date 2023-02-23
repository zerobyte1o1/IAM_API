import ssl
import urllib.request as UR

import yaml
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from utils.env import Env
from utils.switch import Switch
from schema.platform_schema import Mutation, Query


# # 这是简单的发GraphQL请求示例，不依赖自动生成的schema
def login_simple():
    url = ""
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    query = 'mutation login($input: LoginInput!) {login(input: $input) {token}}'
    variables = '''
    {
      "input": {
        "account": "",
        "password": ""
      }
    }
        '''
    endpoint = HTTPEndpoint(url, headers)
    data = endpoint(query, variables)
    print(data, type(data))

# 走代理时，全局取消证书验证，避免报错


class Request:
    get_env = Env()
    url = get_env.get_env()
    account = get_env.get_account()
    password = get_env.get_pwd()

    def __init__(self, proxy_=None):
        switch = Switch()
        is_switch_on = switch.is_proxy_on()
        if is_switch_on is True:
            ssl._create_default_https_context = ssl._create_unverified_context
            proxy_ = "127.0.0.1:8080"
        else:
            pass
        if proxy_:
            proxy = {
                "http": 'http://' + proxy_,
                "https": 'http://' + proxy_
            }
        else:
            proxy = None
        proxy_support = UR.ProxyHandler(proxy)
        # build a new opener that adds authentication and caching FTP handlers
        opener = UR.build_opener(proxy_support, UR.CacheFTPHandler)
        # install it
        UR.install_opener(opener)

    # 这是sgqlc提供的更优雅的请求方式
    def login_right(self):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        endpoint = HTTPEndpoint(url="", base_headers=headers, timeout=3)
        variables = {
            "account": "",
            "password": "",
            "tenant_code": ""
          }
        op = Operation(Mutation)
        login = op.login(input=variables)
        # 指定返回token，不要userid
        # login.token()
        data = endpoint(op)
        res = op + data
        '''
        res = AuthInfo(token=34CkAS3qWpt5xw0O7QX5teMjKUwUnoTh)
        如果res = op + data
        res = Mutation(⬆️res)
        '''
        return res

    def query_project(self, order_by=["-created_at"], **kwargs):
        token = 'Token ' + self.login_right()
        headers = {'accept': 'application/json', 'Content-Type': 'application/json', 'authorization': token}
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers, timeout=3)
        op = Operation(Query)
        pro = op.product_project_list(limit=10, filter=eval(f"{kwargs}"), order_by=order_by)
        pro.data.attachment()
        data = endpoint(op)
        res = (op + data).product_project_list.data
        print(res)

    def json_to_yaml(self):
        j = {
              "attachment": [],
              "bom": {
                "id": 98
              },
              "description": "不知道，瞎搞搞",
              "id": 308
            }
        with open("case_data/temp_v.yaml", "w") as f:
            yaml.safe_dump(data=j, stream=f, allow_unicode=True)

    def yaml_to_json(self):
        y = yaml.safe_load(open("case_data/variables_test2.yaml"))
        res = y["project"]["add_product_task"]
        print(res)

    def change(self):
        j = {
            "project": {
                "id": 178
            },
            "task": [
                {
                    "executive": {
                        "id": "b8e2c7cc-6198-48ab-9faa-e2d9cb410f4b"
                    },
                    "name": "task_name_a_QbcF1h",
                    "participant": [
                        {
                            "id": "b8e2c7cc-6198-48ab-9faa-e2d9cb410f4b"
                        }
                    ],
                    "planEndAt": 1644163200000,
                    "planStartAt": 1644163200000
                }
            ]
        }
        j["task"][0]["name"] = "啊？"
        print(j)

    def yy(self):
        for i in [1, 3]:
            res = []
            if i == 3:
                for j in range(3):
                    res.append(j)
                    j += 1
                break
            elif i != 3:
                continue
        return res


if __name__ == "__main__":
    # r = Request()
    # print(r.login_right())
    # r.yaml_to_json()
    # r.query_project()
    # c = r.yy()
    # print(c)
    # r.json_to_yaml()
    login_simple()
