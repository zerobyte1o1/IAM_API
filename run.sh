pytest testcase/ --alluredir=./result

/opt/homebrew/bin/allure generate ./result -o ./result/report/

/opt/homebrew/bin/allure open -h 127.0.0.1 -p 8080 ./result/report/