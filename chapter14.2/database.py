import MySQLdb
import sqlite3
import sys

try:
    con = MySQLdb.connect(db='iot_db', host='localhost', user='iot', passwd ='6221', port = 3307)
    print("데이터베이스 연결에 성공했습니다.")
except Exception as e:
    print("데이터베이스 연결에 실패했습니다.")
    print(e)
    sys.exit(0)