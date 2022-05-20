import os
import ssl
import urllib.request as ur

import yaml

from utils.env import Env
from utils.switch import Switch


class BaseApi:
    get_env = Env()
    url = get_env.get_env()
    account = get_env.get_account()
    password = get_env.get_pwd()
    env_name = get_env.get_env_name()

    def __init__(self, proxy_=None):
        switch = Switch()
        is_switch_on = switch.is_proxy_on()
        if is_switch_on is True:
            # 走代理时，全局取消证书验证，避免报错
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
        proxy_support = ur.ProxyHandler(proxy)
        # build a new opener that adds authentication and caching FTP handlers
        opener = ur.build_opener(proxy_support, ur.CacheFTPHandler)
        # install it
        ur.install_opener(opener)

    def get_variables(self, module_name: str, variables_name: str):
        """
        :param module_name:
        :param variables_name: for instance: variables_name="create_product_project_temp"
        :return: json
        """
        root_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        path = os.path.join(root_path, "case_data/variables_" + self.env_name + ".yaml")
        variables = yaml.safe_load(open(path))
        res = variables[module_name][variables_name]
        return res

    def modify_variables(self, target_json, args: list):
        """
        CAUTION: 只支持一级字段;

        :param target_json: 目标Json, 配合method get_variables使用
        :param args: 列表形式的参数, 记录目标参数和修改后的效果。for instance:
            args=[("name", "jojo"), ("code", "jojo")]
        :return: Json after modified
        """
        json_temp = target_json
        for (target, change_to) in args:
            json_temp[target] = change_to
        return json_temp


if __name__ == '__main__':
    b = BaseApi()
    t = b.get_variables(module_name="project", variables_name="create_product_project")
    res1 = b.modify_variables(target_json=t, args=[("a?", "jojo5"), ("code", "jojo5")])
    print(res1)
