
import time
import cx_Oracle

def sleep(n_secs):
    time.sleep(n_secs)

def get_quota():
    return 997600
    # conn = cx_Oracle.connect('zhao/zhao@192.168.0.66:1521/zhaotest')
    # cursor = conn.cursor()
    # sql = "select quota from users where id = (:1)"
    # cursor.execute(sql, ([username]))

