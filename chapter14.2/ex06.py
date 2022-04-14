import sqlite3
from models import TblAddr

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("DELETE FROM tblAddr WHERE name = '김상형'")
con.commit()

cursor.close()
con.close()

