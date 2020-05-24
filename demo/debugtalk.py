import configparser
import time
import cx_Oracle
from oracle_con import Ora

conf = configparser.ConfigParser()
conf.read("./config.ini")
db_info = {
        'dbtype': 'oracle',
        'user': 'zhao',
        'pwd': 'zhao',
        'host': '192.168.0.66',
        'port': '1521',
        'sid': 'zhaotest'
    }
con = Ora(db_info)

def sleep(n_secs):
    time.sleep(n_secs)

def get_quota(username):
    # a = 997600
    # print(type(a))
    #
    conn = cx_Oracle.connect('zhao/zhao@192.168.0.66:1521/zhaotest')
    cursor = conn.cursor()
    # sql = "select quota from users where id = (:1)"
    # cursor.execute(sql, ([username]))
    cursor.execute("select quota from users where id = %s"%(username))
    row = cursor.fetchone()
    print("**************")
    print(row[0])
    print(type(row[0]))
    return row[0]

def get_username():
    # return "1000777"
    print(conf.get("CONFIG","username"))
    return conf.get("CONFIG","username")

def get_phone_ver(user):
    query = "SELECT is_auth FROM ( SELECT * FROM user_phones WHERE user_id = %s ORDER BY updated_at DESC  ) WHERE ROWNUM = 1"%user
    line = con.query(query)
    # print(user)
    # print(type(line))
    # print(type(line[0]))
    print(line)
    phone_ver = line[0]["is_auth"]
    if phone_ver == "":
        return 0
    return phone_ver

def clear_address(user):
    query = "delete from user_addresses where user_id = %s"%user
    con.query(query)

# get_phone_ver(1000010)
clear_address(1000010)