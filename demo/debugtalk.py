import configparser
import time
import cx_Oracle

conf= configparser.ConfigParser()
conf.read("./config.ini")

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
