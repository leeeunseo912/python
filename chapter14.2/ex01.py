import sqlite3
con = sqlite3.connect('addr.db')
print('db 연결 성공')
cursor = con.cursor()

cursor.execute('DROP TABLE IF EXISTS tblAddr')
cursor.execute("""
CREATE TABLE tblAddr(
    name CHAR(16) PRIMARY KEY,
    phone CHAR(16),
    addr TEXT
)
""")


cursor.execute("insert into tblAddr values('김상형' ,'123-4567','오산')")
cursor.execute("insert into tblAddr values('한경은' ,'555-4567','수원')")
cursor.execute("insert into tblAddr values('한주완' ,'777-4567','대전')")


for ix in range(1,201):
    sql = f"INSERT INTO tblAddr VALUES('홍길동{ix:03}','010-1111-{ix:04}','서울')"
    print(sql)
    cursor.execute(sql)

con.commit()

cursor.close()
con.close()