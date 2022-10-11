# IAM接口自动化测试代码开发进度
## 管理中心
-[X] 用户模块已完成
-[X] 角色模块已完成
-[X] 组织模块已完成
-[X] 认证设置已完成
-[X] 日志查询已完成
-[X] 企业设置
-[X] 消息中心
## 平台管理
-[X] 企业管理
    -[X] 企业基本信息
    -[X] 平台管理企业权限分配
    -[X] 平台管理消息模板
## 消息服务
-[X] 推送模板
-[X] 媒介管理


# 运行说明
-  在根目录下的 run.sh文件可以直接运行自动化代码
```shell
pytest testcase/ --alluredir=./result
# 需更换至运行环境的allure路径
/opt/homebrew/bin/allure generate ./result -c -o ./result/report/

/opt/homebrew/bin/allure serve ./result/ -p 8080
```

# 代码调试说明
- 调试单个测试用例时，在utils/env.yml文件中将debug改为True即可。
- run.py 运行时改为False

# 更新日志
## 2022.10.11
- 更新base_api中的modify_variables方法，能够深层的赋值，只需要用":"隔开即可。
