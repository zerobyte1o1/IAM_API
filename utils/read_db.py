import os
import psycopg2.pool
import configparser


# ================读取db_config.ini文件设置=================
class ReadDB:
    root_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_path, "db_config.ini")
    cf = configparser.ConfigParser()
    cf.read(config_path, encoding='UTF-8')
    host = cf.get("test2", "host")
    port = cf.get("test2", "port")
    db = cf.get("test2", "db")
    user = cf.get("test2", "function_script")
    password = cf.get("test2", "password")
    conn = psycopg2.connect(
        host=host, port=port, user=user, password=password, dbname=db)
    cur = conn.cursor()

    def select_count_of_bom_is_released_or_not(self, company_id: int, is_released: bool):
        sql = "select count(*) from bom " \
              "where is_deleted is False " \
              "and company_id = " + str(company_id) + \
              "and is_released is " + str(is_released)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result


if __name__ == '__main__':
    r = ReadDB()
    print(r.select_count_of_bom_is_released_or_not(company_id=11, is_released=True)[0])
