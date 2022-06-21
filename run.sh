pytest testcase/ --alluredir=./result

allure generate ./result -o ./result/report/ --clean

allure open -h 127.0.0.1 -p 80 ./result/report/