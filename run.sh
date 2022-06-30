pytest testcase/ --alluredir=./result --clean-alluredir

allure generate ./result -c -o ./result/report/

allure serve ./result/ -p 8080