from dataclasses import dataclass
from database import con

# 데이터베이스를 위한 모델 클래스명 관례
# 클래명 관례 준수(파스칼 표기법)
# 테이블명의 단수형과 일치

@dataclass
class TblAddr:
    name : str
    phone : str
    addr : str

    def insert(self):
        cursor = con.cursor()
        sql = f"insert into tblAddr values('{self.name}', '{self.phone}', '{self.addr}')"
        cursor.execute(sql)
        con.commit()
        cursor.close()

    @classmethod
    def all(cls):
        cursor = con.cursor()
        sql = 'select * from tblAddr'
        cursor.execute(sql)
        records = cursor.fetchall()
        records = list(map(lambda r : cls(*r), records))

        cursor.close()
        return records

    # 키 컬럼으로 1개 찾기
    @classmethod
    def get(cls, pk):
        cursor = con.cursor()
        sql = f"select *from tblAddr where name = '{pk}'"
        cursor.execute(sql)
        record = cursor.fetchone()
        if record:
            record = cls(*record)

        return record


    def update(self):
        cursor = con.cursor()
        sql = f"""
            update tblAddr
            set
                phone = '{self.phone}',
                addr = '{self.addr}'
            where name = '{self.name}'
        
        """
        cursor.execute(sql)
        con.commit()
        cursor.close()

    def remove(self):
        cursor = con.cursor()
        sql = f"delete from tblAddr where name = '{self.name}'"
        cursor.execute(sql)
        con.commit()
        cursor.close()

if __name__ == '__main__':
    record = ('김상형', '010-1111-1111','부산')

    print(record)   #매개변수의 개수 1개(튜플)
    print(*record)  #매개변수의 개수 3개(콜렉션의 요소 수만큼)

    a = TblAddr(*record)
    # print(a)