import sqlite3
from models import TblAddr

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT *FROM tblAddr order by name desc")

while True:
    record = cursor.fetchone()
    if record == None : break

    record = TblAddr(*record)
    print(f'이름 : {record.name} 전화번호 : {record.phone}, 주소 : {record.addr}')

cursor.close()
con.close()

