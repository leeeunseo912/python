import sqlite3
from models import TblAddr

def main():
    con = sqlite3.connect('addr.db')
    print('db 연결 성공')
    cursor = con.cursor()

    cursor.execute("SELECT * FROM tblAddr")

    table = cursor.fetchall() #데이터가 없는 경우 [] 리턴

    table = list(map(lambda r : TblAddr(*r), table))

    for record in table:
        # print(f'이름: {record[0]}, 전화번호: {record[1]}, 주소: {record[2]}')
        print(f'이름 : {record.name}, 전화번호 : {record.phone}, 주소 : {record.addr}')
        
    cursor.close()
    con.close()

main()