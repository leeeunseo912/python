import sqlite3
from models import TblAddr

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT *FROM tblAddr WHERE name = '김상형'")

record = cursor.fetchone()
print(record)

if record :
    record = TblAddr(*record)
    print(f'김상형은 {record.addr}에 살고 있습니다.')
else :
    print("김상형은 없는 이름입니다.")

cursor.close()
con.close()

