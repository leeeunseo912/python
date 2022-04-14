from models import TblAddr
import sqlite3
from database import con


#전체 목록 얻기 테스트
book = TblAddr.all()
for a in book:
    print(a)

#단일 데이터 추출
print('홍길동197 검색')
item = TblAddr.get('홍길동197')
print(item)
print('홍길동 검색')
item = TblAddr.get('홍길동')
print(item)

#insert 테스트
print('insert 테스트')
item = TblAddr('고길동', '010-9999-9999','인천시')
item.insert()

item = TblAddr.get('고길동')
print(item)

#update 테스트
print("update 테스트")
item.phone = '010-2222-2222'
item.update()
item = TblAddr.get('고길동')
print(item)

#remove 테스트
print("remove 테스트")
item.remove()
item = TblAddr.get('고길동')
print(item)

con.close()